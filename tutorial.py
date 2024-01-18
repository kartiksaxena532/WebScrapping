from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome()
driver.get("https://google.com")
print(driver.title)
WebDriverWait(driver,5).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, "textarea.gLFyf"))
)
element = driver.find_element(By.CSS_SELECTOR, "textarea.gLFyf")
element.send_keys("hi mom"+Keys.RETURN)
link= driver.find_element(By.PARTIAL_LINK_TEXT, "IMDb")
link.click()
linkRate= driver.find_element(By.LINK_TEXT, "Comedy")
linkRate.click()
time.sleep(10)