from numpy import random
import cv2

x = random.randint(255,size=(100))
cv2.imwrite('x.jpg',x)
cv2.imshow('x',x)
cv2.waitKey(0)
cv2.destroyAllWindows()
  