from selenium.webdriver.common.keys import Keys
import time

class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def login_user(self):
        user_name = "roxana"
        password = "roxana"
        self.driver.get("http://{}:{}@217.182.87.241/testlink/".format(user_name, password))
        user = self.driver.find_element_by_xpath('//*[@id="tl_login"]')
        user.click()
        user.send_keys(user_name)

        passw = self.driver.find_element_by_name('tl_password')
        passw.click()
        passw.send_keys(password)

        intro = self.driver.find_element_by_xpath('//*[@id="login"]/div[3]/input')
        intro.send_keys(Keys.ENTER)

