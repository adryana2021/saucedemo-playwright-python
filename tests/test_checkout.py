import pytest
import allure
from data.products import PRODUCTS_TO_BUY
from data.client_data import CLIENT_DATA
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage

class TestCheckout:

    @pytest.mark.regression
    @allure.title("Complete purchase of multiple products")
    def test_complete_purchase_multiple_products(self, logged_in_page):
        page = logged_in_page

        inventory = InventoryPage(page)
        cart = CartPage(page)
        checkout = CheckoutPage(page)

        inventory.validate_inventory_title()

        with allure.step("Select products"):
            for product in PRODUCTS_TO_BUY:
                inventory.select_product(product)

        with allure.step("Open the cart"):
            inventory.go_to_shopping_cart()

        with allure.step("Validate the added products are in the cart"):
            for product in PRODUCTS_TO_BUY:
                cart.validate_item_in_the_cart(product)

        with allure.step("Proceed to Checkout"):
            cart.go_to_checkout()

        with allure.step("Enter First Name, Last Name, and Postal Code"):
            checkout.complete_checkout_step_one(CLIENT_DATA)

        with allure.step("Continue to Checkout Overview and validate the products are still correct"):
            for product in PRODUCTS_TO_BUY:
                cart.validate_item_in_the_cart(product)

        with allure.step("Finish the purchase"):
            checkout.click_on_finish_button()

        with allure.step("Validate the order confirmation message"):
            checkout.validate_success_message()

        page.wait_for_timeout(1000)
