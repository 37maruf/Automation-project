"""
Test Case 1: Register User
Steps:
1. Launch browser
2. Navigate to url 'http://automationexercise.com'
3. Verify that home page is visible successfully
4. Click on 'Signup / Login' button
5. Verify 'New User Signup!' is visible
6. Enter name and email address
7. Click 'Signup' button
8. Verify that 'ENTER ACCOUNT INFORMATION' is visible
9. Fill details: Title, Name, Email, Password, Date of birth
10. Select checkbox 'Sign up for our newsletter!'
11. Select checkbox 'Receive special offers from our partners!'
12. Fill details: First name, Last name, Company, Address, Address2, Country, State, City, Zipcode, Mobile Number
13. Click 'Create Account button'
14. Verify that 'ACCOUNT CREATED!' is visible
15. Click 'Continue' button
16. Verify that 'Logged in as username' is visible
17. Click 'Delete Account' button
18. Verify that 'ACCOUNT DELETED!' is visible and click 'Continue' button
"""
from pages.login_page import LoginPage
from pages.account_page import AccountInformationPage, AccountCreatedPage, AccountDeletedPage
from utils.helpers import generate_unique_email, generate_random_name


def test_register_user(home_page):
    # Steps 1 & 2 (launch browser + open the website) are done by the 'home_page' fixture
    page = home_page.page

    name = generate_random_name()
    email = generate_unique_email()
    password = "Test@1234"

    # Step 3: verify home page is visible
    assert home_page.is_home_page_visible()
    print("Home page is visible")

    # Step 4: click 'Signup / Login'
    home_page.go_to_signup_login_page()

    # Step 5: verify 'New User Signup!' is visible
    login_page = LoginPage(page)
    assert login_page.is_new_user_signup_visible()
    print("'New User Signup!' is visible")

    # Steps 6 & 7: enter name + email and click Signup (reusable function)
    login_page.start_signup(name, email)

    # Step 8: verify 'ENTER ACCOUNT INFORMATION' is visible
    account_info_page = AccountInformationPage(page)
    assert account_info_page.is_heading_visible()
    print("'ENTER ACCOUNT INFORMATION' is visible")

    # Step 9: title, name, email, password, date of birth
    # (the email box is already filled by the site, so we only check it)
    account_info_page.fill_account_information(
        name=name, password=password, day="10", month="5", year="1995"
    )
    assert account_info_page.get_email_value() == email
    print("Account information filled")

    # Steps 10 & 11: tick both checkboxes
    account_info_page.select_newsletter_checkbox()
    account_info_page.select_offers_checkbox()
    assert account_info_page.newsletter_checkbox.is_checked()
    assert account_info_page.offers_checkbox.is_checked()
    print("Newsletter and special offers checkboxes selected")

    # Step 12: address details (reusable function)
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

    # Step 13: click 'Create Account'
    account_info_page.click_create_account()

    # Step 14: verify 'ACCOUNT CREATED!'
    account_created_page = AccountCreatedPage(page)
    assert account_created_page.get_confirmation_text().upper() == "ACCOUNT CREATED!"
    print("'ACCOUNT CREATED!' is visible")

    # Step 15: click 'Continue'
    account_created_page.click_continue()

    # Step 16: verify 'Logged in as username'
    assert home_page.is_logged_in_as(name)
    print(f"'Logged in as {name}' is visible")

    # Step 17: click 'Delete Account'
    home_page.click_delete_account()

    # Step 18: verify 'ACCOUNT DELETED!' and click 'Continue'
    account_deleted_page = AccountDeletedPage(page)
    assert account_deleted_page.get_confirmation_text().upper() == "ACCOUNT DELETED!"
    print("'ACCOUNT DELETED!' is visible")
    account_deleted_page.click_continue()
