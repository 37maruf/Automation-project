from playwright.sync_api import Page


class ProductsPage:
    """Represents the 'All Products' page (https://www.automationexercise.com/products)."""

    def __init__(self, page: Page):
        self.page = page

        # Heading shows 'All Products' first, then 'Searched Products' after a search
        self.page_heading = page.locator("h2.title").first
        self.search_input = page.locator("#search_product")
        self.search_button = page.locator("#submit_search")

        # Every product card, and the name inside each card
        self.product_items = page.locator(".features_items .product-image-wrapper")
        self.product_names = page.locator(".features_items .productinfo p")

        # Popup that appears right after clicking "Add to cart"
        # NOTE: "a[href='/view_cart']" also matches the navbar's Cart icon,
        # so we scope this locator to just the popup itself (#cartModal).
        self.continue_shopping_button = page.locator("button:has-text('Continue Shopping')")
        self.view_cart_link_in_popup = page.locator("#cartModal a[href='/view_cart']")

    # ---------- Search ----------

    def search_product(self, product_name: str):
        """Types a product name in the search box and clicks the search icon."""
        self.search_input.fill(product_name)
        self.search_button.click()
        self.page.wait_for_timeout(4000)

    def get_heading_text(self) -> str:
        # NOTE: the site shows headings in uppercase using CSS, so we return
        # lowercase text. Tests can compare without worrying about uppercase.
        return self.page_heading.inner_text().strip().lower()

    def get_number_of_results(self) -> int:
        return self.product_items.count()

    def get_all_product_names(self) -> list:
        """Returns the names of all products currently shown on the page."""
        return [name.strip() for name in self.product_names.all_inner_texts()]

    # ---------- Product details (by position, first product = 0) ----------

    def get_product_name_by_index(self, index: int) -> str:
        return self.product_items.nth(index).locator(".productinfo p").inner_text().strip()

    def get_product_price_by_index(self, index: int) -> str:
        return self.product_items.nth(index).locator(".productinfo h2").inner_text().strip()

    # ---------- Add to cart ----------

    def add_product_to_cart_by_index(self, index: int = 0):
        """
        Hovers over a product card (by position, first = 0) and clicks
        its 'Add to cart' button. A popup shows up afterwards.
        """
        product_card = self.product_items.nth(index)
        product_card.hover()
        product_card.locator("a:has-text('Add to cart')").first.click()
        self.page.wait_for_timeout(1500)

    def close_add_to_cart_popup(self):
        """Clicks 'Continue Shopping' in the popup."""
        self.continue_shopping_button.click()
        self.page.wait_for_timeout(1000)

    def go_to_cart_from_popup(self):
        """Clicks 'View Cart' in the popup."""
        self.view_cart_link_in_popup.click()
        self.page.wait_for_timeout(4000)
