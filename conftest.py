import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pages.login_page import LoginPage
from utils.config import BASE_URL, USERNAME, PASSWORD

@pytest.fixture(scope="function")
def browser():
    """Initialize WebDriver"""
    options = Options()
    options.add_argument("--headless")  # Optional: run in background
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(10)
    yield driver
    driver.quit()

@pytest.fixture(scope="function")
def logged_in_browser(browser):
    """Login before each test using LoginPage POM"""
    login_page = LoginPage(browser)
    login_page.open()
    login_page.login(USERNAME, PASSWORD)
    return browser
