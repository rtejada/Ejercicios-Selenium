import unittest
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver import ActionChains


class ImplicitlyWait(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('http://www.goodstartbook.com/pruebas/index.html')
        self.driver.implicitly_wait(15) #espera 15 segundos antes de enviar error

    def test_refresh_Button(self):
        button = self.driver.find_element_by_id('proceed')
        if button is not None:
            button.click()

        time.sleep(3)
        #devuelve error, porque el elemento esta escondido y la solucion es con la espera explicita

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()