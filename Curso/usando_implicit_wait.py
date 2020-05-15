import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import  expected_conditions as EC


class UsingImplicitCondition(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_using_implicit(self):
        self.driver.implicitly_wait(5)
        self.driver.get('http://www.google.com')
        myDynamicElement = self.driver.find_element_by_name('q')
        

if __name__ == '__main__':
    unittest.main()
