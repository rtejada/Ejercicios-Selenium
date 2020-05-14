'''da condiciones de espera a que cargue el componente buscado'''

import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class UsingExplicitWait(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_explicit_wait(self):
        self.driver.get('http://www.google.com')

        try:
            element = WebDriverWait(self.driver, 3).until(EC.presence_of_element_located((By.NAME, "p")))

            if element is not None:
                element.click()

        except:

            print("No existe tag culo")

        finally:

            element = WebDriverWait(self.driver, 3).until(EC.presence_of_element_located((By.NAME, "q")))

            if element is not None:
                element.click()

    def tearDown(self):
        self.driver.close()


if __name__ == 'main':
    unittest.main()




