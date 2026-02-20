import cv2

img = cv2.imread("images/Recent.png")

if img is None:
    print("Opp's ! Your image is give's error !")
else:
    print("Image Loaded successfully !")
    cv2.circle(img, (150, 150), 50, (250, 0, 0), -1)
    cv2.imshow("Circle Draw !", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()