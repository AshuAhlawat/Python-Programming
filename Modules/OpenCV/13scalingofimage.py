import cv2
import numpy as np

FILE_NAME = r'D:\Coding\Python Programming\Modules\OpenCV\yeet.jpg'
try:
    img = cv2.imread(FILE_NAME)
    (height, width) = img.shape[:2]
    res = cv2.resize(img, (int(width / 2), int(height/2)), cv2.INTER_CUBIC)
    cv2.imwrite('result.jpg', res)
except IOError:
    print('Error while reading files!!')

