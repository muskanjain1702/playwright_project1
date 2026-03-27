from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage

def test_e2e_flow(page):
    login = LoginPage(page)
    inventory = InventoryPage(page)
    cart = CartPage(page)

    login.load()
    page.wait_for_selector("#user-name")

    login.login("standard_user", "secret_sauce")
    page.wait_for_selector(".inventory_list")

    inventory.add_first_two_products_to_cart()
    page.wait_for_selector(".shopping_cart_badge")

    inventory.go_to_cart()
    page.wait_for_selector("#checkout")

    cart.checkout()
    page.wait_for_selector("#first-name")

    cart.fill_information("Muskan", "Jain", "250110")
    page.wait_for_selector("#finish")

    cart.finish_checkout()
    page.wait_for_timeout(1000)

    assert page.locator("text=Thank you for your order").is_visible()