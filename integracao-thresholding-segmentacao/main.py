import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread('placa.jpg')
image_resized = cv2.resize(image,(800,500))
lower_green = np.array([46,80,0])
upper_green = np.array([109,255,10])
mask = cv2.inRange(image_resized, lower_green, upper_green)
detected_output = cv2.bitwise_and(image_resized, image_resized, mask=mask)
cv2.imshow("PCB detection", detected_output)
cv2.waitKey(0)

detected_output = cv2.cvtColor(detected_output, cv2.COLOR_BGR2RGB)
pixel_values = detected_output.reshape((-1,3))
pixel_values = np.float32(pixel_values)
print(pixel_values.shape)
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TermCriteria_MAX_ITER, 100, 0.2)
k=3
_,labels, (centers) = cv2.kmeans(pixel_values, k, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)
centers = np.uint8(centers)
labels = labels.flatten()
segmented_image = centers[labels.flatten()]
segmented_image = segmented_image.reshape(detected_output.shape)
plt.imshow(segmented_image)
plt.show()