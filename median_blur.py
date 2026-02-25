import cv2
img = cv2.imread("images/Recent.png")
blurred = cv2.medianBlur(img, 7)

cv2.imshow("Original Image : ", img)
cv2.imshow("Median Blur : ", blurred)
cv2.waitKey(0)
cv2.destroyAllWindows()