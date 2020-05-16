import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.chrome.options import Options


class SearchForPag(unittest.TestCase):
    def setUp(self):
        options = Options()
        options.add_argument('--headless')
        options.add_argument('--disable-gpu')
        self.driver = webdriver.Chrome(options=options)

    def test_search(self):
        pal_search = 're'
        self.driver.get('https://www.google.com/')
        time.sleep(5)
        search = self.driver.find_element_by_name('q')
        search.send_keys(pal_search)
        time.sleep(2)

        for i in range(1, 11):
            elements = self.driver.find_elements_by_xpath("//*[@id='tsf']/div[2]/div[1]/div[2]/div[2]/ul/li['+str(i)+']/div/div[2]/div/span/b").text
            print(pal_search + elements)

    def tearDown(self):
        self.driver.close()


if __name__ == 'main':
    unittest.main()
