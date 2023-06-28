import cv2 as cv
import numpy as np

img = cv.imread("imgprocessing/pic1.jpg")

def line(x0, y0, x1, y1, _color):
    start_point = (x0, y0)
    end_point = (x1, y1)
    color = _color
    thickness = 9
    cv.line(img, start_point, end_point, color, thickness)

# line(0,0,img.shape[1], img.shape[0], (0, 255, 0))
arr = [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
filterSize = 15
for y in range(0, 5):
    for x in range(0, 5):
        if(x == y):
            arr[x][y] = 1
        else:
            arr[x][y] = 0
print(arr)
kernel = np.ones((filterSize,filterSize), np.float32)/(filterSize**2)

output = cv.filter2D(src=img, ddepth=-1, kernel=kernel, borderType=cv.BORDER_REFLECT)

cv.imshow("", output)
cv.waitKey(0)
cv.destroyAllWindows()