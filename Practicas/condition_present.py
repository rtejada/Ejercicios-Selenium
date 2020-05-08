import unittest
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TimeWait(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('http://www.goodstartbook.com/pruebas/index.html')
        #self.driver.implicitly_wait(15) #espera 15 segundos antes de enviar error

    def test_wait(self):
        wait = WebDriverWait(self.driver, 10)
        button = wait.until(EC.element_to_be_clickable((By.ID, 'proceed')))
        if button is not None:
            button.click()

        time.sleep(3)
        
    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()