import unittest
from selenium import webdriver


class FindByIdName(unittest.TestCase):

    def setUp(self):

        self.driver = webdriver.Chrome()
        self.driver.get('http://www.goodstartbook.com/pruebas/index.html')

    def test_link_test(self):
        element = self.driver.find_element_by_link_text('Pagina 2')
        if element is not None:
            print('Encontramos el elemento con texto Pagina 2')

    def test_partial_text(self):
        element = self.driver.find_element_by_partial_link_text('agina')
        if element is not None:
            print('Encontamos el elemento usando texto parcial')

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
