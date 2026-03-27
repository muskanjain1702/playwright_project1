class CartPage:
    def __init__(self, page):
        self.page = page

    def checkout(self):
        self.page.click("#checkout")

    def fill_information(self, first_name, last_name, zip_code):
        self.page.fill("#first-name", first_name)
        self.page.fill("#last-name", last_name)
        self.page.fill("#postal-code", zip_code)
        self.page.click("#continue")

    def finish_checkout(self):
        self.page.click("#finish")    