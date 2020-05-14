import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class UsingUnittest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('http://www.google.com')

    def test_search_by_xpath(self):
        search_xpath = self.driver.find_element_by_xpath("//*[@name='q']")
        time.sleep(3)
        search_xpath.send_keys("Selenium", Keys.ARROW_DOWN)
        time.sleep(3)

    def tearDown(self):
        self.driver.close()


if __name__ == '__main':
    unittest.main()




    '''xpath es una estructura de objetos
    busquedas relativo: el mas usado porque el codigo esta siempre cambiandose
    busquedas absoluta: busca la ubicacion exacta'''

