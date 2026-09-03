from playwright.sync_api import Page, expect

class InventoryPage:
    def __init__(self, page: Page):
        self.page = page
        self.inventory_title = page.locator(".title")

    def validate_inventory_title(self):
        expect(self.inventory_title).to_have_text("Products")