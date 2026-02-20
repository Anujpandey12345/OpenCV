import cv2

img = cv2.imread("images/Recent.png")

if img is None:
    print("Opp's ! Your image is give's error !")
else:
    print("Image Loaded successfully !")
    cv2.putText(img, "Hello! Python Developer", (50, 300), cv2.FONT_HERSHEY_SIMPLEX, 1.2, (250, 0, 0), 2)
    cv2.imshow("Adding Text in the image !", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()