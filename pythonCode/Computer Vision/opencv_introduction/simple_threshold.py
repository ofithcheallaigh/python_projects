# Thresholding - popular segmentation technique for separating an object
# from its background

import cv2 as cv
import numpy as np

img = cv.imread('gradient.png', 0)                          # 0 = greyscale
_, th1 = cv.threshold(img, 127, 255, cv.THRESH_BINARY)
_, th2 = cv.threshold(img, 127, 255, cv.THRESH_BINARY_INV)
# With cv.THRESH_TRIMC, pixel value does not change up to threshold, but then
# every value after is set to the threshold value
_, th3 = cv.threshold(img, 120, 255, cv.THRESH_TRUNC)
# When pixel value is less than threshold, pixel value will be assigned zero
# When pixel value is grester than threshold, the pixel value will remain the same
_, th4 = cv.threshold(img, 120, 255, cv.THRESH_TOZERO)
_, th5 = cv.threshold(img, 120, 255, cv.THRESH_TOZERO_INV)



cv.imshow("Image", img)
cv.imshow("th2", th2)
cv.imshow("th3", th3)
cv.imshow("th4", th4)
cv.imshow("th5", th5)


cv.waitKey(0)
cv.destroyAllWindows()


