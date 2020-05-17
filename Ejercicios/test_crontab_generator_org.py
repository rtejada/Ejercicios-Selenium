from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select
import unittest
import time


class GenerateCrontab(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('https://crontab-generator.org/')

    def test_selector_times(self):
        minutes = self.driver.find_element(By.NAME, 'selectMinutes[]')
        minute_select = Select(minutes)
        minute_select.select_by_value('4')
        time.sleep(2)

        hours = self.driver.find_element(By.NAME, 'selectHours[]')
        hour_select = Select(hours)
        hour_select.select_by_value('7')
        time.sleep(2)

        days = self.driver.find_element(By.NAME, 'selectDays[]')
        day_select = Select(days)
        day_select.select_by_value('28')
        time.sleep(2)

        months = self.driver.find_element(By.NAME, 'selectMonths[]')
        month_select = Select(months)
        month_select.select_by_value('5')
        time.sleep(2)

        weekdays = self.driver.find_element(By.NAME, 'selectWeekdays[]')
        weekday_select = Select(weekdays)
        weekday_select.select_by_value('6')
        time.sleep(2)

        command_to_execute = 'https://crontab-generator.org/'
        inputs = self.driver.find_element(By.ID, 'command')
        inputs.send_keys(command_to_execute)

        self.assertEqual(command_to_execute, inputs)

        buttom = self.driver.find_element(By.NAME, 'Generate')
        buttom.send_keys(Keys.ENTER)

        time.sleep(1000)

        a = 5
        b = 8

        self.assertEqual(a, b)

        self.assertNotEqual(a, b)

        c = False

        self.assertTrue(c)

    def tearDown(self):
        self.driver.close()


if __name__ == 'main':
    unittest.main()

