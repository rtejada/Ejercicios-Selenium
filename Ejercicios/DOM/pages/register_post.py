
from selenium.webdriver.common.keys import Keys


class RegisterNewPost:
    def __init__(self, driver, post):
        self.driver = driver

        self.post = post

    def new_post(self):
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

        url = self.driver.find_element_by_link_text("MariPuri")
        url = url.text
        print(url)

        return url

    def check_title(self):

        home = self.driver.find_element_by_link_text('Home')
        home.click()

        global_feed = self.driver.find_element_by_link_text('Global Feed')
        global_feed.click()

        title = self.driver.find_element_by_link_text












