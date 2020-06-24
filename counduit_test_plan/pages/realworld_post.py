from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime


class RealworldPost:

    URL = 'https://react-redux.realworld.io/'

    TIMESTAMP = datetime.timestamp(datetime.now())
    TITLE = ''
    POST = {'title': 'Probando ' + str(TIMESTAMP), 'about': 'Se habla de probando probando',
                 'body': 'Hablando de mis pruebas', 'tags': 'solo son pruebas'}
    COMMENT = 'Comentario Simple'

    BUTTON_WAIT_LOCATOR = (By.ID, "//a/i[@class = 'ion-compose']")

    def __init__(self, driver):
        self.driver = driver

    def load(self):
        self.driver.get(self.URL)

    def wait_button(self):
        wait = WebDriverWait(self.driver, 10, poll_frequency=1)
        wait.until(EC.element_to_be_clickable((self.BUTTON_WAIT_LOCATOR)))

    def register_new_post(self):
        pass

