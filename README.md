# AutomationExercise - Playwright + Pytest (Page Object Model)

Automated tests for https://www.automationexercise.com/ written in the same
style as your sample project: Playwright + pytest + Page Object Model +
reusable functions for repeated steps (login, navigation, form filling).

## Project Structure

```
AutomationExercise/
├── conftest.py            # fixtures: page, home_page, registered_user
├── pytest.ini
├── requirements.txt
├── pages/                 # Page Object Model - one file per page
│   ├── home_page.py       # navbar links, logged-in check, delete account
│   ├── login_page.py      # login(), start_signup()
│   ├── account_page.py    # fill_account_information(), fill_address_information()
│   ├── products_page.py   # search_product(), add_product_to_cart_by_index()
│   └── cart_page.py       # read price / quantity / total of a cart product
├── utils/
│   ├── helpers.py         # generate_unique_email(), generate_random_name(), extract_price_number()
│   └── flows.py           # register_new_user() - repeated steps in one function
└── tests/                 # one test case per file
    ├── test_register_user.py               # Test Case 1
    ├── test_login_correct_credentials.py   # Test Case 2
    ├── test_login_incorrect_credentials.py # Test Case 3
    ├── test_add_products_to_cart.py        # Test Case 4
    └── test_search_product.py              # Test Case 5
```

## Reusable functions (so steps are never copy-pasted)

- Navigation: `home_page.go_to_signup_login_page()`, `home_page.go_to_products_page()`
- Login: `login_page.login(email, password)`
- Signup: `login_page.start_signup(name, email)`
- Form filling: `fill_account_information(...)`, `fill_address_information(...)`
- Whole flow: `register_new_user(...)` in `utils/flows.py`

## Setup

```bash
pip install -r requirements.txt
playwright install chromium
```

## Run all tests (from inside the AutomationExercise folder)

```bash
pytest
```

## Run a single test

```bash
pytest tests/test_register_user.py
```

## Notes for a beginner

- The `home_page` fixture launches the browser and opens the website, so
  Steps 1 and 2 of every test case happen automatically.
- Test Case 2 (login with correct details) needs an existing account, so the
  `registered_user` fixture creates one first, logs out, and gives the test
  the email/password. The test then deletes that account at the end.
- Emails are random each run (`utils/helpers.py`), so you can run the tests
  again and again without an "Email Address already exist!" error.
- If a locator ever stops working, open the page in your browser, right-click
  the element -> Inspect, and update the matching line in `pages/`.
