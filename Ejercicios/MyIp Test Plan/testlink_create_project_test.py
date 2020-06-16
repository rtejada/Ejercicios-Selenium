from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import unittest
import time
from login_pass_testlink import *


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_create_project(self):

        login = LoginPage(self.driver)
        login.login_user()

        self.driver.switch_to.frame(self.driver.find_element_by_xpath('/html/frameset/frame[2]'))

        open_new_project = self.driver.find_element_by_link_text('Gestión de Proyectos de Pruebas')
        open_new_project.click()

        create_new_project = self.driver.find_element_by_id('create')
        create_new_project.click()

        name_project = self.driver.find_element_by_name('tprojectName')
        name_project.send_keys('Automatización Selenium')
        pref_project = self.driver.find_element_by_name('tcasePrefix')
        pref_project.send_keys('Sel')

        check1 = self.driver.find_element_by_name('optReq')
        check1.click()
        check2 = self.driver.find_element_by_name('optInventory')
        check2.click()

        create = self.driver.find_element_by_xpath("//table/tbody//tr/td/div/input[@name='doActionButton']")
        create.click()
        time.sleep(4)
        '''
        edit_project = self.driver.find_element_by_link_text('Automatización Selenium')
        edit_project.click()

        self.driver.switch_to.frame(self.driver.find_element_by_xpath('//*[@id="cke_1_contents"]/iframe'))
        description_project = self.driver.find_element_by_tag_name('p')
        description_project.click()
        description_project.send_keys('pruebas Selenium')
        '''



    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main()
