import cv2 as cv
import numpy as np

img = cv.imread("Circle_Objects.png", cv.COLOR_GRAY2BGR)
blur = cv.GaussianBlur(img, (5, 5), cv.BORDER_DEFAULT)
blur = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

_, binary = cv.threshold(blur, 225, 255, cv.THRESH_BINARY_INV)
contours, hierarchy = cv.findContours(binary, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)

# blank = np.zeros(thresh.shape[:2],dtype='uint8')
blank = np.zeros(binary.shape[:2],dtype='uint8')
# cv.drawContours(blank, contours, -1,(255, 0, 0), 1)
new = cv.bitwise_not(binary)
cv.imwrite('pic2.png', new)

def draw(image):
    img = cv.imread(image)
    mark = cv.inRange(img, (0, 0, 0), (200, 200, 200))
    non = np.transpose(np.nonzero(mark))
    for(y, x) in non:
        cv.circle(img, (x, y), 28, (0, 0, 0),56)
    
    cv.imshow('', img)
    cv.waitKey(0)
    cv.destroyAllWindows()
draw('Circle_Objects.png')
# cv.imshow('', )
cv.waitKey(0)
cv.destroyAllWindows()