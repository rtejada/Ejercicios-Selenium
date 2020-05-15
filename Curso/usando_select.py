import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys


class UsingSelect(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_using_select(self):
        self.driver.get('https://www.w3schools.com/howto/howto_custom_select.asp')
        time.sleep(2)
        selection = self.driver.find_element_by_xpath('//*[@id="main"]/div[3]/div[1]/select')
        options = selection.find_elements_by_tag_name('option')
        time.sleep(3)
        for option in options:
            print('Los valores son: %s' % option.get_attribute('value'))
            option.click()
            time.sleep(2)

        sel = Select(self.driver.find_element_by_xpath('//*[@id="main"]/div[3]/div[1]/select'))
        sel.select_by_value('10')
        time.sleep(2)

    def tearDown(self):
        self.driver.close()


if __name__ == 'main':
    unittest.main()