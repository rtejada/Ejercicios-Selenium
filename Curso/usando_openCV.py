import unittest
import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import cv2

class UsingOpenCV(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_using_opencv(self):
        self.driver.get('http://www.google.com')
        self.driver.save_screenshot('image.png')
        time.sleep(3)

    def test_compare_image(self):
        img1 = cv2.imread('image1.png')
        img2 = cv2.imread('image.png')

        diference = cv2.absdiff(img1, img2)
        img_grey = cv2.cvtColor(diference, cv2.COLOR_BGR2GRAY)
        contours, = cv2.findContours(img_grey, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        for c in contours:
            if cv2.contourArea(c) >= 20:
                posicion_x, posicion_y, ancho, alto = cv2.boundingRect(c)
                cv2.rectangle(img1, (posicion_x, posicion_y), (posicion_x + ancho + posicion_y + alto), (0, 0, 255), 2)

        while (1):
            cv2.imshow('image1', img1)
            cv2.imshow('image', img2)
            cv2.imshow('Diferencias detectadas', diference)
            teclado = cv2.waitkey(5) & 0xFF
            if teclado == 27:
                break

        cv2.destroyAllWindows()


if __name__ == 'main':
    unittest.main()



