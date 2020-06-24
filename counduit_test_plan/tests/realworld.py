import unittest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pages.realworld_home import RealworldHome
from pages.realworld_post import RealworldPost


class Realworld(unittest.TestCase):
    def setUp(self):
        options = Options()
        options.add_argument("--incognito")
        self.driver = webdriver.Chrome()

    def tearDown(self):
        self.driver.close()

    def test_realworld(self):
        home = RealworldHome(self.driver)

        home.init_session()

        post = RealworldPost(self.driver)
        post.load()
        post.wait_button()

