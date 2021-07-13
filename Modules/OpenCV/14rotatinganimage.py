import cv2
import numpy as np

FILE_NAME = r'D:\Coding\Python Programming\Modules\OpenCV\yeet.jpg'

try:
    img = cv2.imread(FILE_NAME)
    (rows, cols) = img.shape[:2]
    M = cv2.getRotationMatrix2D((cols / 2, rows / 2), 45, 1)
    res = cv2.warpAffine(img, M, (cols, rows))
    cv2.imwrite('rotate.jpg', res)
except IOError:
    print('Error while reading files !!!')