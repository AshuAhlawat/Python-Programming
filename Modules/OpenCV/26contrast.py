import cv2
import numpy as np

img = cv2.imread('D:\Coding\Python Programming\Modules\OpenCV\yeet.jpg')

def pixelVal(pix, r1, s1, r2, s2):
    if(0 <= pix and pix <= r1):
        return (s1/r1)*pix
    elif(r1 < pix and pix <= r2):
        return  ((s2 - s1)/(r2 - r1)) * (pix - r1) + s1
    else:
        return ((255 - s2)/(255 - r2)) * (pix - r2) + s2
    
r1 = 70
s1 = 0
r2 = 140
s2 = 255

pixelval_vec = np.vectorize(pixelVal)

contrast_streched = pixelval_vec(img, r1,s1,r2,s2)

cv2.imwrite("contrast_streche.jpg", contrast_streched)