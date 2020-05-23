import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class SignIn(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_in_session(self):
        self.driver.get('https://es-es.facebook.com/')
        time.sleep(3)
        mail = self.driver.find_element_by_id('email')
        mail.send_keys('rtejadasilva@gmail.com')
        mail.send_keys(Keys.ENTER)
        time.sleep(2)
        passw = self.driver.find_element_by_id('pass')
        passw.send_keys('prueba')
        passw.send_keys(Keys.ENTER)
        time.sleep(2)

        self.driver.execute_script('window.open("");')
        time.sleep(2)
        self.driver.switch_to.window(self.driver.window_handles[1])
        self.driver.get('https://twitter.com/iniciarsesion?lang=es')

        time.sleep(2)
        session = self.driver.find_element_by_link_text("Iniciar sesión")
        session.send_keys(Keys.ENTER)
        time.sleep(2)
        user_name = self.driver.find_element_by_name('session[username_or_email]')
        user_name.send_keys('rtejadasilva@gmail.com')
        user_name.send_keys(Keys.ENTER)
        time.sleep(2)
        password = self.driver.find_element_by_name('session[password]')
        password.send_keys('prueba')
        password.send_keys(Keys.ENTER)

        time.sleep(2)
        self.driver.switch_to.window(self.driver.window_handles[0])
        time.sleep(2)

    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main()



