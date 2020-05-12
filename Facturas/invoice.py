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

    def test_invoice(self):

        self.invoice_info()
        self.product_info()

    def invoice_info(self):
        name_company = self.driver.find_element_by_xpath('//*[@id="invoice-company-name"]')
        if name_company is not None:
            name_company.click()
            time.sleep(1)
            name_company.send_keys('Industrias Textiles')
        email_company = self.driver.find_element_by_xpath('//*[@id="invoice-company-email"]')
        if email_company is not None:
            email_company.click()
            time.sleep(1)
            email_company.send_keys('pepito@gmail.com')
            time.sleep(1)
        address_company = self.driver.find_element_by_xpath('//*[@id="invoice-company-address1"]')
        if address_company is not None:
            address_company.click()
            time.sleep(1)
            address_company.send_keys('Av. Libertad')
            time.sleep(1)
        city = self.driver.find_element_by_xpath('//*[@id="invoice-company-address2"]')
        if city is not None:
            city.click()
            time.sleep(1)
            city.send_keys('Madrid')
            time.sleep(1)
        cp = self.driver.find_element_by_xpath('//*[@id="invoice-company-address3"]')
        if cp is not None:
            cp.click()
            time.sleep(1)
            cp.send_keys('28000')
            time.sleep(1)
        phone_company = self.driver.find_element_by_xpath('//*[@id="invoice-company-phone"]')
        if phone_company is not None:
            phone_company.click()
            time.sleep(1)
            phone_company.send_keys('6457878')
            time.sleep(1)
        phone_business = self.driver.find_element_by_xpath('//*[@id="invoice-company-business-number"]')
        if phone_business is not None:
            phone_business.click()
            time.sleep(1)
            phone_business.send_keys('6457878')
            time.sleep(1)
        drop_down = self.driver.find_element_by_css_selector('.invoice-detail-terms .Select--single')
        if drop_down is not None:
            drop_down.click()
            time.sleep(1)
            action = ActionChains(self.driver)
            action.move_to_element(drop_down).perform()

            element = self.driver.find_element(By.ID, "invoice-item-code")
            actions = ActionChains(self.driver)
            actions.move_to_element(element).release().perform()

        name_client = self.driver.find_element(By.ID, 'invoice-client-name')
        if name_client is not None:
            name_client.click()
            time.sleep(1)
            name_client.send_keys('Pedro')
            time.sleep(1)
        email_client = self.driver.find_element(By.XPATH, '//*[@id="invoice-client-email"]')
        if email_client is not None:
            email_client.click()
            time.sleep(1)
            email_client.send_keys('pedro@gmail.com')
            time.sleep(1)
        address = self.driver.find_element(By.ID, 'invoice-client-address1')
        if address is not None:
            address.click()
            time.sleep(1)
            address.send_keys('Calle Madrid S/N')
            time.sleep(1)
        city_client = self.driver.find_element_by_xpath('//*[@id="invoice-client-address2"]')
        if city_client is not None:
            city_client.click()
            time.sleep(1)
            city_client.send_keys('Madrid')
            time.sleep(1)
        cp_city = self.driver.find_element_by_xpath('//*[@id="invoice-client-address3"]')
        if cp_city is not None:
            cp_city.click()
            time.sleep(1)
            cp_city.send_keys('28000')
            time.sleep(1)
        phone_client = self.driver.find_element(By.ID, 'invoice-client-phone')
        if phone_client is not None:
            phone_client.click()
            time.sleep(1)
            phone_client.send_keys('00000000')
            time.sleep(1)

    def product_info(self):

        details = [["Camisa", "De algon pima y gamusa", '20', '1'], ["Vestido", "lo que sea", '30', '2'],
                   ["vaquero", "para vaqueros", '18.50', '2']]

        number_elements = len(details)

        i = 0
        total_price = 0
        for description in details:
            i += 1

            product_name = description[0]
            description_name = description[1]
            price = description[2]
            units = description[3]

            amount = float(price) * int(units)
            total_price += amount

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

            if i < number_elements:
                add = self.driver.find_element(By.XPATH, '//*[@id="invoice-item-add"]')
                add.click()

    def test_import(self):
        type_iva = self.driver.find_element(By.CSS_SELECTOR, ".invoice-tax-type-input .Select-arrow")
        type_iva.click()
        element = self.driver.find_element(By.ID, "invoice-tax-rate")
        actions = ActionChains(type_iva)
        actions.move_to_element(element).release().perform()

        name = self.driver.find_element(By.ID, 'invoice-tax-label')
        name.click()
        name.send_keys('iva')

        time.sleep(5)

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
