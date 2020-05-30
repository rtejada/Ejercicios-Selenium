import unittest
from selenium import webdriver


class CapturarPantalla(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('https://www.youtube.com/watch?v=DnsNYxDbaAA&list=PLas30d-GGNa2UW9-1H-NCNrUocvWD9cyh&index=36')

    def test_captura_pantalla(self):
        self.driver.get_screenshot_as_file('/home/roxana/Documentos/captura_pantalla.png')
        #self.assertEqual(True, False)

    def tearDown(self):
        self.driver.close()



if __name__ == '__main__':
    unittest.main()
