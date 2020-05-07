import unittest
from selenium import webdriver


class FindByIdName(unittest.TestCase):

    def setUp(self):

        self.driver = webdriver.Chrome()
        self.driver.get('http://www.goodstartbook.com/pruebas/index.html')

    def test_xpath(self):
        element = self.driver.find_element_by_xpath('//tr[@id="noImportante"]') #busca el id noImportante dentro de tr
        if element is not None:
            print('Encontramos el elemento Xpath')

    def test_Class_Name(self):
        element = self.driver.find_element_by_class_name('rojo')
        if element is not None:
            print('Encontamos el elemento clase name = rojo')

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
