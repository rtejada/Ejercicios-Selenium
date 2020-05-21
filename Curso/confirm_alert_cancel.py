import unittest
from selenium import webdriver
import time


class ConfirmAlert(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_confirm_alert_Cancel(self):
        self.driver.get('file:///home/roxana/Documentos/Programas_HTML_CSS/HojasInscripcion.html')
        time.sleep(2)
        confirm = self.driver.find_element_by_name('confirm_alert')
        confirm.click()
        time.sleep(2)
        confirm = self.driver.switch_to.alert()
        confirm.dismiss()
        time.sleep(2)

    def tearDown(self):
        self.driver.close()


if __name__ == 'main':
    unittest.main()