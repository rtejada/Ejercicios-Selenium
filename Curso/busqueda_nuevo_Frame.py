import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


class BuscarFrameGoogle(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_busca_frame(self):
        self.driver.get('https://www.google.com/')
        time.sleep(2)
        aplicaciones = self.driver.find_element_by_id("gbwa")
        time.sleep(2)
        aplicaciones.click()
        time.sleep(2)
        self.driver.switch_to.frame(self.driver.find_element_by_xpath('/html/body/div/div[2]/div[2]/div/div/div[3]/iframe'))
        time.sleep(3)
        abre_apli = self.driver.find_element_by_id("yDmH0d")
        time.sleep(2)
        abre_apli.click()
        time.sleep(3)

    def tearDown(self):
        self.driver.close()



if __name__ == '__main__':
    unittest.main()
