import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class BrowseWindow(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_change_window_following_and_previous(self):
        self.driver.get('http://www.gmail.com')
        time.sleep(3)
        self.driver.get('http://www.google.com')
        time.sleep(3)
        self.driver.get('http://www.youtube.com')
        time.sleep(3)
        self.driver.back()

        time.sleep(3)
        self.driver.back()
        time.sleep(3)
        self.driver.forward()
        time.sleep(3)

    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main()
