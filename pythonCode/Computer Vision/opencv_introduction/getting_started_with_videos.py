import cv2

cap = cv2.VideoCapture(0)               # cap is instance of video capture. Device index is either 0 or -1
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 480))
# For above, 'fourcc' is standard I think, but needs to put passed to 'out'. The 20.0 is the frames per second
# and the (640,480) is the frame size

print(cap.isOpened())
while(cap.isOpened()):
    ret, frame = cap.read()              # Image is stored in 'frame'. ret is bool variable, if frame is available
                                        # ret is true, otherwise false

    if ret == True:
        print("Frame width: ", cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        print("Frame height: ", cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

        out.write(frame)

        grey = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)       # Greyscale imagine
        cv2.imshow('frame', grey)           # Shows the video

        # Not quite sure what the below line is doing, but it allows pressing the 'q' key to quit
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

out.release()
cap.release()
cv2.destroyAllWindows()

