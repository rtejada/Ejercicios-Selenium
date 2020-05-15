import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

pal_search = 'sele'
driver = webdriver.Chrome
driver.get('https://google.com')
time.sleep(5)
