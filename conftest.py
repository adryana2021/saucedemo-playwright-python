import allure
import pytest
from playwright.sync_api import expect

from config.config import (
    EXPECT_TIMEOUT,
    ACTION_TIMEOUT,
    NAVIGATION_TIMEOUT,
)
from data.users import STANDARD_USER, PASSWORD
from pages.login_page import LoginPage


expect.set_options(timeout=EXPECT_TIMEOUT)


@pytest.fixture(autouse=True)
def configure_context(context):
    context.set_default_timeout(ACTION_TIMEOUT)
    context.set_default_navigation_timeout(NAVIGATION_TIMEOUT)


@pytest.fixture
def logged_in_page(page):
    login = LoginPage(page)
    login.goto()

    with allure.step("Login"):
        login.login(STANDARD_USER, PASSWORD)

    return page