from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from lib.ip import IP

class CualEsMiIpMaxMind:

    URL = 'https://www.maxmind.com/en/locate-my-ip-address'
    LOCATOR_WAIT = (By.XPATH, '//*[@id="geoip-demo-results-tbody"]/tr/td[1]')
    LOCATOR_COLUMN = (By.XPATH, '//*[@id="geoip-demo-results-tbody"]/tr/td')

    def __init__(self, driver):
        self.driver = driver

    def load(self):
        self.driver.get(self.URL)

        wait = WebDriverWait(self.driver, 10, poll_frequency=1)
        wait.until(EC.visibility_of_element_located(self.LOCATOR_WAIT))

    def get_data(self):

        col_maxmind = len(self.driver.find_elements(*self.LOCATOR_COLUMN))
        data_maxmind = []

        for j in range(1, col_maxmind):
            values = self.driver.find_element(By.XPATH,
                                              '//*[@id="geoip-demo-results-tbody"]/tr[' + str(1) + ']/td[' + str(j) + ']')
            data_maxmind.append(values.text)

        ip = IP()
        ip.ip = data_maxmind[0]

        city_nation = data_maxmind[2]
        ip.country = city_nation[26:31]
        ip.city = city_nation[0:8]

        longitude_latitude = data_maxmind[5]
        ip.lat = float(longitude_latitude[0:7])
        ip.lon = float(longitude_latitude[-7:])

        ip.isp = data_maxmind[7]

        return ip