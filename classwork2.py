import cv2 as cv
import numpy as np

img = cv.imread("imgprocessing/Image-Processing/Circle_Objects.png")

cv.imshow("", img)
cv.waitKey(0)
cv.destroyAllWindows()