

import os
import pytest
from selenium import webdriver


@pytest.fixture
def driver():
    browser = webdriver.Chrome()
    browser.maximize_window()
    browser.implicitly_wait(5)

    browser.get("https://www.saucedemo.com/")

    yield browser

    browser.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        browser = item.funcargs.get("driver")

        if browser:
            os.makedirs("screenshots", exist_ok=True)

            screenshot_path = os.path.join(
                "screenshots",
                f"{item.name}.png"
            )

            browser.save_screenshot(screenshot_path)
            print(f"\nScreenshot saved: {screenshot_path}")
