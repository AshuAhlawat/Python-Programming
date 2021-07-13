import cv2
import numpy as np
from matplotlib import pyplot as plt

image = cv2.imread("D:\Coding\Python Programming\Modules\OpenCV\osama.jpg")

cv2.imshow('x', image)
cv2.waitKey(0)
Gaussian = cv2.GaussianBlur(image, (7,7),0)
cv2.imshow('Gaussian', Gaussian)
cv2.waitKey(0)

bilateral = cv2.bilateralFilter(image, 9, 75, 75)
cv2.imshow('b', bilateral)
cv2.waitKey(0)
cv2.destroyAllWindows()