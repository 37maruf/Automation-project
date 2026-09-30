from playwright.sync_api import Page

BASE_URL = "https://www.automationexercise.com"


class HomePage:
    """
    Represents the Home Page (https://www.automationexercise.com/).
    All the navbar links live here because almost every test starts
    by clicking one of these links.
    """

    def __init__(self, page: Page):
        self.page = page

        # Big banner slider that is only shown on the home page
        self.slider = page.locator("#slider")

        # Navbar links
        # NOTE: the page repeats some of these same links elsewhere (e.g. a
        # "View Cart" link inside a hidden popup), so we scope every locator
        # to the navbar itself (".navbar-nav") to always match exactly one
        # element. ".first" is an extra safety net.
        navbar = page.locator(".navbar-nav")
        self.signup_login_link = navbar.locator('a[href="/login"]').first
        self.products_link = navbar.locator('a[href="/products"]').first
        self.cart_link = navbar.locator('a[href="/view_cart"]').first

        # Shown only after a successful login
        self.logged_in_as_text = page.locator("li:has-text('Logged in as')")
        self.logout_link = page.locator('a[href="/logout"]')
        self.delete_account_link = page.locator('a[href="/delete_account"]')

    def open(self):
        self.page.goto(BASE_URL)
        self.page.wait_for_timeout(4000)

    def is_home_page_visible(self) -> bool:
        """Home page is visible when the title is right and the banner slider shows up."""
        return "Automation Exercise" in self.page.title() and self.slider.is_visible()

    def go_to_signup_login_page(self):
        self.signup_login_link.click()
        self.page.wait_for_timeout(4000)

    def go_to_products_page(self):
        self.products_link.click()
        self.page.wait_for_timeout(4000)

    def is_logged_in_as(self, name: str) -> bool:
        return self.logged_in_as_text.inner_text().strip() == f"Logged in as {name}"

    def click_delete_account(self):
        self.delete_account_link.click()
        self.page.wait_for_timeout(4000)

    def logout(self):
        self.logout_link.click()
        self.page.wait_for_timeout(4000)
