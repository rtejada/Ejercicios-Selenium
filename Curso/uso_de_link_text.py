import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


class HiperlinksText(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_hiperlinks(self):
        self.driver.get('https://www.w3schools.com/')
        time.sleep(2)
        find_link = self.driver.find_element_by_link_text('Learn CSS')
        find_link.click()
        time.sleep(2)

    def tearDown(self):
        self.driver.close()


if __name__ == 'main':
    unittest.main()
