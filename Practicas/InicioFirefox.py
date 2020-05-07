from selenium import webdriver
driver = webdriver.Firefox()
#driver = webdriver.Chrome()

driver.get('http://www.goodstartbook.com/pruebas/index.html')
driver.quit()
