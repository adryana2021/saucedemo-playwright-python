import pytest
import allure
from data.users import STANDARD_USER, PASSWORD
from data.products import PRODUCTS_TO_BUY
from data.client_data import CLIENT_DATA
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from config.config import BASE_URL

class TestSauceDemo:

    @pytest.mark.regression
    def test_complete_purchase_multiple_products(self, page):
        #1. Log in with valid credentials
        #2. Add multiple products to the cart
        #3. Open the cart
        #4. Validate the added products are in the cart
        #5. Proceed to Checkout
        #6. Enter First Name, Last Name, and Postal Code
        #7. Continue to Checkout Overview
        #8. Validate the products are still correct
        #9. Finish the purchase
        #10. Validate the order confirmation message
        print("\nTest 2 — Positive — Complete purchase of multiple products")
        login = LoginPage(page)
        inventory = InventoryPage(page)
        cart = CartPage(page)
        checkout = CheckoutPage(page)

        page.goto(BASE_URL)
        with allure.step("Login"):
            login.login(STANDARD_USER, PASSWORD)
        inventory.validate_inventory_title()

        with allure.step("Select products"):
            for product in PRODUCTS_TO_BUY:
                inventory.select_product(product)

        with allure.step("Open the cart"):
            inventory.go_to_shopping_cart()

        #Validate products in Cart
        with allure.step("Validate the added products are in the cart"):
            for product in PRODUCTS_TO_BUY:
                cart.validate_item_in_the_cart(product)

        with allure.step("Proceed to Checkout"):
            cart.go_to_checkout()

        with allure.step("Enter First Name, Last Name, and Postal Code"):
            checkout.complete_checkout_step_one(CLIENT_DATA)

        #Validate products in Checkout step one
        with allure.step("Continue to Checkout Overview and validate the products are still correct"):
            for product in PRODUCTS_TO_BUY:
                cart.validate_item_in_the_cart(product)

        with allure.step("Finish the purchase"):
            checkout.click_on_finish_button()

        with allure.step("Validate the order confirmation message"):
            checkout.validate_success_message()

        page.wait_for_timeout(1000)
