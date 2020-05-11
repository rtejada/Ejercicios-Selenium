import unittest
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class PageTwo:
    def __init__(self, driver):
        self.driver = driver

    def intro_nom(self, nom):
        wait = WebDriverWait(self.driver, 10)
        nom1 = wait.until(EC.element_to_be_clickable((By.ID, 'Segundo')))
        if nom1 is not None:
            nom1.send_keys(nom)
            print('prueba exitosa')
            time.sleep(3)



