import cv2
import numpy as np  
img = cv2.imread("images/Recent11.jpg")
sharpen_blur = np.array([
    [0, -1, 0],
    [-1, 5, -1],
    [0, -1, 0]
])
blurred = cv2.filter2D(img, -1, sharpen_blur)

cv2.imshow("Original Image : ", img)
cv2.imshow("Sharpen Imagee : ", blurred)
cv2.waitKey(0)
cv2.destroyAllWindows()