"""
Test Case 3: Login User with incorrect email and password
Steps:
1. Launch browser
2. Navigate to url 'http://automationexercise.com'
3. Verify that home page is visible successfully
4. Click on 'Signup / Login' button
5. Verify 'Login to your account' is visible
6. Enter incorrect email address and password
7. Click 'login' button
8. Verify error 'Your email or password is incorrect!' is visible
"""
from pages.login_page import LoginPage


def test_login_with_incorrect_credentials(home_page):
    # Steps 1 & 2 (launch browser + open the website) are done by the 'home_page' fixture
    page = home_page.page

    # Step 3: verify home page is visible
    assert home_page.is_home_page_visible()
    print("Home page is visible")

    # Step 4: click 'Signup / Login'
    home_page.go_to_signup_login_page()

    # Step 5: verify 'Login to your account' is visible
    login_page = LoginPage(page)
    assert login_page.is_login_to_your_account_visible()
    print("'Login to your account' is visible")

    # Steps 6 & 7: enter an email/password that do not belong to any account (reusable function)
    login_page.login(email="not_a_real_user_123@example.com", password="wrongPassword123")

    # Step 8: verify the error message
    assert login_page.get_login_error_text() == "Your email or password is incorrect!"
    print("Error 'Your email or password is incorrect!' is visible")
