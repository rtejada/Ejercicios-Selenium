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
        list_minutes = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36', '37', '38', '39', '40', '41', '42', '43', '44', '45', '46', '47', '48', '49', '50', '51', '52', '53', '54', '55', '56', '57', '58', '59')
        list_hours = ('1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23')
        list_days = ('1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '26', '27', '28', '29', '30', '31')
        list_months = ('1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12')
        list_weekdays = ('0', '1', '2', '3', '4', '5', '6')

        minutes = self.driver.find_element(By.NAME, 'selectMinutes[]')
        minute_select = Select(minutes)
        minute_select.select_by_value(list_minutes[5])
        time.sleep(1)

        hours = self.driver.find_element(By.NAME, 'selectHours[]')
        hour_select = Select(hours)
        hour_select.select_by_value(list_hours[16])

        days = self.driver.find_element(By.NAME, 'selectDays[]')
        day_select = Select(days)
        day_select.select_by_value(list_days[7])

        months = self.driver.find_element(By.NAME, 'selectMonths[]')
        month_select = Select(months)
        month_select.select_by_value(list_months[6])

        weekdays = self.driver.find_element(By.NAME, 'selectWeekdays[]')
        weekday_select = Select(weekdays)
        weekday_select.select_by_value(list_weekdays[4])

        command_to_execute = 'prueba'
        tub = '>/dev/null 2>&1'

        minute = list_minutes[5]
        hour = list_hours[16]
        day = list_days[7]
        month = list_months[6]
        weekday = list_weekdays[4]

        results1 = minute, hour, day, month, weekday, command_to_execute, tub
        battery = ''

        for i in results1:
            battery = battery + i + ' '

        battery = battery.strip()

        if command_to_execute != '':

            input_value = self.driver.find_element(By.ID, 'command')
            input_value.send_keys(command_to_execute)

            button_generate = self.driver.find_element(By.NAME, 'Generate')
            button_generate.send_keys(Keys.RETURN)

            results = self.driver.find_element_by_xpath('//*[@id="generatedResult"]/pre')
            results = results.text #59 0 8 1 0 /usr/bin/php /home/username/public_html/cron.php >/dev/null 2>&1
            print(results)

            self.assertEqual(results, battery)

        else:

            inputs = self.driver.find_element(By.ID, 'command')
            inputs.send_keys(command_to_execute)

            button_generate = self.driver.find_element(By.NAME, 'Generate')
            button_generate.send_keys(Keys.ENTER)
            button_generate = self.driver.switch_to_alert()
            button_generate.accept()
            time.sleep(2)


        time.sleep(2)
        '''
        a = 5
        b = 8

        self.assertEqual(a, b)

        self.assertNotEqual(a, b)

        c = False

        self.assertTrue(c)
        '''

    def tearDown(self):
        self.driver.close()


if __name__ == 'main':
    unittest.main()
