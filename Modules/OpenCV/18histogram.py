import cv2
from matplotlib import pyplot as plt

img = cv2.imread('D:\Coding\Python Programming\Modules\OpenCV\yeet.jpg',0)

histr = cv2.calcHist([img],[0],None,[256],[0,256])

plt.plot(histr)
plt.show() 