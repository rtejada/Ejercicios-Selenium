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
        element = self.driver.find_element_by_tag_name('h3')
        if element is not None:
            print('Encontramos el elemento con tag Name')

    def test_partial_text(self):
        element = self.driver.find_element_by_css_selector('#primera')
        if element is not None:
            print('Encontamos el elemento usando css selector')

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
