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

        for min in list_minutes:
            minute = min
            for hour in list_hours:
                hour = hour
                for day in list_days:
                    day = day
                    for month in list_months:
                        month = month
                        for weekd in list_weekdays:
                            weekday = weekd

                            minutes = self.driver.find_element(By.NAME, 'selectMinutes[]')
                            minute_select = Select(minutes)
                            minute_select.deselect_all()
                            minute_select.select_by_value(min)

                            hours = self.driver.find_element(By.NAME, 'selectHours[]')
                            hour_select = Select(hours)
                            hour_select.deselect_all()
                            hour_select.select_by_value(hour)

                            days = self.driver.find_element(By.NAME, 'selectDays[]')
                            day_select = Select(days)
                            day_select.deselect_all()
                            day_select.select_by_value(day)

                            months = self.driver.find_element(By.NAME, 'selectMonths[]')
                            month_select = Select(months)
                            month_select.deselect_all()
                            month_select.select_by_value(month)

                            weekdays = self.driver.find_element(By.NAME, 'selectWeekdays[]')
                            weekday_select = Select(weekdays)
                            weekday_select.deselect_all()
                            weekday_select.select_by_value(weekd)
                            time.sleep(1)

                            command = '/home/username/Roxana/'
                            tub = '>/dev/null 2>&1'

                            results1 = minute, hour, day, month, weekday, command, tub
                            battery = ''

                            for k in results1:
                                battery = battery + k + ' '

                            battery = battery.strip()

                            if command != '':

                                input_value = self.driver.find_element(By.ID, 'command')
                                input_value.click()
                                input_value.clear()
                                input_value.send_keys(command)

                                #self.driver.execute_script("document.getElementById('command').value = /home/username/Roxana/")
                                time.sleep(1)

                                button_generate = self.driver.find_element(By.NAME, 'Generate')
                                button_generate.send_keys(Keys.RETURN)

                                results = self.driver.find_element_by_xpath('//*[@id="generatedResult"]/pre')
                                results = results.text #59 0 8 1 0 /usr/bin/php /home/username/public_html/cron.php >/dev/null 2>&1

                                self.assertEqual(results, battery)

                            elif command == '':

                                inputs = self.driver.find_element(By.ID, 'command')
                                inputs.send_keys(command)

                                button_generate = self.driver.find_element(By.NAME, 'Generate')
                                button_generate.send_keys(Keys.ENTER)
                                button_generate = self.driver.switch_to_alert()
                                button_generate.accept()
                                continue

    def tearDown(self):
        self.driver.close()


if __name__ == 'main':
    unittest.main()
