from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
import time

driver = webdriver.Chrome()
driver.get('https://www.w3schools.com/html/')
time.sleep(7)
content = driver.find_element_by_class_name('.nextprev .w3-right')
content.click()

