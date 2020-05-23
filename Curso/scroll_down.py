import unittest
import time
from selenium import webdriver


class UsingScrollDown(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_scroll_window(self):
        self.driver.get('https://www.amazon.es/')
        time.sleep(2)
        self.driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')
        time.sleep(2)

        work_amazon = self.driver.find_element_by_link_text('Trabajar en Amazon')
        work_amazon.click()
        time.sleep(3)

    def tearDown(self):
        self.driver.close()


if __name__ == 'main':
    unittest.main()
