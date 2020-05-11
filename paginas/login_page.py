
class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def login(self, username, password):
        nom = self.driver.find_element_by_id('nombre')
        if nom is not None:
            nom.send_keys(username)

        password = self.driver.find_element_by_name('contrasena')
        if password is not None:
            password.send_keys(password)

        click_button = self.driver.find_element_by_id('proceed')
        if click_button is not None:
            click_button.click()




