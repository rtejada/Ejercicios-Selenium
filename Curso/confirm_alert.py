import unittest
from selenium import webdriver
import time


class Confirm_Alert(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_click_alert(self):
        self.driver.get('https://crontab-generator.org/')
        buttom_generate = self.driver.find_element_by_name('Generate')
        buttom_generate.click()
        time.sleep(2)
        buttom_generate = self.driver.switch_to_alert()
        buttom_generate.accept()
        #buttom_generate.dismiss() -- cuando los alert tienen solo un boton se pueden utilizar (accept y dismiss)
        time.sleep(3)

    def tearDown(self):
        self.driver.close()


if __name__ == 'main':
    unittest.main()
