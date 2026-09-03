from data.users import STANDARD_USER, PASSWORD
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from config.config import BASE_URL

class TestSauceDemo:

    def test_login(self, page):
        login = LoginPage(page)
        inventory = InventoryPage(page)

        page.goto(BASE_URL)
        login.login(STANDARD_USER, PASSWORD)
        inventory.validate_inventory_title()

        
        page.wait_for_timeout(2000)
