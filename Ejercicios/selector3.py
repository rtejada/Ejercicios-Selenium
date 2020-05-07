'''3º Contar el nº de cuadrados de la home:'''
import unittest
from selenium import webdriver


class CountRows(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('https://phptravels.com/demo/')

    def test_count_rows(self):
        number_elements = self.driver.find_elements_by_class_name('resource-box')
        if number_elements is not None:
            number_elements = len(number_elements)
            print('Hay:', number_elements, 'elementos')


if __name__ == '__main__':
    unittest.main()
