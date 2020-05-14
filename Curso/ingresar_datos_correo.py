from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()

driver.get('https://gmail.com')
user = driver.find_element_by_id('identifierId')
user.send_keys('rtejadasilva@gmail.com')
user.send_keys(Keys.ENTER)
time.sleep(2)

clave = driver.find_element_by_name('password')
clave.send_keys('')
clave.send_keys(Keys.ENTER)
time.sleep(1)
driver.quit()
