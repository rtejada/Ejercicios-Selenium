import unittest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class SelectorMenu(unittest.TestCase):
    def setUp(self):
        options = Options()
        options.add_argument('--headless')
        options.add_argument('--disable-gpu')
        self.driver = webdriver.Chrome(options=options)
        self.driver.get('http://thedemosite.co.uk/')

    def test_select_home(self):
        home = self.driver.find_element_by_xpath('//a[@href = "index.php"]')
        if home is not None:
            print('Home encontrada')

    def test_select_database(self):
        home = self.driver.find_element_by_xpath('//a[@href = "thedatabase.php"]')
        if home is not None:
            print('DataBase encontrada')

    def test_add_user(self):
        home = self.driver.find_element_by_xpath('//a[@href = "addauser.php"]')
        if home is not None:
            print('Add User encontrada')

    def test_login(self):
        home = self.driver.find_element_by_xpath('//a[@href = "login.php"]')
        if home is not None:
            print('Login encontrada')

    def test_db_online(self):
        home = self.driver.find_element_by_xpath('//a[@href = "getyourowndbonline.php"]')
        if home is not None:
            print('DB Online encontrada')


if __name__ == '__main__':
    unittest.main()
