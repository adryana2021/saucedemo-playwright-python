from playwright.sync_api import Page, expect

from config.config import BASE_URL


class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        self.username_input = page.locator("#user-name")
        self.password_input = page.locator("#password")
        self.login_button = page.locator("#login-button")
        self.login_error_message = page.locator('[data-test="error"]')

    def goto(self):
        self.page.goto(BASE_URL)

    def login(self, username, password):
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_button.click()

    def validate_login_error_message(self, expected_message):
        expect(self.login_error_message).to_contain_text(expected_message)