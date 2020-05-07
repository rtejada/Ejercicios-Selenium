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

    def test_element_Xpath(self):
        element = self.driver.find_element(By.XPATH, '//*[@id="noImportante"]')
        if element is not None:
           print('Encontramos el elemento usando XPATH')
            
    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
