from playwright.sync_api import Page


class LoginPage:
    """
    Represents the 'Login / Signup' page (https://www.automationexercise.com/login).
    This one page has two forms side by side: Login form and Signup form.
    """

    def __init__(self, page: Page):
        self.page = page

        # Login form (left side)
        self.login_heading = page.locator(".login-form h2")
        self.login_email = page.locator('input[data-qa="login-email"]')
        self.login_password = page.locator('input[data-qa="login-password"]')
        self.login_button = page.locator('button[data-qa="login-button"]')
        self.login_error_message = page.locator(".login-form p")

        # Signup form (right side)
        self.signup_heading = page.locator(".signup-form h2")
        self.signup_name = page.locator('input[data-qa="signup-name"]')
        self.signup_email = page.locator('input[data-qa="signup-email"]')
        self.signup_button = page.locator('button[data-qa="signup-button"]')
        self.signup_error_message = page.locator(".signup-form p")

    # ---------- Reusable functions ----------

    def login(self, email: str, password: str):
        """Fills the login form and clicks the Login button."""
        self.login_email.fill(email)
        self.login_password.fill(password)
        self.login_button.click()
        self.page.wait_for_timeout(4000)

    def start_signup(self, name: str, email: str):
        """
        Fills the small signup form (name + email) and clicks 'Signup'.
        This takes the user to the 'Enter Account Information' page.
        """
        self.signup_name.fill(name)
        self.signup_email.fill(email)
        self.signup_button.click()
        self.page.wait_for_timeout(4000)

    # ---------- Getters used for verification ----------

    def is_new_user_signup_visible(self) -> bool:
        return "new user signup!" in self.signup_heading.inner_text().lower()

    def is_login_to_your_account_visible(self) -> bool:
        return "login to your account" in self.login_heading.inner_text().lower()

    def get_login_error_text(self) -> str:
        return self.login_error_message.inner_text().strip()

    def get_signup_error_text(self) -> str:
        return self.signup_error_message.inner_text().strip()
