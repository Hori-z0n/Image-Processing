import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

src = cv.imread("pic3.jpg")
img = cv.imread('imagewithsp.png')
fil = cv.medianBlur(img, ksize=3)
dst = cv.fastNlMeansDenoisingColored(fil, None, 10, 10, 7, 21)


plt.subplot(2,2,1),plt.imshow(src)
plt.subplot(2,2,2),plt.imshow(img)
plt.subplot(2,2,3),plt.imshow(dst)
plt.subplot(2,2,4),plt.imshow(fil)


plt.show()