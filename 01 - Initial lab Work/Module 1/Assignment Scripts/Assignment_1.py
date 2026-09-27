#Imports
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

#Website Automation
driver = webdriver.Edge()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()

# ID
country = driver.find_element(By.ID, "autocomplete")
country.send_keys("Indonesia")
print("ID :", country.get_attribute("value"))

# NAME
name = driver.find_element(By.NAME, "enter-name")
name.send_keys("John")
print("NAME:", name.get_attribute("value"))

# TAG NAME
inputs = driver.find_element(By.TAG_NAME, "input")
print("TAG NAME:",inputs)

# LINK TEXT
home = driver.find_element(By.LINK_TEXT, "Home")
print("LINK URL:", home.get_attribute("href"))

# PARTIAL LINK TEXT
partial_link = driver.find_element(By.PARTIAL_LINK_TEXT, "Ho")
print("PARTIAL LINK URL:", partial_link.get_attribute("href"))

# CLASS NAME
class_element = driver.find_element(By.CLASS_NAME, "inputs")
print("CLASS NAME:", class_element.get_attribute("class"))

# CSS SELECTOR
css_element = driver.find_element(By.CSS_SELECTOR, "#name")
print("CSS SELECTOR - Value:", css_element.get_attribute("value"))

# XPATH
xpath_element = driver.find_element(By.XPATH, "//input[@id='name']")
print("XPATH - Value:", xpath_element.get_attribute("value"))

#Sleep time to check Automation and then Quit Driver
time.sleep(5)
driver.quit()