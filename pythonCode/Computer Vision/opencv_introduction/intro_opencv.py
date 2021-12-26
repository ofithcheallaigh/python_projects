import cv2

img = cv2.imread('lena.jpg', -1)        # 0 flag, image loads in greyscale, 1 = colour, -1 = colour with alpha channel
# print(img)                            # will produce pixel matrix

cv2.imshow('image',img)
k = cv2.waitKey(0)                      # Number of milliseconds to show image, if you use 0, it will never close itself
if k == 27:                             # Number signifies the esc key
    cv2.destroyAllWindows()
elif k == ord('s'):
    # Write an image to a file
    cv2.imwrite('lena_copy.png',img)
    cv2.destroyAllWindows()

