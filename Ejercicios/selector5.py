'''1º Contar el número de productos que hay en la home.'''
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class CountElementsHome(unittest.TestCase):

    def setUp(self) -> None:
        options = Options()
        options.add_argument('--headless')
        options.add_argument('--disable-gpu')
        self.driver = webdriver.Chrome(options=options)
        self.driver.get('http://automationpractice.com/index.php')

    def test_count(self):
        number_elements = self.driver.find_elements_by_xpath("//ul[@id ='homefeatured']/li//a/img")
        if number_elements is not None:
            number_elements = len(number_elements)
            print('Hay:', number_elements, 'elementos')


if __name__ == '__main__':
    unittest.main()
