import unittest
from selenium import webdriver


class FindByIdName(unittest.TestCase):

    def setUp(self):
        global driver
        driver = webdriver.Chrome()
        driver.get('http://www.goodstartbook.com/pruebas/index.html')

    def testIdName(self):
        element = driver.find_element_by_id('noImportante')
        if element is not None:
            print('El Elemento ID fue encontrado')

        element = driver.find_element_by_name('ultimo')
        if element is not None:
            print('El Elemento Name fue encontrado')

    def tearDown(self):
        driver.quit()


if __name__ == '__main__':
    unittest.main()


