import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    _, frame = cap.read()
    blurred_frame = cv2.GaussianBlur(frame, (5, 5), 0)
    hsv = cv2.cvtColor(blurred_frame, cv2.COLOR_BGR2HSV)

    low = np.array([25, 52, 72])
    high = np.array([102, 255, 255])

    mascara = cv2.inRange(hsv, low, high)

    contours, _ = cv2.findContours(mascara, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

    for contour in contours:
        area = cv2.contourArea(contour)
        if area>1000:
            cv2.drawContours(frame, contours, -1, (0, 0, 255), 3)

    cv2.imshow("Frame", frame)
    cv2.imshow("mascara", mascara)



    if cv2.waitKey(1)==27:
        break
cap.release()
cv2.destroyAllWindows()