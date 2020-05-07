import unittest
import time
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.chrome.options import Options


class selectDropDown(unittest.TestCase):

    def setUp(self):
        chrome_options = Options()
        chrome_options.add_argument("--start-maximized")
        self.driver = webdriver.Chrome(options= chrome_options)
        self.driver.get('http://www.goodstartbook.com/pruebas/index.html')

    def test_list_options(self):
        vegetables = self.driver.find_element_by_name('ingrediente')
        if vegetables is not None:
            vegetable_select = Select(vegetables)
            vegetable_select.select_by_value('cebolla')

        time.sleep(5)

    def test_select_options(self):
        fruit = self.driver.find_element_by_name('Select1')
        if fruit is not None:
            fruit_select = Select(fruit)
            fruit_select.select_by_index(1)
            fruit_select.select_by_visible_text('Sandia')

        time.sleep(5)


if __name__ == '__main__':
    unittest.main()
