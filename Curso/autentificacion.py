from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

url = "http://roxana@roxana:217.182.87.241/testlink/login.php"
driver = webdriver.Chrome()
driver.get(url)
time.sleep(5)
