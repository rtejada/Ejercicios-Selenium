'''2º Seleccionar el Login'''
import unittest
from selenium import webdriver


class MyTestTwo(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('https://phptravels.com/demo/')

    def test_selector(self):
        element = self.driver.find_element_by_xpath('//*[@id="main-menu"]/ul/li[7]/a')
        if element is not None:
            print('Casilla Login encontrador')


if __name__ == '__main__':
    unittest.main()
