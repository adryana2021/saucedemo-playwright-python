from playwright.sync_api import Page, expect

class CartPage:
    def __init__(self, page: Page):
        self.page = page
        self.items = page.locator(".inventory_item_name")
        self.checkout_button = page.locator("button#checkout")

    def validate_item_in_the_cart(self, item):
        expect(self.items.filter(has_text=item)).to_be_visible()

    def go_to_checkout(self):
        self.checkout_button.click()