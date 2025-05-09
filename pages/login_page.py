from selenium.webdriver.common.by import By
from .base_page import BasePage
from utils.config import BASE_URL

class LoginPage(BasePage):
    URL = f"{BASE_URL}/login"

    USERNAME_INPUT = (By.ID, "username")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "loginBtn")

    def open(self):
        self.driver.get(self.URL)

    def login(self, username, password):
        self.enter_text(self.USERNAME_INPUT, username)
        self.enter_text(self.PASSWORD_INPUT, password)
        self.click(self.LOGIN_BUTTON)
