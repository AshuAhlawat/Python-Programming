import cv2
import numpy as np

FILE_NAME = r'D:\Coding\Python Programming\Modules\OpenCV\yeet.jpg'

image1 = cv2.imread(FILE_NAME)

img = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)

ret, thresh1 = cv2.threshold(img, 120, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)

cv2.imshow('otsu', thresh1)

cv2.waitKey(0)
cv2.destroyAllWindows()
