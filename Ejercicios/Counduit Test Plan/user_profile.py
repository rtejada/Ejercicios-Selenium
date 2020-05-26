from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementNotVisibleException
from selenium.common.exceptions import ElementNotSelectableException


class UserProfile:
    def __init__(self, driver):
        self.driver = driver

    def user_profile_post(self):
        self.driver.switch_to.window(self.driver.window_handles[0])
        profile = self.driver.find_element_by_xpath('//*[@id="main"]//div/ul/li[4]/a')
        profile.click()

        wait = WebDriverWait(self.driver, 10, poll_frequency=1,
                             ignored_exceptions=[ElementNotVisibleException, ElementNotSelectableException])
        wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="main"]//div[1]/a/h1')))

        last_published_article = self.driver.find_element_by_xpath('//*[@id="main"]//div[1]/a/h1')
        last_published_article = last_published_article.text
        return last_published_article
