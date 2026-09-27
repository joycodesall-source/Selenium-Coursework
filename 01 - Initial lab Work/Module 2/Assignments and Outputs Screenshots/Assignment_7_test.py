# Imports
from selenium import webdriver
from Assignment_7_login import LoginPage
import time

# Launch Browser
driver = webdriver.Edge()
driver.maximize_window()

# Open Website
driver.get("https://www.saucedemo.com/")

# Login
login_page = LoginPage(driver)
login_page.enter_username("standard_user")
login_page.enter_password("secret_sauce")
login_page.click_login()

# Validation
assert "/inventory.html" in driver.current_url
print("Login successful")
time.sleep(3)
driver.save_screenshot("Assignment7_Success.png")
driver.quit()