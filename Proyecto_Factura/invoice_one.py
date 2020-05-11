import unittest
import time
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


class InsertDates(unittest.TestCase):
    def setUp(self):
        options = Options()
        options.add_argument("--incognito")
        self.driver = webdriver.Chrome(options=options)
        self.driver.get('https://www.invoicesimple.com/invoice-generator')

    def test_insert_dates(self):

        details = [["Camisa", "De algon pima y gamusa", '20', '1'], ["Vestido", "lo que sea", '30', '2'],
                   ["vaquero", "para vaqueros", '18.50', '2']]

        for description in details:

            product_name = description[0]
            description_name = description[1]
            price = description[2]
            units = description[3]

            product_input = self.driver.find_element(By.XPATH, '//*[@id="invoice-item-code"] [last()]')
            product_input.click()
            time.sleep(1)
            product_input.send_keys(product_name)

            description_input = self.driver.find_element(By.CSS_SELECTOR, ".item-description-input")
            description_input.click()
            time.sleep(1)
            description_input.send_keys(description_name)

            price_input = self.driver.find_element(By.CSS_SELECTOR, ".item-row-rate input")
            price_input.click()
            time.sleep(1)
            price_input.send_keys(price)

            quantity = self.driver.find_element(By.CSS_SELECTOR, ".item-row-quantity input")
            quantity.click()
            quantity.clear()
            time.sleep(1)
            quantity.send_keys(units)

            add = self.driver.find_element(By.XPATH, '//*[@id="invoice-item-add"]')
            add.click()
            time.sleep(1)


        '''
        print_invoice = self.driver.find_element(By.CSS_SELECTOR, ".btn-print > span")
        print_invoice.click()
        time.sleep(10)


        '''


if __name__ == '__main__':
    unittest.main()
