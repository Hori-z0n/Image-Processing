import cv2 as cv
import numpy as np


def block_img(path, dx, dy, n):
    img = cv.imread(path)
    width = img.shape[1]
    height = img.shape[0]
    # print(width)
    # print(height)
    c = 0
    for y in range(dy, width, n):
        for x in range(dx, height, n):
            image = img[y:y+n, x:x+n]
            cv.imshow(str(c), image)
            c += 1
        
if __name__ == '__main__':
    block_img("imgprocessing/pic4.jpg",0, 0, 500)
    cv.waitKey(0)
    cv.destroyAllWindows()