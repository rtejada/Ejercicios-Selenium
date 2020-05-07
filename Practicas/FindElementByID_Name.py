from selenium import webdriver

driver = webdriver.Chrome()
driver.get('http://www.goodstartbook.com/pruebas/index.html')
element = driver.find_element_by_id('noImportante')
if element is not None:
    print('El Elemento ID fue encontrado')

element = driver.find_element_by_name('ultimo')
if element is not None:
    print('El Elemento Name fue encontrado')

driver.quit()

