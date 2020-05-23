
class RegisterPage:
    def __init__(self, driver):
        self.driver = driver

    def user_registration(self, nom, mail, passw):
        sign_up = self.driver.find_element_by_link_text('Sign up')
        sign_up.click()

        username = self.driver.find_element_by_xpath('//input[@type="text"]')
        username.click()
        username.send_keys(nom)

        email = self.driver.find_element_by_xpath('//input[@type="email"]')
        email.click()
        email.send_keys(mail)

        password = self.driver.find_element_by_xpath('//input[@type="password"]')
        password.click()
        password.send_keys(passw)

        sign_in = self.driver.find_element_by_xpath('//button[@type="submit"]')
        sign_in.click()
