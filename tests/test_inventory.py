from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage


def test_products_are_displayed(driver, base_url):
    LoginPage(driver).open(base_url).login("standard_user", "secret_sauce")
    inventory_page = InventoryPage(driver).wait_until_loaded()

    assert inventory_page.product_count() > 0


def test_adding_backpack_updates_cart_badge(driver, base_url):
    LoginPage(driver).open(base_url).login("standard_user", "secret_sauce")
    inventory_page = InventoryPage(driver).wait_until_loaded()
    inventory_page.add_backpack_to_cart()

    assert inventory_page.cart_count() == "1"
