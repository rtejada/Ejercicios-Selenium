import unittest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import time
from datetime import datetime
from register_page import RegisterPage
from login_page import LoginPage
from register_post import RegisterNewPost
from check_post import CheckPost
from user_profile import UserProfile
from add_comment import AddComment

class GenerateRealworld(unittest.TestCase):

    def setUp(self):
        options = Options()
        options.add_argument("--incognito")

        self.driver = webdriver.Chrome(options=options)
        now = datetime.now()
        timestamp = datetime.timestamp(now)

        self.title = ''
        self.post = {'title': 'Probando ' + str(timestamp), 'about': 'Se habla de probando probando',
                     'body': 'Hablando de mis pruebas', 'tags': 'solo son pruebas'}

        self.comment = 'Este es un comentario simple'

    '''
    def test_register_user(self):
        registration = RegisterPage(self.driver)
        registration.user_registration('MariPuri', 'maripuri@gmail.com', 'maripuri2020')
    '''

    def login_and_register(self):

        self.driver.get('https://react-redux.realworld.io/')
        login = LoginPage(self.driver)
        login.login_user('maripuri@gmail.com', 'maripuri2020')

        time.sleep(2)
        post = RegisterNewPost(self.driver, self.post)
        return post.new_post()

    def test_a_check_post(self):

        url = self.login_and_register()

        title_article = (self.post['title'])
        body_Article = (self.post['body'])

        check = CheckPost(self.driver)
        title, body = check.check_post(url)

        self.assertEqual(title_article, title)
        self.assertEqual(body_Article, body)

        profile = UserProfile(self.driver)
        last_published_article = profile.user_profile_post()

        self.assertEqual(title_article, last_published_article)
        add = AddComment(self.driver, self.comment)
        comment_add = add.add_comment()
        self.assertEqual(self.comment, comment_add)

    def tearDown(self):
        self.driver.close()


if __name__ == 'main':
    unittest.main()

