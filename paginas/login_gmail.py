from selenium import webdriver


class LoginPage:

    driver = ...  # type: webdriver.Chrome()

    def __init__(self, driver):
        self.driver = driver

    def init_session(self, username):

        email_address = self.driver.find_element_by_id('identifierId')
        if email_address is not None:
            email_address.send_keys(username)

        click_button = self.driver.find_element_by_xpath('//*[@id="identifierNext"]/span/span')
        if click_button is not None:
            click_button.click()
