# Imports
from selenium.webdriver.common.by import By


class LoginPage:

    def __init__(self, driver):
        self.driver = driver

    def open_login_page(self):
        self.driver.get("https://www.saucedemo.com/")

    def enter_username(self, username):
        self.driver.find_element(By.ID, "user-name").send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(By.NAME, "password").send_keys(password)

    def click_login(self):
        self.driver.find_element(
            By.XPATH, "//input[@id='login-button']"
        ).click()

    def is_login_successful(self):
        return "/inventory.html" in self.driver.current_url

    def is_error_displayed(self):
        return self.driver.find_element(
            By.CSS_SELECTOR, "[data-test='error']"
        ).is_displayed()