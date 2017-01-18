import numpy as np
import cv2

# = np.loadtxt("C:\\Users\\ywq\\Desktop\\example.csv", delimiter=",")
img = cv2.imread ('screenshot.jpg', 0)

cv2.imshow('image', img)

cv2.waitKey(0)

cv2.destroyAllWindows()
