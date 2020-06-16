from selenium import webdriver
import unittest
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time


class DescargarArchivos(unittest.TestCase):
    def setUp(self):
        options = Options()
        options.add_experimental_option('prefs',{
            'download.default_directory': '/home/roxana',})
        self.driver = webdriver.Chrome(chrome_options=options)

    def test_descargar_archivo(self):
        self.driver.get('https://www.w3schools.com/tags/tryit.asp?filename=tryhtml5_a_download')
        time.sleep(3)
        self.driver.switch_to.frame(self.driver.find_element_by_xpath('/html/body/div[7]/div[4]/div/div/iframe'))
        time.sleep(3)
        self.driver.find_element_by_xpath('/html/body/p[2]/a').click()
        time.sleep(5)

    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
        unittest.main()


