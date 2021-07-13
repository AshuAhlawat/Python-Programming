import cv2
import numpy as np

image1 = cv2.imread('D:\Coding\Python Programming\Modules\OpenCV\yeet.jpg')
image2 = cv2.imread('D:\Coding\Python Programming\Modules\OpenCV\osama.jpg')
img2_resize = cv2.resize(image2, (image1.shape[1], image1.shape[0]))
addition = cv2.addWeighted(image1, 0.5, img2_resize, 0.5, 0)
cv2.imshow('weightend Iamge', addition)
cv2.waitKey(0)
subtract = cv2.subtract(image1, img2_resize)
cv2.imshow("subtract", subtract)
cv2.waitKey(0)
cv2.destroyAllWindows()

