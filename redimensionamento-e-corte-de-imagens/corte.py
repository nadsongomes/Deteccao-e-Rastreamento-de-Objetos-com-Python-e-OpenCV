import cv2
import numpy as np

img = cv2.imread("carro.png")
print(img.shape)
imgCropped = img[0:200,200:500]
cv2.imshow("imagem",img)
cv2.imshow("imagem cortada",imgCropped)
cv2.waitKey(0)