import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


BASE_URL = "https://www.saucedemo.com/"


@pytest.fixture
def driver():
    """Start a fresh Chrome session for each test and always close it."""
    options = Options()
    options.add_argument("--start-maximized")
    browser = webdriver.Chrome(options=options)  # Selenium Manager handles the driver.
    browser.implicitly_wait(0)  # We use explicit waits in page objects instead.
    yield browser
    browser.quit()


@pytest.fixture
def base_url():
    return BASE_URL
