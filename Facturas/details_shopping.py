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
        cantidad = len(details)
        i = 0
        for description in details:
            i += 1

            product_name = description[0]
            description_name = description[1]
            price = description[2]
            units = description[3]

            product_input = self.driver.find_element(By.XPATH, '(//input[@id="invoice-item-code"])[last()]')
            product_input.click()
            time.sleep(1)
            product_input.send_keys(product_name)

            description_input = self.driver.find_element(By.XPATH, '(//textarea[@class="item-description-input"])[last()]')
            description_input.click()
            time.sleep(1)
            description_input.send_keys(description_name)

            price_input = self.driver.find_element(By.XPATH, '(//input[@placeholder="0.00"])[last()]')
            price_input.click()
            time.sleep(1)
            price_input.send_keys(price)

            quantity = self.driver.find_element(By.XPATH, '(//input[@placeholder="0"])[last()]')
            quantity.click()
            quantity.clear()
            time.sleep(1)
            quantity.send_keys(units)

            if i < cantidad:
                add = self.driver.find_element(By.XPATH, '//*[@id="invoice-item-add"]')
                add.click()

            time.sleep(2)

        type_iva = self.driver.find_element(By.CSS_SELECTOR, ".invoice-tax-type-input .Select-arrow")
        type_iva.click()
        element = self.driver.find_element(By.ID, "invoice-tax-rate")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).release().perform()

        self.driver.execute_script("document.getElementById('invoice-tax-rate').value = '21.000%'")
        time.sleep(1000)

        print_invoice = self.driver.find_element(By.CSS_SELECTOR, ".btn-print > span")
        print_invoice.click()
        time.sleep(1)

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
