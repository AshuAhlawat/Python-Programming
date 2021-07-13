import cv2

image = cv2.imread('D:\Coding\Python Programming\Modules\OpenCV\osama.jpg')
cv2.imshow('original', image)
cv2.waitKey()

gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

cv2.imshow('Grayscale', gray_image)
cv2.waitKey(0)

img = cv2.imread('D:\Coding\Python Programming\Modules\OpenCV\yeet.jpg', 0)

cv2.imshow('g', img)
cv2.waitKey()

cv2.destroyAllWindows()