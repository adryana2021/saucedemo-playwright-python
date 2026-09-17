import pytest

from data.users import INVALID_USER, INVALID_PASSWORD
from pages.login_page import LoginPage
from config.config import BASE_URL

class TestSauceDemo:
    
    @pytest.mark.regression
    def test_login_invalid_credentials(self, page):
        print("\nTest 1 — Negative — invalid credentials")
        login = LoginPage(page)
        page.goto(BASE_URL)
        login.login(INVALID_USER, INVALID_PASSWORD)
        login.validate_invalid_credentials_message()
