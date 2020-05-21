from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import unittest

'''Bloquear notificaciones en las paginas web
argumentos: 1 = permitir notificacion, 2 = bloquear notificacion'''


class NotificationPermissions(unittest.TestCase):
    def setUp(self):
        options = Options()
        options.add_experimental_option("prefs", {
            "profile.default_content_setting_values.notifications": 1
        })
        self.driver = webdriver.Firefox(options=options)

    def test_permission_notification(self):

        self.driver.get('https://developer.mozilla.org/es/docs/Web/API/notification')
        time.sleep(2)

    def tearDown(self):
        self.driver.close()


if __name__ == 'main':
    unittest.main()

