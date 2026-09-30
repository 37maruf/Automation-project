from playwright.sync_api import Page


class CartPage:
    """Represents the 'Cart' page (https://www.automationexercise.com/view_cart)."""

    def __init__(self, page: Page):
        self.page = page
        self.cart_rows = page.locator("#cart_info tbody tr")

    def get_number_of_products_in_cart(self) -> int:
        return self.cart_rows.count()

    def is_product_in_cart(self, product_name: str) -> bool:
        return self.cart_rows.filter(has_text=product_name).count() > 0

    # ---------- Read one product's row (found by the product name) ----------

    def _get_row(self, product_name: str):
        return self.cart_rows.filter(has_text=product_name).first

    def get_product_price(self, product_name: str) -> str:
        return self._get_row(product_name).locator(".cart_price p").inner_text().strip()

    def get_product_quantity(self, product_name: str) -> str:
        return self._get_row(product_name).locator(".cart_quantity button").inner_text().strip()

    def get_product_total(self, product_name: str) -> str:
        return self._get_row(product_name).locator(".cart_total_price").inner_text().strip()
