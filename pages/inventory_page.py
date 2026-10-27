from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class InventoryPage:
    """Page checks and actions for the product inventory page."""

    TITLE = (By.CSS_SELECTOR, ".title")
    INVENTORY_ITEMS = (By.CSS_SELECTOR, ".inventory_item")
    ADD_BACKPACK_BUTTON = (By.ID, "add-to-cart-sauce-labs-backpack")
    CART_BADGE = (By.CSS_SELECTOR, ".shopping_cart_badge")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def wait_until_loaded(self):
        self.wait.until(EC.visibility_of_element_located(self.TITLE))
        return self

    def title(self):
        return self.driver.find_element(*self.TITLE).text

    def product_count(self):
        self.wait.until(EC.visibility_of_all_elements_located(self.INVENTORY_ITEMS))
        return len(self.driver.find_elements(*self.INVENTORY_ITEMS))

    def add_backpack_to_cart(self):
        self.wait.until(
            EC.element_to_be_clickable(self.ADD_BACKPACK_BUTTON)
        ).click()

    def cart_count(self):
        return self.wait.until(
            EC.visibility_of_element_located(self.CART_BADGE)
        ).text
