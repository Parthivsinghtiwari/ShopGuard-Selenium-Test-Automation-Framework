from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage


def test_valid_login_opens_products_page(driver, base_url):
    login_page = LoginPage(driver).open(base_url)
    login_page.login("standard_user", "secret_sauce")

    inventory_page = InventoryPage(driver).wait_until_loaded()
    assert inventory_page.title() == "Products"
    assert "inventory.html" in driver.current_url


def test_invalid_password_shows_error(driver, base_url):
    login_page = LoginPage(driver).open(base_url)
    login_page.login("standard_user", "wrong_password")

    assert "Username and password do not match" in login_page.error_text()


def test_locked_out_user_cannot_login(driver, base_url):
    login_page = LoginPage(driver).open(base_url)
    login_page.login("locked_out_user", "secret_sauce")

    assert "locked out" in login_page.error_text().lower()
