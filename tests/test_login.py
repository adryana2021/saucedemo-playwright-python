import pytest

from data.users import LOGIN_NEGATIVE_CASES
from pages.login_page import LoginPage
from config.config import BASE_URL


class TestLogin:

    @pytest.mark.regression
    @pytest.mark.parametrize("username, password, expected_message", LOGIN_NEGATIVE_CASES)
    def test_login_invalid_credentials(self, page, username, password, expected_message):
        print(f"\nNegative login test with user: {username}")

        login = LoginPage(page)

        page.goto(BASE_URL)
        login.login(username, password)
        login.validate_login_error_message(expected_message)