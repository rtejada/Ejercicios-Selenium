import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class DisplayElement(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_display(self):
        self.driver.get('https://www.google.com')
        display = self.driver.find_element_by_name('btnI')
        time.sleep(4)
        print(display.is_displayed()) #Si carga el elemento revuelve un buleano True o False
        print(display.is_enabled()) #Si el elemento esta disponible devuelve True o False
