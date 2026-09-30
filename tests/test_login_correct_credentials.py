"""
Test Case 2: Login User with correct email and password
Steps:
1. Launch browser
2. Navigate to url 'http://automationexercise.com'
3. Verify that home page is visible successfully
4. Click on 'Signup / Login' button
5. Verify 'Login to your account' is visible
6. Enter correct email address and password
7. Click 'login' button
8. Verify that 'Logged in as username' is visible
9. Click 'Delete Account' button
10. Verify that 'ACCOUNT DELETED!' is visible

NOTE: Login needs an account that already exists. The 'registered_user'
fixture (see conftest.py) creates one before this test starts and logs out.
"""
from pages.login_page import LoginPage
from pages.account_page import AccountDeletedPage


def test_login_with_correct_credentials(home_page, registered_user):
    page = home_page.page

    # Steps 1 & 2: browser is launched by the fixtures, we open the website again
    # (the fixture left us on the login page after logging out)
    home_page.open()

    # Step 3: verify home page is visible
    assert home_page.is_home_page_visible()
    print("Home page is visible")

    # Step 4: click 'Signup / Login'
    home_page.go_to_signup_login_page()

    # Step 5: verify 'Login to your account' is visible
    login_page = LoginPage(page)
    assert login_page.is_login_to_your_account_visible()
    print("'Login to your account' is visible")

    # Steps 6 & 7: enter correct email + password and click login (reusable function)
    login_page.login(email=registered_user["email"], password=registered_user["password"])

    # Step 8: verify 'Logged in as username'
    assert home_page.is_logged_in_as(registered_user["name"])
    print(f"'Logged in as {registered_user['name']}' is visible")

    # Step 9: click 'Delete Account'
    home_page.click_delete_account()

    # Step 10: verify 'ACCOUNT DELETED!'
    account_deleted_page = AccountDeletedPage(page)
    assert account_deleted_page.get_confirmation_text().upper() == "ACCOUNT DELETED!"
    print("'ACCOUNT DELETED!' is visible")
