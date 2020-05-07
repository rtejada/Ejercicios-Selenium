import unittest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class MyTestCase(unittest.TestCase):

    def setUp(self):

        options = Options()
        options.add_argument('--headless')
        options.add_argument('--disable-gpu')  # Last I checked this was necessary.

        self.driver = webdriver.Chrome(options=options)
        self.driver.get('http://www.goodstartbook.com/pruebas/index.html')

    def test_link_test(self):
        elements = self.driver.find_elements_by_tag_name('p')
        if elements is not None:
            for element in elements:
                print(element.size)
                print('Encontramos el elemento con tag Pagina 2')

    def test_partial_text(self):
        element = self.driver.find_element_by_partial_link_text('agina')
        if element is not None:
            print('Encontamos el elemento usando texto parcial')

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
