import cv2

image = cv2.imread('osama.jpg')
h,w = image.shape[:2]
print("Height = {}, width = {}".format(h,w))
(B, G, R) = image[100,100]
# print("R = {}, G = {}, B = {}".format(R,G,B))
B = image[100,100,0]
# print("B = {}".format(B))
# resize = cv2.resize(image, (800,800))
output = image.copy()

rectangle = cv2.rectangle(output, (1500,900),(60,400),(255,0,0),2)

