"""
Test Case 4: Add Products in Cart
Steps:
1. Launch browser
2. Navigate to url 'http://automationexercise.com'
3. Verify that home page is visible successfully
4. Click 'Products' button
5. Hover over first product and click 'Add to cart'
6. Click 'Continue Shopping' button
7. Hover over second product and click 'Add to cart'
8. Click 'View Cart' button
9. Verify both products are added to Cart
10. Verify their prices, quantity and total price
"""
from pages.products_page import ProductsPage
from pages.cart_page import CartPage
from utils.helpers import extract_price_number


def test_add_products_to_cart(home_page):
    # Steps 1 & 2 (launch browser + open the website) are done by the 'home_page' fixture
    page = home_page.page

    # Step 3: verify home page is visible
    assert home_page.is_home_page_visible()
    print("Home page is visible")

    # Step 4: click 'Products'
    home_page.go_to_products_page()
    products_page = ProductsPage(page)

    # Save the name and price of the first two products
    # (index 0 = first product, index 1 = second product),
    # so we can compare them with the Cart page later.
    first_name = products_page.get_product_name_by_index(0)
    first_price = extract_price_number(products_page.get_product_price_by_index(0))
    second_name = products_page.get_product_name_by_index(1)
    second_price = extract_price_number(products_page.get_product_price_by_index(1))

    # Step 5: hover over first product and click 'Add to cart'
    products_page.add_product_to_cart_by_index(0)

    # Step 6: click 'Continue Shopping'
    products_page.close_add_to_cart_popup()

    # Step 7: hover over second product and click 'Add to cart'
    products_page.add_product_to_cart_by_index(1)

    # Step 8: click 'View Cart'
    products_page.go_to_cart_from_popup()
    assert page.url == "https://www.automationexercise.com/view_cart"

    # Step 9: verify both products are in the cart
    cart_page = CartPage(page)
    assert cart_page.get_number_of_products_in_cart() == 2
    assert cart_page.is_product_in_cart(first_name)
    assert cart_page.is_product_in_cart(second_name)
    print(f"Both products are in the cart: '{first_name}' and '{second_name}'")

    # Step 10: verify price, quantity and total of each product
    for product_name, expected_price in [(first_name, first_price), (second_name, second_price)]:
        cart_price = extract_price_number(cart_page.get_product_price(product_name))
        cart_quantity = int(cart_page.get_product_quantity(product_name))
        cart_total = extract_price_number(cart_page.get_product_total(product_name))

        assert cart_price == expected_price          # same price as on Products page
        assert cart_quantity == 1                    # we added it only once
        assert cart_total == cart_price * cart_quantity   # total = price x quantity
        print(f"{product_name}: price={cart_price}, quantity={cart_quantity}, total={cart_total}")
