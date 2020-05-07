''' 1º Seleccionar el botón demo: '''

import unittest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class MyTestOne(unittest.TestCase):
    def setUp(self):
        options = Options()
        options.add_argument('--headless')
        options.add_argument('--disable-gpu')
        self.driver = webdriver.Chrome(options=options)
        self.driver.get('https://phptravels.com/demo/')

    def test_selector(self):
        element = self.driver.find_element_by_xpath('//*[@id="Main"]/section[1]/div/div/div[2]/div/div[2]/a')
        if element is not None:
            print('Encontramos el elemento')


if __name__ == '__main__':
    unittest.main()
