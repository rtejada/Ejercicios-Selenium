import time


class CheckPost:
    def __init__(self, driver):
        self.driver = driver

    def check_post(self, url):

        self.driver.get(url)
        time.sleep(2)

        title = self.driver.find_element_by_xpath('//*[@id="main"]//div[1]/div/h1')
        title = title.text

        body = self.driver.find_element_by_xpath('//*[@id="main"]//div[2]/div[1]//div/p')
        body = body.text

        return title, body



