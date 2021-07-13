import cv2
import numpy as np

#in this proccess we determine that which part of that image contains yellow

path = r'D:\Coding\Python Programming\Modules\OpenCV\yeet.jpg'

image1 = cv2.imread(path)

hsv = cv2.cvtColor(image1, cv2.COLOR_BGR2HSV)

lower_yellow = np.array([20,100,100])
upper_yellow = np.array([30,255,255])

mask = cv2.inRange(hsv, lower_yellow, upper_yellow)

result = cv2.bitwise_and(image1, image1, mask=mask)

cv2.imshow('1', image1)
cv2.imshow('2', mask)
cv2.imshow('3', result)
cv2.waitKey(0)
cv2.destroyAllWindows()
