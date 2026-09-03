from data.users import STANDARD_USER, PASSWORD, INVALID_USER, INVALID_PASSWORD
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from config.config import BASE_URL

class TestSauceDemo:

    def test_login_valid_credentials(self, page):
        print("\nTest 1 — Positive — valid credentials")
        login = LoginPage(page)
        inventory = InventoryPage(page)
        page.goto(BASE_URL)
        login.login(STANDARD_USER, PASSWORD)
        inventory.validate_inventory_title()

    def test_login_invalid_credentials(self, page):
            print("\nTest 2 — Negative — invalid credentials")
            login = LoginPage(page)
            page.goto(BASE_URL)
            login.login(INVALID_USER, INVALID_PASSWORD)
            login.validate_invalid_credentials_message()
