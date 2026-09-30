import pytest
from playwright.sync_api import sync_playwright
from pages.home_page import HomePage
from utils.helpers import generate_unique_email, generate_random_name
from utils.flows import register_new_user


@pytest.fixture
def page():
    """Opens one browser + one tab for each test, and closes it afterwards."""
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        yield page

        browser.close()


@pytest.fixture
def home_page(page):
    """Opens the website and returns the Home Page object, ready to use."""
    home = HomePage(page)
    home.open()
    return home


@pytest.fixture
def registered_user(home_page):

    name = generate_random_name()
    email = generate_unique_email()
    password = "Test@1234"

    register_new_user(home_page, name, email, password)
    home_page.logout()

    return {"name": name, "email": email, "password": password}
