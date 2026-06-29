# Ecommerce Playwright Automation Framework

This repository contains end-to-end UI tests for [Automation Exercise](https://automationexercise.com/) using Python, `pytest`, and Playwright.

The suite covers the main storefront flows implemented in the current codebase: authentication, signup, contact form submission, cart actions, checkout and payment, and basic page validation.

## Tech Stack

- Python
- `pytest`
- `playwright`
- `pytest-playwright`
- `pytest-html`

## Project Structure

```text
.
├── conftest.py
├── helpers/
│   ├── __init__.py
│   └── user_actions.py
├── images/
│   └── shirt.jpg
├── pages/
│   ├── base_page.py
│   ├── cart_page.py
│   ├── login_page.py
│   └── payment_page.py
├── pytest.ini
├── README.md
├── reports/
│   ├── assets/
│   └── report.html
├── requirements.txt
└── tests/
    ├── test_auth.py
    ├── test_cart.py
    ├── test_contact_form.py
    ├── test_payment.py
    └── test_verify_pages.py
```

## Test Coverage

### Authentication and Signup

[`tests/test_auth.py`](/home/adelelakour/ecommerce-playwright-automation-framework/tests/test_auth.py)

- Valid login
- Invalid login
- Blank login validation
- Account creation with randomized email data
- Invalid signup email validation

### Contact Us

[`tests/test_auth.py`](/home/adelelakour/ecommerce-playwright-automation-framework/tests/test_auth.py) and [`tests/test_contact_form.py`](/home/adelelakour/ecommerce-playwright-automation-framework/tests/test_contact_form.py)

- Submit the Contact Us form through a page object
- Upload `images/shirt.jpg`
- Accept the browser confirmation dialog
- Exercise a direct form submission flow

### Cart

[`tests/test_cart.py`](/home/adelelakour/ecommerce-playwright-automation-framework/tests/test_cart.py)

- Add products with custom quantities
- Open the cart after adding items
- Remove an item from the cart

### Payment and Checkout

[`tests/test_payment.py`](/home/adelelakour/ecommerce-playwright-automation-framework/tests/test_payment.py)

- Login through a shared fixture
- Reuse a shared cart fixture
- Complete checkout
- Submit payment details and confirm the order

### Navigation and Product Pages

[`tests/test_verify_pages.py`](/home/adelelakour/ecommerce-playwright-automation-framework/tests/test_verify_pages.py)

- Verify the Test Cases page
- Verify product details content
- Search for a product and validate results

## Framework Design

### Page Objects

The `pages/` package contains small page-object classes for reusable actions:

- [`pages/login_page.py`](/home/adelelakour/ecommerce-playwright-automation-framework/pages/login_page.py): login, signup, and contact form interactions
- [`pages/cart_page.py`](/home/adelelakour/ecommerce-playwright-automation-framework/pages/cart_page.py): product add/remove cart flows
- [`pages/payment_page.py`](/home/adelelakour/ecommerce-playwright-automation-framework/pages/payment_page.py): checkout and payment steps

### Fixtures

[`conftest.py`](/home/adelelakour/ecommerce-playwright-automation-framework/conftest.py) defines shared fixtures for:

- `login`: signs in with a fixed account
- `cart_with_products`: preloads the cart with products
- `payment`: returns a helper that fills payment fields

### Helpers

[`helpers/user_actions.py`](/home/adelelakour/ecommerce-playwright-automation-framework/helpers/user_actions.py) contains reusable flow helpers for registration, cart manipulation, and payment processing.

## Setup

1. Create and activate a virtual environment.
2. Install project dependencies.
3. Install Playwright browser binaries.

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
playwright install
```

## Running Tests

Run the full suite:

```bash
pytest
```

Run a single test module:

```bash
pytest tests/test_payment.py
```

Run tests by keyword:

```bash
pytest -k "login"
```

Run in headed mode:

```bash
pytest --headed
```

Generate an HTML report:

```bash
pytest --html=reports/report.html --self-contained-html
```

## Pytest Configuration

[`pytest.ini`](/home/adelelakour/ecommerce-playwright-automation-framework/pytest.ini)

- `base_url = https://automationexercise.com`
- Default `addopts = -v`
- Available markers:
  - `smoke`
  - `regression`
  - `ui`
  - `auth`

## Dependencies

[`requirements.txt`](/home/adelelakour/ecommerce-playwright-automation-framework/requirements.txt)

```text
playwright
pytest
pytest-playwright
pytest-html
python-dotenv
```

## Notes

- The suite targets a live public site, so failures can be caused by site changes, rate limits, popups, or temporary downtime.
- Some flows depend on hard-coded credentials and card values from the local test suite.
- Several tests use randomized email addresses to avoid signup collisions.
- The repository currently includes generated cache folders and an existing HTML report artifact.
