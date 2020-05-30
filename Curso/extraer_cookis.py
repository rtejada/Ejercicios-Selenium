import unittest
from selenium import webdriver


class Cookis(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('https://www.w3schools.com/')

    def test_extraer_cookis(self):

        all_cookis = self.driver.get_cookies()
        print(all_cookis)

        #self.assertEqual(True, False)

    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main()
