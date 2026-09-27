from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Edge()

driver.get("https://www.selenium.dev/selenium/web/dynamic.html")
driver.maximize_window()

wait = WebDriverWait(driver, 10)

# Explicit Wait
driver.find_element(By.ID, "reveal").click()

text_element = wait.until(
    EC.visibility_of_element_located((By.ID, "revealed"))
)
text_element.send_keys("Displayed")

print("Text:", text_element.get_attribute("value"))

assert text_element.is_displayed()
driver.quit()