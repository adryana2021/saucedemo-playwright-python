from playwright.sync_api import Page, expect

class InventoryPage:
    def __init__(self, page: Page):
        self.page = page
        self.inventory_title = page.locator(".title")
        self.products = page.locator(".inventory_item")
        self.shopping_cart_link = page.locator("a.shopping_cart_link")       

    def validate_inventory_title(self):
        expect(self.inventory_title).to_have_text("Products")

    def select_product(self, product):
        print(f"Selecting product: {product}")
        product = self.products.filter(has_text=product)
        product.locator(".inventory_item_description > div.pricebar >button").click()

    def go_to_shopping_cart(self):
        self.shopping_cart_link.click()