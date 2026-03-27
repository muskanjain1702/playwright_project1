class InventoryPage:
    def __init__(self, page):
        self.page = page

    def add_first_two_products_to_cart(self):
        products = self.page.locator(".inventory_item button")

        # first product
        products.nth(0).click()

        # second product
        products.nth(1).click()

    def go_to_cart(self):
        self.page.click(".shopping_cart_link")