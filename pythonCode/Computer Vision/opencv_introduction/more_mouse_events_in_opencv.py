import numpy as np
import cv2

# Code to print the events inside a library
# events = [i for i in dir(cv2) if 'EVENT' in i]
# print(events)

# Get the event plus the x and y coordinates on the image of the click
def click_event(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        blue = img[x, y, 0]
        green = img[x, y, 1]
        red = img[x, y, 2]
        cv2.circle(img, (x, y), 3, (0, 0, 255), -1)     # -1 fills in the circle
        myColourImage = np.zeros((512, 512, 3), np.uint8)

        myColourImage[:] = [blue, green, red]

        cv2.imshow('colour', myColourImage)


# img = np.zeros((512, 512, 3), np.uint8)               # numpy zeros array which generates a black image
img = cv2.imread('lena.jpg')
cv2.imshow('image', img)
points = []

cv2.setMouseCallback('image', click_event)

cv2.waitKey(0)
cv2.destroyAllWindows()