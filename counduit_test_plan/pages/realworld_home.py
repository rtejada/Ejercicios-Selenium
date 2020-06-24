from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from lib.login import Login

class RealworldHome:

    URL = 'https://react-redux.realworld.io/'

    def __init__(self, driver):
        self.driver = driver

    def load(self):
        self.driver.get(self.URL)

    def init_session(self):
        login = Login(self.driver)
        login.login_user()


