from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import ElementNotVisibleException
from selenium.common.exceptions import ElementNotSelectableException


class AddComment:
    def __init__(self, driver, comment):
        self.driver = driver
        self.comment = comment

    def add_comment(self):
        wait = WebDriverWait(self.driver, 10, poll_frequency=1,
                             ignored_exceptions=[ElementNotVisibleException, ElementNotSelectableException])
        wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="main"]//div[1]/a/h1')))

        go_comment = self.driver.find_element_by_xpath('//*[@id="main"]//div[1]/a/h1')
        go_comment.click()

        wait = WebDriverWait(self.driver, 10, poll_frequency=1,
                             ignored_exceptions=[ElementNotVisibleException, ElementNotSelectableException])
        wait.until(EC.visibility_of_element_located((By.XPATH, "//div/form/div/textarea[@class='form-control']")))

        add_comment = self.driver.find_element_by_xpath("//div/form/div/textarea[@class='form-control']")
        add_comment.click()

        add_comment.send_keys(self.comment)
        sent_comment = self.driver.find_element_by_xpath("//div/button[@type='submit']")
        sent_comment.send_keys(Keys.ENTER)

        wait = WebDriverWait(self.driver, 10, poll_frequency=1,
                             ignored_exceptions=[ElementNotVisibleException, ElementNotSelectableException])
        wait.until(EC.visibility_of_element_located((By.XPATH, "//div/p[@class='card-text']")))

        comment_add = self.driver.find_element_by_xpath("//div/p[@class='card-text']")
        comment_add = comment_add.text
        return comment_add




