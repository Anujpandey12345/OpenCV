import cv2

img = cv2.imread("images/Recent.png")

if img is None:
    print("Opp's ! Your image is give's error !")
else:
    print("Image Loaded successfully !")
    P1 = (50, 50)
    P2 = (250, 200)
    color = (250, 0 , 0)
    thikness = 3
    cv2.rectangle(img, P1, P2, color, thikness)
    cv2.imshow("Line draw !", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()