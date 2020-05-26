from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import ElementNotVisibleException
from selenium.common.exceptions import ElementNotSelectableException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class RegisterNewPost:
    def __init__(self, driver, post):
        self.driver = driver

        self.post = post

    def get_url(self):

        wait = WebDriverWait(self.driver, 10, poll_frequency=1,
                             ignored_exceptions=[ElementNotVisibleException, ElementNotSelectableException])
        wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="main"]/div/div/div[1]/div/h1')))

        return self.driver.current_url

    def new_post(self):

        wait = WebDriverWait(self.driver, 10, poll_frequency=1,
                             ignored_exceptions=[ElementNotVisibleException, ElementNotSelectableException])
        wait.until(EC.element_to_be_clickable((By.XPATH, "//a/i[@class = 'ion-compose']")))

        create_post = self.driver.find_element_by_xpath("//a/i[@class = 'ion-compose']")
        create_post.click()

        title_article = self.driver.find_element_by_xpath('//*[@id="main"]//fieldset/fieldset[1]/input')
        title_article.click()
        title_article.send_keys(self.post['title'])

        about_article = self.driver.find_element_by_xpath('//*[@id="main"]//fieldset/fieldset[2]/input')
        about_article.click()
        about_article.send_keys(self.post['about'])

        body_article = self.driver.find_element_by_xpath("//textarea[@class = 'form-control']")
        body_article.click()
        body_article.send_keys(self.post['body'])

        tags_article = self.driver.find_element_by_xpath("//input[@placeholder='Enter tags']")
        tags_article.click()
        tags_article.send_keys(self.post['tags'])

        intro_article = self.driver.find_element_by_xpath("//button[@type='button']")
        intro_article.send_keys(Keys.ENTER)
