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

    def test_implicit_wait(self):
        button_menu = self.driver.find_element_by_class_name('dropbtnx')
        if button_menu is not None:
            action = ActionChains(self.driver)
            action.move_to_element(button_menu).perform()

            access_click = self.driver.find_element_by_link_text('Link 1')
            if access_click is not None:
                action.move_to_element(access_click)
                action.click()
                action.perform()

        time.sleep(3)

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()