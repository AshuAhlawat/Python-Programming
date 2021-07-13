import cv2

import os

image_path = r'D:\Coding\Python Programming\Modules\OpenCV\osama.jpg'

directory = r'D:\Coding\Python Programming\Modules\OpenCV'

img = cv2.imread(image_path)
os.chdir(directory)

print("Before saving Image")
print(os.listdir(directory))

filename = 'savedImage.jpg'

cv2.imwrite(filename, img)

print("After saving Image: ")
print(os.listdir(directory))
print("successfully saved")