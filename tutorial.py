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
movie=driver.find_element(By.CLASS_NAME, "EKtkFWMYpwzMKOYr0GYm LQVY1Jpkk8nyJ6HBWKAk").click()
movie2=driver.find_element(By.CSS_SELECTOR, "video.jw-video jw-reset").click()

time.sleep(10)