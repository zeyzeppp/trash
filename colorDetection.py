import cv2
import numpy as np

cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()
    frame = cv2.flip(frame, 1)
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    lower_orange = np.array([161, 155, 70])
    upper_orange = np.array([179, 255, 255])
    orange_mask = cv2.inRange(hsv_frame, lower_orange, upper_orange)
    orange = cv2.bitwise_and(frame, frame, mask = orange_mask)


    cv2.imshow("webcam", frame)
    cv2.imshow("HSV Orange", orange_mask)
    cv2.imshow("original", orange)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break




cv2.destroyAllWindows()

