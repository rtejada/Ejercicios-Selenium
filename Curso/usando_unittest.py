import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


class UsingUnittest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_search(self):
        driver = self.driver
        driver.get('http://www.google.com')
        self.assertIn("Google", driver.title)
        element = driver.find_element_by_name('q')
        element.send_keys("Selenium")
        element.send_keys(Keys.RETURN)
        time.sleep(3)
        assert "No se encontro el elemento:" not in driver.page_source

    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main()








