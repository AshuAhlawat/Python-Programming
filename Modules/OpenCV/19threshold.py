import cv2
import numpy as np

image1 = cv2.imread('D:\Coding\Python Programming\Modules\OpenCV\yeet.jpg')
img = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)

ret, thresh1 = cv2.threshold(img, 120, 255, cv2.THRESH_BINARY)
ret, thresh2 = cv2.threshold(img, 120, 255, cv2.THRESH_BINARY_INV)
ret, thresh3 = cv2.threshold(img, 120, 255, cv2.THRESH_TRUNC)
ret, thresh4 = cv2.threshold(img, 120,255, cv2.THRESH_TOZERO)
ret, thresh5 = cv2.threshold(img, 120,255, cv2.THRESH_TOZERO_INV)

cv2.imshow('1', thresh1)
cv2.imshow('2', thresh2)
cv2.imshow('3', thresh3)
cv2.imshow('4', thresh4)
cv2.imshow('5', thresh5)

cv2.waitKey(0)
cv2.destroyAllWindows()