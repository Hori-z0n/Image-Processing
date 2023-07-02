import cv2 as cv
import numpy as np

img = cv.imread("imgprocessing/Image-Processing/Circle_Objects.png", cv.COLOR_GRAY2BGR)
blur = cv.GaussianBlur(img, (5, 5), cv.BORDER_DEFAULT)
blur = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

_, binary = cv.threshold(blur, 225, 255, cv.THRESH_BINARY_INV)
contours, hierarchy = cv.findContours(binary, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)

# blank = np.zeros(thresh.shape[:2],dtype='uint8')
blank = np.zeros(binary.shape[:2],dtype='uint8')
# cv.drawContours(blank, contours, -1,(255, 0, 0), 1)
for i in contours:
    M = cv.moments(i)
    if M['m00'] != 0:
        cx = int(M['m10']/M['m00'])
        cy = int(M['m01']/M['m00'])
        cv.drawContours(img, [i], -1, (0, 255, 0), 2)
        cv.circle(img, (cx, cy), 7, (0, 0, 255), -1)
        cv.putText(img, "center", (cx - 20, cy - 20),
                   cv.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 2)
    print(f"x: {cx} y: {cy}")
    

cv.imshow("1", binary)

cv.imwrite("Contours.png", blank)
cv.waitKey(0)
cv.destroyAllWindows()