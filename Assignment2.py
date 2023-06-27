import cv2 as cv
import numpy as np

img = cv.imread("imgprocessing/pic1.jpg")
width = img.shape[1] #x
height = img.shape[0] #y
cut = width//2
left = img[:, :cut]
right = img[:, cut:]

cv.imshow("left",left)
cv.imshow("right",right)

print(width)
print(height)
cv.waitKey(0)
cv.destroyAllWindows()