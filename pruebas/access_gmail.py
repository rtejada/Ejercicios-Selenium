import unittest
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from paginas.login_gmail import LoginPage


class ClickSendKeys(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('https://www.gmail.com/')
        # self.driver.implicitly_wait(15) #espera 15 segundos antes de enviar error

    def test_login(self):
        page_init = LoginPage(self.driver)
        page_init.init_session('gfyhgvgygy@gmail.com')
        time.sleep(3)

    def tearDown(self):
        self.driver.quit()
