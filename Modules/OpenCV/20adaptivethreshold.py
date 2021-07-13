import cv2
import numpy as np

image1 = cv2.imread('D:\Coding\Python Programming\Modules\OpenCV\yeet.jpg')

img = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)

thresh1 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 199, 5)

thresh2 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 199, 5)

cv2.imshow('1',thresh1)
cv2.imshow('2', thresh2)
cv2.waitKey(0)
cv2.destroyAllWindows()