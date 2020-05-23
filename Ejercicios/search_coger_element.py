from selenium import webdriver
import time

driver = webdriver.Firefox()
driver.get('http://www.w3c.org')
element = driver.find_element_by_name('q')
element.send_keys('hi mom')
time.sleep(2)
element_text = element.text
element_attribute_value = element.get_attribute('value')

print (element)
print ('element.text: {0}'.format(element_text))
print ('element.get_attribute(\'value\'): {0}'.format(element_attribute_value))
time.sleep(2)

element = driver.find_element_by_css_selector('.description.expand_description > p')
element_text = element.text
element_attribute_value = element.get_attribute('value')

print (element)
print ('element.text: {0}'.format(element_text))
print ('element.get_attribute(\'value\'): {0}'.format(element_attribute_value))
time.sleep(2)
driver.quit()