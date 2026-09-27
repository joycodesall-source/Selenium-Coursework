# Imports
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Browser Fixture
@pytest.fixture
def driver():
    driver = webdriver.Edge()
    driver.maximize_window()
    yield driver
    driver.quit()

# Login Test
def test_login(driver):

    # Open Website
    driver.get("https://www.saucedemo.com/")

    # Login
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.NAME, "password").send_keys("secret_sauce")
    driver.find_element(By.XPATH, "//input[@id='login-button']").click()

    # Validation and Screenshot
    time.sleep(3)
    assert "/inventory.html" in driver.current_url