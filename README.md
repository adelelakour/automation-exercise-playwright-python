# Automation Exercise UI Test Suite

This repository contains end-to-end UI tests for [Automation Exercise](https://automationexercise.com/) using Python, `pytest`, and Playwright. The suite covers core user journeys such as account registration, authentication, product browsing, contact form submission, and checkout.

## Overview

The tests are written against the public Automation Exercise demo site and are intended to validate common browser-based workflows:

- User registration with a unique email address
- Login with valid and invalid credentials
- Logout flow
- Contact form submission with file upload
- Product listing, product details, and search
- Add-to-cart and checkout flow

## Tech Stack

- Python
- `pytest`
- Playwright for Python

## Project Structure

```text
.
├── conftest.py
├── images/
│   └── shirt.jpg
├── pytest.ini
├── requirements.txt
├── tests/
│   ├── test_buy_item.py
│   ├── test_contact_form.py
│   ├── test_registrayion.py
│   └── test_verify_pages.py
├── reports/
├── screenshots/
└── utils/
```

## Test Coverage

### Registration and Authentication

[`tests/test_registrayion.py`](/home/adelelakour/automation-exercise-playwright-python/tests/test_registrayion.py)

- Register a new user with randomized email data
- Attempt registration with an existing email
- Login with valid credentials
- Login with invalid credentials
- Logout flow

### Contact Form

[`tests/test_contact_form.py`](/home/adelelakour/automation-exercise-playwright-python/tests/test_contact_form.py)

- Submit the contact form
- Upload an attachment from `images/shirt.jpg`

### Product and Navigation Checks

[`tests/test_verify_pages.py`](/home/adelelakour/automation-exercise-playwright-python/tests/test_verify_pages.py)

- Verify the Test Cases page
- Verify product listing and product details
- Verify product search

### Cart and Checkout

[`tests/test_buy_item.py`](/home/adelelakour/automation-exercise-playwright-python/tests/test_buy_item.py)

- Login
- Add a product to cart
- Proceed to checkout
- Submit payment details

## Prerequisites

Before running the suite, make sure you have:

- Python 3.10+ installed
- `pip` available
- Playwright browser binaries installed

## Setup

Create and activate a virtual environment, then install the required tools.

```bash
python -m venv .venv
source .venv/bin/activate
pip install pytest pytest-playwright playwright
playwright install
```

If you prefer to use `requirements.txt`, populate it with the project dependencies first or install the packages directly as shown above.

## Running the Tests

Run the full suite:

```bash
pytest
```

Run a single test file:

```bash
pytest tests/test_buy_item.py
```

Run a single test by name:

```bash
pytest -k "login_correct_credential"
```

Run in headed mode:

```bash
pytest --headed
```

## Notes and Assumptions

- The suite depends on the live availability and current behavior of `https://automationexercise.com/`.
- Some tests use hard-coded credentials and payment data intended for demo-site automation only.
- The registration flow generates a random email to reduce collisions.
- Browser state, screenshots, and reports directories already exist in the repository, but their generation depends on how `pytest` and Playwright are configured locally.
- `conftest.py`, `pytest.ini`, and `requirements.txt` are currently present but empty in this repository.

## Known Limitations

- Several tests rely on static user credentials, which can make them environment-sensitive.
- The suite currently has minimal shared fixtures/configuration.
- The test file `test_registrayion.py` contains a filename typo, but it does not prevent `pytest` from collecting the tests.

## Future Improvements

- Add a populated `requirements.txt`
- Add shared fixtures to `conftest.py`
- Configure screenshots, traces, and HTML reporting
- Move test data and credentials into dedicated config or environment variables
- Improve assertions for post-login, logout, and successful checkout outcomes

## License

This project is for educational and automation practice purposes.
