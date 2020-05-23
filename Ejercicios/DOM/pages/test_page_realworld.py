import unittest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from datetime import datetime
from register_page import RegisterPage
from login_page import LoginPage
from register_post import RegisterNewPost


class GenerateRealworld(unittest.TestCase):
    def setUp(self):
        options = Options()
        options.add_argument("--incognito")
        self.driver = webdriver.Chrome(options=options)
        self.driver.get('https://react-redux.realworld.io/')
        now = datetime.now()
        timestamp = datetime.timestamp(now)
        self.url = ''
        self.post = {'title': 'Probando ' + str(timestamp), 'about': 'Se habla de probando probando',
                     'body': 'Hablando de mis pruebas', 'tags': 'solo son pruebas'}

    '''
    def test_register_user(self):
        registration = RegisterPage(self.driver)
        registration.user_registration('MariPuri', 'maripuri@gmail.com', 'maripuri2020')
    '''
    def test_login_and_register_post(self):
        login = LoginPage(self.driver)
        login.login_user('maripuri@gmail.com', 'maripuri2020')

        post = RegisterNewPost(self.driver, self.post)
        self.url = post.new_post()

    def tearDown(self):
        self.driver.close()


if __name__ == 'main':
    unittest.main()

