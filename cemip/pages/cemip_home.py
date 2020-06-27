from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.cemip_base_page import CualEsMiIpBasePage


class CualEsMiIpHome(CualEsMiIpBasePage):
    URL = 'https://www.cual-es-mi-ip.net/'
    LINK_TEXT_BUTTON = 'Geolocalizar IP'
    LOCATOR_WAIT = (By.ID, "direccion-ip")

    def press_button(self):
        geolocate_button = self.driver.find_element_by_link_text(self.LINK_TEXT_BUTTON)
        geolocate_button.send_keys(Keys.RETURN)

