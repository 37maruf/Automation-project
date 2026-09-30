"""
Test Case 5: Search Product
Steps:
1. Launch browser
2. Navigate to url 'http://automationexercise.com'
3. Verify that home page is visible successfully
4. Click on 'Products' button
5. Verify user is navigated to ALL PRODUCTS page successfully
6. Enter product name in search input and click search button
7. Verify 'SEARCHED PRODUCTS' is visible
8. Verify all the products related to search are visible
"""
from pages.products_page import ProductsPage

SEARCH_TEXT = "Blue Top"


def test_search_product(home_page):
    # Steps 1 & 2 (launch browser + open the website) are done by the 'home_page' fixture
    page = home_page.page

    # Step 3: verify home page is visible
    assert home_page.is_home_page_visible()
    print("Home page is visible")

    # Step 4: click 'Products'
    home_page.go_to_products_page()

    # Step 5: verify we are on the ALL PRODUCTS page
    # (get_heading_text() gives lowercase text, because the site uses CSS to show it in uppercase)
    products_page = ProductsPage(page)
    assert page.url == "https://www.automationexercise.com/products"
    assert "all products" in products_page.get_heading_text()
    print("ALL PRODUCTS page is visible")

    # Step 6: enter product name and click search (reusable function)
    products_page.search_product(SEARCH_TEXT)

    # Step 7: verify 'SEARCHED PRODUCTS' is visible
    assert "searched products" in products_page.get_heading_text()
    print("'SEARCHED PRODUCTS' is visible")

    # Step 8: verify all the results are related to the search
    assert products_page.get_number_of_results() > 0
    for product_name in products_page.get_all_product_names():
        assert SEARCH_TEXT.lower() in product_name.lower()
        print(f"Found related product: {product_name}")
