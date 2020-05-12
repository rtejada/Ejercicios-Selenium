import unittest
import time
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


class InsertDates(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('file:///home/roxana/Documentos/Programas_HTML_CSS/HojasInscripcion.html')
        self.driver.implicitly_wait(15)

    def test_dates(self):
        name = self.driver.find_element_by_name('nombre')
        name.click()
        name.send_keys('Roxana')

        last_name = self.driver.find_element_by_name('apellidos')
        last_name.click()
        last_name.send_keys('Tejada')

        dni = self.driver.find_element(By.ID, 'dni')
        dni.click()
        dni.send_keys('055055055T')

        place_of_origin = self.driver.find_element(By.ID, 'loc_nacimiento')
        place_of_origin.click()
        place_of_origin.send_keys('Madrid')

        provincia = self.driver.find_element_by_name('provincia')
        if provincia is not None:
            province_select = Select(provincia)
            province_select.select_by_visible_text('Murcia')

        self.driver.execute_script("document.getElementById('fec_nac').value = '2000-02-01'")

        address = self.driver.find_element_by_name('direccion')
        address.click()
        address.send_keys('Av. del Pinar')

        cp = self.driver.find_element(By.ID, 'cp')
        cp.click()
        cp.send_keys('28925')
        time.sleep(5)

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()


