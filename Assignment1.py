import cv2 as cv
import numpy as np

import math

image = np.zeros((600, 600, 3), dtype=np.uint8)

radius = 50
center_x = 200
center_y = 200

def slope(x0, y0, x1, y1):
    return (y1-y0)/(x1-x0)

def draw_line(x1, y1, x2, y2):
    for y in range(y1, y2):
        for x in range(x1, x2):
            if(x == y):
                image[y, x] = (255, 255, 255)

def draw_line2(x1, y1, x2, y2, c):
    # m = (y2 - y1)/(x2 - x1)
    m = slope(x1, y1, x2, y2)
    for x in range(x1, x2 + 1):
        y = round(m * x + c)
        image[y, x] = (255, 255, 255)

def draw_line3(x1, y1, x2, y2):
    dx = x2-x1
    dy = y2-y1
    p = 2*dy-dx
    while(x1 < x2):
        if(p>=0):
            image[y1, x1] = (255, 255, 255)
            y1 = y1+1
            p = p + 2*dy-2*dx
        else:
            image[y1, x1] = (255, 255, 255)
            p = p + 2*dy
            x1 = x1+1

def draw_line4(x, radius):
    for i in range(0, x):
        dy = int(abs(i * np.sin(radius)))
        dx = int(abs(i * np.cos(radius)))
        image[dy, dx] = (255, 255, 255)


def draw_line5(x0, y0, x1, y1, radius):
    m = slope(x0, y0, x1, y1)
    dy = math.sin(30)
    # dy = np.sin(radius)
    dx = np.cos(radius)
    print("y = ", dy)
    print("x = ", dx)
    for y in range(y0, y1):
        for x in range(x0, x1):
            dy = int(abs(y * np.sin(radius)))
            dx = int(abs(x * np.cos(radius)))
            image[dy, dx] = (255, 255, 255)

def draw_regtangle(x1, y1, x2, y2):
    for y in range(y1, y2):
        for x in range(x1, x2):
            image[y, x] = (255, 255, 255)

draw_line2(0, 0, 100, 100, 0)
draw_line2(0, 100, 100, 0, 0)
draw_line2(498, 599, 599, 498, 0)
draw_line2(498, 498, 599, 599, 0)
draw_line2(100, 100, 500, 100, 100)
draw_line2(100, 100, 500, 100, 500)
draw_regtangle(100, 100, 101, 500)
draw_regtangle(500, 100, 501, 500)

# draw_line4(0, 0, 100, 100, 30)
# draw_line5(100, 30)
cv.imshow("Circle", image)
cv.waitKey(0)
cv.destroyAllWindows()