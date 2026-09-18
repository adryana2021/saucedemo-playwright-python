import pytest
import allure

from config.config import BASE_URL
from data.users import STANDARD_USER, PASSWORD
from pages.login_page import LoginPage


@pytest.fixture
def login_user(page):
    page.goto(BASE_URL)

    login = LoginPage(page)

    with allure.step("Login"):
        login.login(STANDARD_USER, PASSWORD)