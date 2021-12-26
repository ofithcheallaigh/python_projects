import numpy as np
import cv2

img = cv2.imread('lena.jpg', 1)             # 0 => image loaded in greyscale
# Below. First arg is image, second is starting coord., third is ending coord.,
# forth is colour in RGB format (B, G, R), last argument is the thickness
img = cv2.line(img, (0, 0), (255, 255), (0, 255, 0), 5)

cv2.imshow('imgage', img)

cv2.waitKey(0)                              # Holds image open until user closes
cv2.destroyAllWindows()

