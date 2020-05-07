import unittest
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class ChangeWindow(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('http://www.goodstartbook.com/pruebas/index.html')

    def test_click_alert(self):
        element = self.driver.find_element_by_xpath('//*[@id="center"]/button')
        if element is not None:
            element.click()
        time.sleep(3)

        alert = self.driver.switch_to.alert
        alert.accept()

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()