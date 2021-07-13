import cv2
import numpy as np

image1 = cv2.imread('D:\Coding\Python Programming\Modules\OpenCV\osama.jpg')
image2 = cv2.imread('D:\Coding\Python Programming\Modules\OpenCV\yeet.jpg')

img2_resize = cv2.resize(image2, (image1.shape[1], image1.shape[0]))

dest_and = cv2.bitwise_and(image1, img2_resize, mask = None)
cv2.imshow('Bitwise And', dest_and)
cv2.waitKey(0)

dest_or = cv2.bitwise_or(image1, img2_resize, mask = None)
cv2.imshow('Bitwise Or', dest_or)
cv2.waitKey(0)

dest_xor = cv2.bitwise_xor(image1, img2_resize, mask = None)
cv2.imshow('Bitwise Xor', dest_xor)
cv2.waitKey(0)

img1_not = cv2.bitwise_not(image1, mask=None)
cv2.imshow('NOT 1', img1_not)
cv2.waitKey(0)

cv2.destroyAllWindows()