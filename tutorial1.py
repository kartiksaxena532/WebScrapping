from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome()
driver.get("https://google.com")
WebDriverWait(driver,5).until(
    EC.presence_of_element_located()
)

time.sleep(10)