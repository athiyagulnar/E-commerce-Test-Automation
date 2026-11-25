
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


def add_product_and_open_checkout(driver):
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
        EC.element_to_be_clickable((By.ID, "checkout"))
    ).click()

    wait.until(EC.url_contains("checkout-step-one.html"))


def test_checkout_success(driver):
    wait = WebDriverWait(driver, 15)

    add_product_and_open_checkout(driver)

    wait.until(
        EC.visibility_of_element_located((By.ID, "first-name"))
    ).send_keys("Test")

    driver.find_element(By.ID, "last-name").send_keys("User")
    driver.find_element(By.ID, "postal-code").send_keys("500001")

    driver.find_element(By.ID, "continue").click()

    wait.until(EC.url_contains("checkout-step-two.html"))

    wait.until(
        EC.element_to_be_clickable((By.ID, "finish"))
    ).click()

    wait.until(EC.url_contains("checkout-complete.html"))

    confirmation = wait.until(
        EC.visibility_of_element_located(
            (By.CLASS_NAME, "complete-header")
        )
    )

    assert confirmation.text == "Thank you for your order!"


def test_checkout_without_first_name(driver):
    wait = WebDriverWait(driver, 15)

    add_product_and_open_checkout(driver)

    driver.find_element(By.ID, "last-name").send_keys("User")
    driver.find_element(By.ID, "postal-code").send_keys("500001")

    driver.find_element(By.ID, "continue").click()

    error = wait.until(
        EC.visibility_of_element_located(
            (By.CSS_SELECTOR, "[data-test='error']")
        )
    )

    assert "First Name is required" in error.text
