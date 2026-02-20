import cv2

img = cv2.imread("images/Recent.png")
if img is None:
    print("Image gives some error !")
else:
    print("Image Loaded!")

    resize = cv2.resize(img, (1000, 300))
    cv2.imshow("Original Image !", img)
    cv2.imshow("Resized Image !", resize)

    cv2.imwrite("images/Recent_output.png", resize)


    cv2.waitKey(0)
    cv2.destroyAllWindows()
