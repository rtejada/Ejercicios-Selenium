import unittest
from selenium import webdriver
import time

class PromtAlert(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_prompt_alert(self):
        self.driver.get('file:///home/roxana/Documentos/Programas_HTML_CSS/HojasInscripcion.html')
        prompt_alert = self.driver.find_element_by_name('prompt_alert')
        prompt_alert.click()
        time.sleep(3)
        prompt_alert = self.driver.switch_to.alert()
        prompt_alert.accept()
        time.sleep(2)

    def tearDown(self):
        self.driver.close()

if __name__ == 'main':
    unittest.main()


