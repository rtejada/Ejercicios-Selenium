import HtmlTestRunner
import unittest


class SuiteTestCase(unittest.TestCase):

    def test_title_page(self):

        self.assertEqual('Google', 'Google')


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='/home/roxana/Documentos/Programas_Selenium/Resultado'))


