import cv2

img = cv2.imread("images/Recent.png")

if img is None:
    print("Image is not loaded Please tryAgain!")
else:
    # flip_horizontal = cv2.flip(img, 1)
    # cv2.imshow("Ori IMG!", img)
    # cv2.imshow("Fliped IMG!", flip_horizontal)

    # flip_vertical = cv2.flip(img, 0)
    # cv2.imshow("Ori IMG!", img)
    # cv2.imshow("Fliped IMG!", flip_vertical)


    flip_both = cv2.flip(img, 0)
    cv2.imshow("Ori IMG!", img)
    cv2.imshow("Fliped IMG!", flip_both)

    cv2.waitKey(0)
    cv2.destroyAllWindows()