# Imports
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

# Launch Browser
driver = webdriver.Edge()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()

# Dropdown
dropdown = Select(driver.find_element(By.ID, "dropdown-class-example"))
dropdown.select_by_visible_text("Option2")
print("Dropdown:", dropdown.first_selected_option.text)

# Checkboxes
option1 = driver.find_element(By.ID, "checkBoxOption1")
option1.click()
print("Option1 Selected:", option1.is_selected())

option2 = driver.find_element(By.ID, "checkBoxOption2")
option2.click()
print("Option2 Selected:", option2.is_selected())

# Suggestion Dropdown
suggestion = driver.find_element(By.ID, "autocomplete")
suggestion.send_keys("Ind")

time.sleep(2)
suggestions = driver.find_elements(By.XPATH, '//*[@id="autocomplete"]')

for country in suggestions:
    if country.text.strip() == 'India':
        country.click()
        break

print("Country:", "India")

# Sleep Time and Quit Driver
time.sleep(5)
driver.quit()