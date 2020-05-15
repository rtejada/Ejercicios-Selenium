import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait


class UsignRadioButton(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_using_radio_button(self):
        self.driver.get('https://www.w3schools.com/howto/howto_css_custom_checkbox.asp')
        time.sleep(2)
        radio = self.driver.find_element_by_xpath('//*[@id="main"]/div[3]/div[1]/input[4]')
        radio.click()
        time.sleep(2)

        radio = self.driver.find_element_by_xpath('//*[@id="main"]/div[3]/div[1]/input[3]')
        radio.click()
        time.sleep(2)

    def tearDown(self):
        self.driver.close()


if __name__ == 'main':
    unittest.main()

