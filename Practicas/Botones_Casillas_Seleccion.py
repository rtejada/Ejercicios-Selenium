'''click en botones de seleccion y casillas de seleccion'''
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time



class CheckBox(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('http://www.goodstartbook.com/pruebas/index.html')

    def test_click_radio(self):
        print('Radio Buttons')
        button1 = self.driver.find_element_by_id('RadioGroup1_0')
        if button1 is not None:
            button1.click()
        time.sleep(5)

        button2 = self.driver.find_element_by_id('RadioGroup1_1')
        if button2 is not None:
            button2.click()
        time.sleep(5)

    def test_click_checks_box(self):
        print('Check Box')
        check1 = self.driver.find_element_by_id('CheckboxGroup1_0')
        if check1 is not None:
            check1.click()
        time.sleep(5)

        check2 = self.driver.find_element_by_id('CheckboxGroup1_1')
        if check2 is not None:
            check2.click()
        time.sleep(5)

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
