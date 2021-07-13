import cv2

path = r'D:\Coding\Python Programming\Modules\OpenCV\osama.jpg'

image = cv2.imread(path)

window_name = 'image'

image = cv2.copyMakeBorder(image, 10, 10, 10, 10, cv2.BORDER_CONSTANT)

cv2.imshow(window_name, image)

cv2.waitKey(0)
cv2.destroyAllWindows()

image1 = cv2.copyMakeBorder(image, 100,100,50,50,cv2.BORDER_REFLECT)
cv2.imshow(window_name, image1)
cv2.waitKey(0)
cv2.destroyAllWindows()