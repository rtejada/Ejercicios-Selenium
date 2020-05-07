import unittest
from selenium import webdriver


class FindByIdName(unittest.TestCase):

    def setUp(self):

        self.driver = webdriver.Chrome()
        self.driver.get('http://www.goodstartbook.com/pruebas/index.html')

    def test_Id(self):
        element = self.driver.find_element_by_id('noImportante')
        if element is not None:
            print('El Elemento ID fue encontrado')

    def test_Name(self):
        element = self.driver.find_element_by_name('ultimo')
        if element is not None:
            print('El Elemento Name fue encontrado')

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
