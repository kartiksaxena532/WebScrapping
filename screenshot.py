from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
driver = webdriver.Chrome()
driver.get('http://kartikdesign.netlify.app/')
driver.save_screenshot('screenshot.png')
driver.quit()