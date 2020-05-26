import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class Browsetabs(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('http://www.google.com')

    def test_change_tab(self):
        self.driver.execute_script('window.open("");')
        time.sleep(3)
        self.driver.switch_to.window(self.driver.window_handles[1])
        self.driver.get('https://github.com/')
        time.sleep(3)
        self.driver.switch_to.window(self.driver.window_handles[0])
        time.sleep(3)

    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main()

