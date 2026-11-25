
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def login(driver):
    wait = WebDriverWait(driver, 15)

    wait.until(
        EC.visibility_of_element_located((By.ID, "user-name"))
    ).send_keys("standard_user")

    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    wait.until(EC.url_contains("inventory.html"))


def test_add_product_to_cart(driver):
    wait = WebDriverWait(driver, 15)

    login(driver)

    wait.until(
        EC.element_to_be_clickable(
            (By.ID, "add-to-cart-sauce-labs-backpack")
        )
    ).click()

    wait.until(
        EC.element_to_be_clickable(
            (By.CLASS_NAME, "shopping_cart_link")
        )
    ).click()

    wait.until(EC.url_contains("cart.html"))

    product = wait.until(
        EC.visibility_of_element_located(
            (By.CLASS_NAME, "inventory_item_name")
        )
    )

    assert product.text == "Sauce Labs Backpack"


def test_remove_product_from_cart(driver):
    wait = WebDriverWait(driver, 15)

    login(driver)

    wait.until(
        EC.element_to_be_clickable(
            (By.ID, "add-to-cart-sauce-labs-backpack")
        )
    ).click()

    wait.until(
        EC.element_to_be_clickable(
            (By.CLASS_NAME, "shopping_cart_link")
        )
    ).click()

    wait.until(EC.url_contains("cart.html"))

    wait.until(
        EC.element_to_be_clickable(
            (By.ID, "remove-sauce-labs-backpack")
        )
    ).click()

    wait.until(
        lambda d: len(d.find_elements(By.CLASS_NAME, "cart_item")) == 0
    )

    assert len(driver.find_elements(By.CLASS_NAME, "cart_item")) == 0
