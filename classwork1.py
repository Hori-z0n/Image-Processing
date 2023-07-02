import cv2 as cv
import numpy as np

width = 32
height = 32
image = np.zeros((height, width), dtype=np.uint8)

start_point = (0, 10)
end_point = (20, 30)
color = (255, 255, 255)
thickness = 1

img = cv.line(image, start_point, end_point, color, thickness)

cv.imwrite("filter.png", img)

root = "pic.jpg"
input = cv.imread(root, cv.IMREAD_GRAYSCALE)
filter = cv.imread("filter.png", cv.IMREAD_GRAYSCALE)

filter_sum = filter.sum()
filter = filter / filter_sum

output = cv.filter2D(src=input, ddepth=-1, kernel=filter)

cv.imwrite("output.png", output)