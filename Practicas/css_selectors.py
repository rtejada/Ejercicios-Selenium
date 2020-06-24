import unittest
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver import ActionChains


driver = webdriver.Chrome()
driver.get('http://www.goodstartbook.com/pruebas/index.html')
'''
#importante - encuentra nodos con el id = importante
table#primera - encuentra tabla con el id = importante
[name] - encuentra todos los elementos con atributo name
[name = ultimo]
[name = tabla prueba][id = primera] encuntra los elementos con atributo name e id
.rojo = todos los elementos que usan la clase rojo
tr.rojo = encuentra la fila donde la clase es rojo
tr.rojo>td = encuentra nodos hijos de la fila donde la clase es rojo
tr,td = filas y columnas
[name^='tabla'] = encuentra elementos donde el atributo name empieza por tabla
[name*='pru'] atributo contien la cadena
[name$='prueba'] abtributo contiene al final prueba
'''

