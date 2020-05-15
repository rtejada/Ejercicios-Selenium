import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

#boton off - on


class UsingToggleSwincht(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_using_toggle_swicht(self):
        self.driver.get('https://www.w3schools.com/howto/howto_css_switch.asp')
        time.sleep(3)
        toogle = self.driver.find_element_by_xpath('//*[@id="main"]/label[3]/div')
        toogle.click()
        time.sleep(2)
        toogle.click()
        time.sleep(3)

    def tearDown(self):
        self.driver.close()


if __name__ == 'main':
    unittest.main()


