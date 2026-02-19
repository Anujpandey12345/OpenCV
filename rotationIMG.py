import cv2

img = cv2.imread("images/Recent.png")

if img is None:
    print("Image is not loaded Please tryAgain!")
else:
    (h, w) = img.shape[:2]
    center = (w//2, h//2)
    M = cv2.getRotationMatrix2D(center, 90, 1.0)
    rotated_img = cv2.warpAffine(img, M, (w, h))

    cv2.imshow("Original IMG !", img)
    cv2.imshow("Rotated_Image !", rotated_img)
    cv2.imwrite("images/rotated_img_output.png", rotated_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()