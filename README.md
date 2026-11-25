
# E-commerce Test Automation Framework

## Project Overview
This project is an automated testing framework for an e-commerce website using Python, Selenium WebDriver and Pytest.

## Website
https://www.saucedemo.com/

## Technologies Used
- Python
- Selenium WebDriver
- Pytest
- pytest-html
- Chrome Browser

## Features
- Website launch testing
- Valid login testing
- Invalid login testing
- Add product to cart testing
- Remove product from cart testing
- Checkout testing
- Automatic screenshots when tests fail
- HTML test reports

## Project Structure

E-commerce test Automation framework/
│
├── tests/
│   ├── test_login.py
│   ├── test_cart.py
│   └── test_checkout.py
│
├── reports/
├── screenshots/
├── conftest.py
├── pytest.ini
├── requirements.txt
├── .gitignore
└── README.md

## Installation

Install the required packages:

pip install -r requirements.txt

## Run Tests

python -m pytest

## Generate HTML Report

python -m pytest --html=reports/report.html --self-contained-html

## Expected Result

All seven test cases should pass when the website and browser are working correctly.
