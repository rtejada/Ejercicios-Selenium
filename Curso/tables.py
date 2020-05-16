import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class ParseTable(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('https://www.w3schools.com/html/html_tables.asp')
        time.sleep(5)

    def test_parse_table(self):
        rows = len(self.driver.find_elements(By.XPATH, '//*[@id="customers"]/tbody/tr'))
        col = len(self.driver.find_elements(By.XPATH, '//*[@id="customers"]/tbody/tr[1]/th'))
        head_table = self.driver.find_elements(By.XPATH, '//*[@id="customers"]/tbody/tr/th')

        for head in head_table:
            print(head.text, end='                  ')

        print()

        for a in range(2, rows + 1):
            for b in range(1, col + 1):
                values = self.driver.find_element(By.XPATH, '//*[@id="customers"]/tbody/tr['+str(a)+']/td['+str(b)+']')
                print(values.text, end='    ')
            print()
        print()

    def tearDown(self):
        self.driver.close()


if __name__ == 'main':
    unittest.main()

