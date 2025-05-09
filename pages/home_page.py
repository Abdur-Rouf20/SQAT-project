from selenium.webdriver.common.by import By
from .base_page import BasePage
from utils.config import BASE_URL

class HomePage(BasePage):
    URL = f"{BASE_URL}/home"
    WELCOME_BANNER = (By.CLASS_NAME, "message alert alert-success")

    def open(self):
        self.driver.get(self.URL).maximize_window()

    def is_welcome_banner_displayed(self):
        return self.driver.find_element(*self.WELCOME_BANNER).is_displayed()
