import time


class UserProfile:
    def __init__(self, driver):
        self.driver = driver

    def user_profile_post(self):
        self.driver.switch_to.window(self.driver.window_handles[0])
        time.sleep(2)
        profile = self.driver.find_element_by_xpath('//*[@id="main"]//div/ul/li[4]/a')
        profile.click()
        last_published_article = self.driver.find_element_by_xpath('//*[@id="main"]//div[1]/a/h1')
        last_published_article = last_published_article.text
        return last_published_article
