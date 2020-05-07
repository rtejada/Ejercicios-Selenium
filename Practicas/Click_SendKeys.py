'''muestra dos conceptos:
click en boton que lleva a una 2da pagina, en la 2da pagina bucar algo en el text box'''
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class ClickSendKeys(unittest.TestCase):

    def setUp(self):

        self.driver = webdriver.Chrome()
        self.driver.get('http://www.goodstartbook.com/pruebas/index.html')

    def test_click_button(self):
        button = self.driver.find_element(By.XPATH, "//a[contains(text(),'Pagina 2')]") #donde contenga el texto Pagina2
        if button is not None:
            button.click()

        insert_name = self.driver.find_element_by_id('Segundo')
        if insert_name is not None:
            insert_name.send_keys('Roxana')

        time.sleep(5)

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()

