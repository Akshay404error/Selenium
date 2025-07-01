import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome()
driver.get("https://www.google.com")
print("Page title:", driver.title)
#serach box locating
search_box = driver.find_element(By.NAME, "q")
search_box.send_keys("https://www.saucedemo.com/")
search_box.send_keys(u'\ue007')  # Press Enter key
time.sleep(5)  # Wait for 20 seconds to let the page load
print("Search completed successfully.")
frist_result = driver.find_element(By.XPATH, "(//h3)[1]")
frist_result.click()

time.sleep(5)  # Wait for 5 seconds to let the page load
driver.quit()
print("Test completed successfully.")