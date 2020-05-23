import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select


class Register(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_register_account(self):
        self.driver.get('https://es-es.facebook.com/')
        time.sleep(2)
        nom = self.driver.find_element_by_name('firstname')
        time.sleep(1)
        nom.send_keys('Txana')
        time.sleep(1)
        surname = self.driver.find_element_by_name('lastname')
        surname.send_keys('Silva')
        time.sleep(1)
        email = self.driver.find_element_by_name("reg_email__")
        email.send_keys('rsilvas@gmail.com')
        time.sleep(1)
        email_confirmation = self.driver.find_element_by_name("reg_email_confirmation__")
        email_confirmation.send_keys('rsilvas@gmail.com')
        time.sleep(1)
        passw = self.driver.find_element_by_name("reg_passwd__")
        passw.send_keys('pruebaNueva')
        time.sleep(1)

        day = self.driver.find_element_by_id('day')
        days_select = Select(day)
        days_select.select_by_value('13')
        time.sleep(1)

        month = self.driver.find_element_by_id('month')
        months_select = Select(month)
        months_select.select_by_value('8')
        time.sleep(1)

        year = self.driver.find_element_by_id('year')
        years_select = Select(year)
        years_select.select_by_value('2000')
        time.sleep(1)

        sexo = self.driver.find_element_by_css_selector("input[type='radio'][value='1']")
        sexo.click()
        time.sleep(1)

        registration = self.driver.find_element_by_name('websubmit')
        registration.send_keys(Keys.RETURN)
        time.sleep(2)

