'''Los pasos que vamos a seguir:
1- Vamos a obtener el handle de la pagina actual
2- Seleccionar submit para abrir la nueva pagina
3- Obtener los handles otra vez y comparar con la pagina actual.
si NO es la pagina actual podemos usar switch_to.window para ir a esa pagina'''

import unittest
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class ChangeWindow(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('http://www.goodstartbook.com/pruebas/index.html')

    def test_current_page(self):
        '''Obtener Pagina Actual'''
        actual_handle = self.driver.current_window_handle
        print('Pagina actual:', actual_handle)

        '''Encuentra el boton submit y dale click'''
        self.driver.find_element(By.ID, 'Button1').click()
        time.sleep(3)

        '''Obtiene todos los handlos'''
        all_handles = self.driver.window_handles
        print('Todas los handles:', all_handles)

        for handle in all_handles:
            if handle != actual_handle:
                self.driver.switch_to_window(handle) #cambiarnos a la nueva ventana

        element = self.driver.find_element_by_id('Segundo')
        if element is not None:
            element.send_keys('Juan')
        time.sleep(3)

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()