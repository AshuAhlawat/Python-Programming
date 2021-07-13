import cv2

path = r'D:\Coding\Python Programming\Modules\OpenCV\yeet.jpg'
img = cv2.imread(path, 0)

window_name = 'image'

cv2.imshow(window_name, img)

cv2.waitKey(0)

cv2.destroyAllWindows()