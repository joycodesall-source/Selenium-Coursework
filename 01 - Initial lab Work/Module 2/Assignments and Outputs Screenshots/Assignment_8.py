# Imports
from selenium import webdriver
from selenium.webdriver.common.by import By
import csv
import os
import time

# Launch Browser
driver = webdriver.Edge()
driver.maximize_window()

# Read Test Data
file_path = os.path.join(os.path.dirname(__file__), "Assignment_8.csv")
with open(file_path, newline="") as file:
    data = csv.DictReader(file)
    for row in data:

        # Open Website
        driver.get("https://www.saucedemo.com/")

        # Login
        driver.find_element(By.ID, "user-name").send_keys(row["username"])
        driver.find_element(By.NAME, "password").send_keys(row["password"])
        driver.find_element(By.XPATH, "//input[@id='login-button']").click()

        # Validation
        if row["expected"] == "success":
            assert "/inventory.html" in driver.current_url
            print(row["username"], "- Login successful")

        else:
            error_message = driver.find_element(By.CSS_SELECTOR, "[data-test='error']")
            assert error_message.is_displayed()
            print(row["username"], "- Validation error displayed")

# Quit Driver
time.sleep(5)
driver.quit()