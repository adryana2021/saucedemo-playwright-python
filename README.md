# SauceDemo Playwright Automation

UI test automation project for [SauceDemo](https://www.saucedemo.com/) built with Python, Playwright, and Pytest.

## Tech Stack

- Python
- Playwright
- Pytest
- Page Object Model (POM)

## Automated Scenarios

- Invalid login validation
- Add multiple products to cart
- Cart validation
- Complete checkout flow
- Purchase confirmation

## Project Structure

```text
config/
data/
pages/
tests/
conftest.py
pytest.ini
requirements.txt
```

## Run the Tests

Install dependencies:

```bash
pip install -r requirements.txt
```

Run all tests:

```bash
pytest
```

Run the regression suite:

```bash
pytest -m regression
```

Run with the browser visible:

```bash
pytest -m regression --headed -s
```

## Test Design

The framework includes:

- Page Object Model for UI interactions
- Reusable test data
- Pytest markers for test suite organization
- Playwright assertions and auto-waiting
- Separate test files by functionality

## Current Coverage

```text
Login
└── Invalid credentials

Checkout
└── Login
    └── Select multiple products
        └── Cart
            └── Checkout
                └── Complete purchase
```
