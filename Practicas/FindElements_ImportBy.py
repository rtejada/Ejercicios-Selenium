import unittest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


class MyTestCase(unittest.TestCase):

    def setUp(self):
        options = Options()
        options.add_argument('--headless')
        options.add_argument('--disable-gpu')  # Last I checked this was necessary.

        self.driver = webdriver.Chrome(options=options)
        self.driver.get('http://www.goodstartbook.com/pruebas/index.html')

    def test_xpath(self):
        rows = self.driver.find_elements(By.XPATH, '//tr')
        if rows is not None:
            number_elements = len(rows)
            print('Encontre:',number_elements,'elementos')

    def test_tags(self):
        elements = self.driver.find_elements_by_tag_name('tr')
        if elements is not None:
            number = len(elements)
            print('Encontre:',number,'elementos')


    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
