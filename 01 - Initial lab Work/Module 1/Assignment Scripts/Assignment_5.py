# Imports
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Launch Browser
driver = webdriver.Edge()
driver.get("https://qaplayground.com/practice/data-table")
driver.maximize_window()

# Find Table
table = driver.find_element(By.XPATH, "//table")
rows = table.find_elements(By.XPATH, ".//tbody/tr")

# Search Row
for row in rows:
    columns = row.find_elements(By.TAG_NAME, "td")
    print([column.text for column in columns])

    if "Clean Code" in [column.text for column in columns]:
        print("Element Found: Clean Code")
        print("Genre:", columns[2].text)
        break

# Sleep Time and Screenshot
time.sleep(5)
driver.save_screenshot("Assignment5_Success.png")
print("Success Screenshot taken")

driver.quit()