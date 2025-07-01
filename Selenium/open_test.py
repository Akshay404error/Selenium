import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome()
driver.get("https://quotes.toscrape.com/page/2/")
print("Page title:", driver.title)
time.sleep(20)  # Wait for 2 seconds to let the page load
driver.quit()
print("Test completed successfully.")