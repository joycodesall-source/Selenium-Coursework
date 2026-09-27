# Imports
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Launch Browser
driver = webdriver.Edge()
driver.maximize_window()

# Iframe Task
driver.get("https://practice-automation.com/iframes/")
iframe = driver.find_element(By.TAG_NAME, "iframe")
driver.switch_to.frame(iframe)

get_started = driver.find_element(
    By.XPATH,
    "//*[@id='__docusaurus_skipToContent_fallback']/header/div/div/a"
)
driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", get_started)
time.sleep(1)

get_started.click()
time.sleep(3)
print("Iframe interaction successful")
driver.save_screenshot("Assignment6_Iframe_Success.png")
driver.switch_to.default_content()

# Window and Tab Task
driver.get("https://practice-automation.com/window-operations/")

main_window = driver.current_window_handle

new_tab_button = driver.find_element(
    By.XPATH,
    "//*[@id='post-1147']/div/p[3]/button/b"
)
new_tab_button.click()
time.sleep(3)

for window in driver.window_handles:
    if window != main_window:
        driver.switch_to.window(window)
        break
print("New Tab Title:", driver.title)

# Screenshot
driver.save_screenshot("Assignment6_Window_Success.png")
driver.close()
driver.switch_to.window(main_window)
print("Returned to Main Window")

time.sleep(3)
print("Both tasks completed successfully!")
driver.quit()