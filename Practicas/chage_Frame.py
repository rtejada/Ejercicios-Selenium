import unittest
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class ChangeFrame(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('http://www.goodstartbook.com/pruebas/index.html')

    def test_click_alert(self):
        iframe = self.driver.find_element_by_id('pruebas-iframe')
        if iframe is not None:
            self.driver.switch_to.frame(iframe)
        nom = self.driver.find_element_by_id('Segundo')
        if nom is not None:
            nom.send_keys('Juan')

        time.sleep(3)

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
