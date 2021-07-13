import cv2
import numpy as np

filename = r'D:\Coding\Python Programming\Modules\OpenCV\yeet.jpg'
try:
    img = cv2.imread(filename)
    edges = cv2.Canny(img, 100,200)
    cv2.imwrite('edges.jpg', edges)

except IOError:
    print('Error')