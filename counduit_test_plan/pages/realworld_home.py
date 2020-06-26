from lib.login import Login


class RealworldHome:

    URL = 'https://react-redux.realworld.io/'

    def __init__(self, driver):
        self.driver = driver

    def load(self):
        self.driver.get(self.URL)

    def init_session(self):
        login = Login(self.driver)
        url_profile = login.login_user()
        return url_profile


