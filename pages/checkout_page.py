from playwright.sync_api import Page, expect

class CheckoutPage:
    def __init__(self, page: Page):
        self.first_name = page.locator("[name='firstName']")
        self.last_name = page.locator("[name='lastName']")
        self.postal_code = page.locator("[name='postalCode']")
        self.continue_button = page.locator("input[name='continue']")
        self.finish_button = page.locator("button[name='finish']")
        self.success_msg = page.locator(".complete-header")

    def complete_checkout_step_one(self, client_data):
        self.first_name.fill(client_data["first_name"])
        self.last_name.fill(client_data["last_name"])
        self.postal_code.fill(client_data["postal_code"])
        self.continue_button.click()

    def click_on_finish_button(self):
        self.finish_button.click()

    def validate_success_message(self):
        expect(self.success_msg).to_have_text("Thank you for your order!")
