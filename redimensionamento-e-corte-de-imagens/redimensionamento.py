import cv2
import numpy as np

img = cv2.imread("carro.png")
originalWidth, originalHeight, _ = img.shape
newWidth = 100
newHeight = int((originalHeight/originalWidth)*newWidth)
imgResize = cv2.resize(img,(newHeight,newWidth))
print(originalWidth, originalHeight)
print(newWidth,newHeight)
cv2.imshow("carro",img)
cv2.imshow("carro redimensionado",imgResize)
cv2.waitKey(0)