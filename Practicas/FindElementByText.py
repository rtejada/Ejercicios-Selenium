import unittest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class GetAttributeText(unittest.TestCase):

    def setUp(self):

        options = Options()
        options.add_argument('--headless')
        options.add_argument('--disable-gpu')  # Last I checked this was necessary.

        self.driver = webdriver.Chrome(options=options)
        self.driver.get('http://www.goodstartbook.com/pruebas/index.html')

    def test_get_text(self):
        option = self.driver.find_element_by_xpath("//tr[@id='noImportante']/td[2]")

        if option is not None:
            print('Texto:', option.text) #Muestra valor del atributo

    def test_get_class(self):
        option2 = self.driver.find_element_by_id('importante')
        if option2 is not None:
            value_atrib = option2.get_attribute('class')
            print('Clase:', value_atrib)


    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()

