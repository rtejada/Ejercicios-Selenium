from selenium import webdriver
from selenium.webdriver import ActionChains
import unittest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


class ActionHover(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_activion_hover(self):
        self.driver.get('https://google.com')
        time.sleep(2)
        element = self.driver.find_element_by_link_text('Privacidad')
        hover = ActionChains(self.driver).move_to_element(element)
        time.sleep(2)
        hover.perform()
        time.sleep(2)

    def tearDown(self):
        self.driver.close()


if __name__ == 'main':
    unittest.main()


