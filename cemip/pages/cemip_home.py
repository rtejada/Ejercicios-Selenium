from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CualEsMiIpHome:
    URL = 'https://www.cual-es-mi-ip.net/'
    LINK_TEXT_BUTTON = 'Geolocalizar IP'
    BUTTON_WAIT_LOCATOR = (By.ID, "direccion-ip")

    def __init__(self, driver):
        self.driver = driver

    def load(self):
        self.driver.get(self.URL)

    def press_button(self):
        geolocate_button = self.driver.find_element_by_link_text(self.LINK_TEXT_BUTTON)
        geolocate_button.send_keys(Keys.RETURN)

    def wait_button(self):

        wait = WebDriverWait(self.driver, 10, poll_frequency=1)
        wait.until(EC.visibility_of_element_located(self.BUTTON_WAIT_LOCATOR))
