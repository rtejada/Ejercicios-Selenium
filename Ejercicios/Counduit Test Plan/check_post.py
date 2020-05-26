from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementNotVisibleException
from selenium.common.exceptions import ElementNotSelectableException


class CheckPost:
    def __init__(self, driver):
        self.driver = driver

    def check_post(self, url):
        self.driver.execute_script('window.open("");')

        self.driver.switch_to.window(self.driver.window_handles[1])
        self.driver.get(url)

        wait = WebDriverWait(self.driver, 10, poll_frequency=1,
                             ignored_exceptions=[ElementNotVisibleException, ElementNotSelectableException])
        wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="main"]//div[1]/div/h1')))

        title = self.driver.find_element_by_xpath('//*[@id="main"]//div[1]/div/h1')
        title = title.text

        body = self.driver.find_element_by_xpath('//*[@id="main"]//div[2]/div[1]//div/p')
        body = body.text

        return title, body



