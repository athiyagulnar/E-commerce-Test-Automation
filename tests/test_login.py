
from selenium.webdriver.common.by import By


def test_website_opens(driver):
    assert driver.title == "Swag Labs"


def test_valid_login(driver):
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()
    assert "inventory" in driver.current_url

def test_invalid_login(driver):
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("wrong_password")
    driver.find_element(By.ID, "login-button").click()

    error_message = driver.find_element(
        By.CSS_SELECTOR, "[data-test='error']"
    ).text

    assert "Username and password do not match" in error_message
