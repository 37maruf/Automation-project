"""
Reusable 'flows' = a group of steps that many tests need.
Instead of copy-pasting the same steps again and again,
we write them once here and call the function.
"""
from pages.login_page import LoginPage
from pages.account_page import AccountInformationPage, AccountCreatedPage


def register_new_user(home_page, name: str, email: str, password: str):
    """
    Creates a brand-new account from start to finish:
    Home -> Signup/Login -> Signup form -> Account information -> Account created.
    Used as a 'setup' step by tests that need an existing user (e.g. Login test).
    """
    page = home_page.page

    home_page.go_to_signup_login_page()

    login_page = LoginPage(page)
    login_page.start_signup(name, email)

    account_info_page = AccountInformationPage(page)
    account_info_page.fill_account_information(
        name=name, password=password, day="10", month="5", year="1995"
    )
    account_info_page.fill_address_information(
        first_name=name,
        last_name="Tester",
        company="Test Company",
        address="123 Test Street",
        address2="Suite 5",
        country="United States",
        state="Texas",
        city="Austin",
        zipcode="12345",
        mobile_number="1234567890",
    )
    account_info_page.click_create_account()

    account_created_page = AccountCreatedPage(page)
    account_created_page.click_continue()
