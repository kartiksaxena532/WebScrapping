from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome()
driver.get("https://google.com")
print(driver.title)
element = driver.find_element(By.CSS_SELECTOR, "textarea.gLFyf")
element.send_keys("hi mom"+Keys.RETURN)
time.sleep(10)