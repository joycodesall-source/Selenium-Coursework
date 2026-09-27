# Imports
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Launch Browser
driver = webdriver.Edge()
driver.get("https://the-internet.herokuapp.com/javascript_alerts")
driver.maximize_window()

# Alert
driver.find_element(By.XPATH, '//*[@id="content"]/div/ul/li[1]/button').click()
alert = driver.switch_to.alert
print("Alert:", alert.text)
alert.accept()

# Confirm
driver.find_element(By.XPATH, '//*[@id="content"]/div/ul/li[2]/button').click()
alert = driver.switch_to.alert
print("Confirm:", alert.text)
alert.dismiss()

# Prompt
driver.find_element(By.XPATH, '//*[@id="content"]/div/ul/li[3]/button').click()
alert = driver.switch_to.alert
print("Prompt:", alert.text)
alert.send_keys("John")
alert.accept()

# Sleep Time and Screenshot
time.sleep(5)
driver.save_screenshot("Assignment4_Success.png")
print("Success Screenshot taken")
driver.quit()