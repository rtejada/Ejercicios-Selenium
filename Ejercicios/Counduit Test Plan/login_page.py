

class LoginPage:
    def __init__(self, driver):
        self.driver = driver


    def login_user(self, mail, passw):
        sign_up = self.driver.find_element_by_link_text('Sign in')
        sign_up.click()

        email = self.driver.find_element_by_xpath('//input[@type="email"]')
        email.click()
        email.send_keys(mail)

        password = self.driver.find_element_by_xpath('//input[@type="password"]')
        password.click()
        password.send_keys(passw)

        sign_in = self.driver.find_element_by_xpath('//button[@type="submit"]')
        sign_in.click()
