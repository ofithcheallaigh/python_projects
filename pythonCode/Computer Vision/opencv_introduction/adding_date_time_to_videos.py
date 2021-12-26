import cv2
import datetime

cap = cv2.VideoCapture(0)                       # 0 is the device index. If that doesn't work, try -1
print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))        # Prints video frame width
print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))       # Prints video frame height

# cap.set(3, 1208)                                # 3 is the number of the property CAP_PROP_FRAME_WIDTH
# cap.set(4, 720)                                 # 4 is the number of the property CAP_PROP_FRAME_HEIGHT
# print(cap.get(3))                               # Prints video frame width
# print(cap.get(4))                               # Prints video frame height
while(cap.isOpened()):
    ret, frame = cap.read()
    if ret == True:
        # grey = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
        font = cv2.FONT_HERSHEY_COMPLEX
        text = 'Width ' +  str(cap.get(3)) + ' Height ' + str(cap.get(4))
        datet = str(datetime.datetime.now())
        frame = cv2.putText(frame, datet, (10, 50), font, 1, (0, 255, 255), 2, cv2.LINE_AA)
        cv2.imshow('frame', frame)

        if cv2.waitKey(1) & (0xFF) == ord('q'):
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()
