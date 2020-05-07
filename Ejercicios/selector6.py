import unittest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class CountElementsHome(unittest.TestCase):

    def setUp(self) -> None:
        options = Options()
        options.add_argument('--headless')
        options.add_argument('--disable-gpu')
        self.driver = webdriver.Chrome(options=options)
        self.driver.get('http://automationpractice.com/index.php')

    def test_three_product(self):
        element = self.driver.find_element_by_xpath('//*[@id="homefeatured"]/li[3]/div/div[1]/div/a[1]/img')
        if element is not None:
            print('Tercer elemento OK')


if __name__ == '__main__':
    unittest.main()
