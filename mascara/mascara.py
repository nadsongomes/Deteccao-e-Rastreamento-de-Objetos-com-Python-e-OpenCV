# Para ver este código funcionando, mostre itens de cor verde para a câmera. Eles serão identificados, dependendo do tom de verde.

import cv2
import numpy as np

low = np.array([25, 52, 72])
high = np.array([102, 255, 255])

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    cv2.imshow('Frame Original', frame)

    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

    mask = cv2.inRange(hsv, low, high)
    cv2.imshow('Frame com máscara', mask)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
