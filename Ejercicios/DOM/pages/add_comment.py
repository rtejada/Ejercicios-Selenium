from selenium.webdriver.common.keys import Keys
import time


class AddComment:
    def __init__(self, driver, comment):
        self.driver = driver
        self.comment = comment

    def add_comment(self):
        go_comment = self.driver.find_element_by_xpath('//*[@id="main"]//div[1]/a/h1')
        go_comment.click()
        add_comment = self.driver.find_element_by_xpath("//div/form/div/textarea[@class='form-control']")
        add_comment.click()
        time.sleep(1)
        add_comment.send_keys(self.comment)
        sent_comment = self.driver.find_element_by_xpath("//div/button[@type='submit']")
        sent_comment.send_keys(Keys.ENTER)
        time.sleep(2)
        comment_add = self.driver.find_element_by_xpath("//div/p[@class='card-text']")
        comment_add = comment_add.text
        return comment_add




