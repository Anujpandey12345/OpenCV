import cv2

img = cv2.imread("images/Recent.png")

if img is not None:
    print("Image loaded SuccessFully!")
    cropped = img[100:200, 50:150]
    cv2.imshow("Ori IMG!", img)
    cv2.imshow("Cropped IMG!", cropped)
    cv2.imwrite("New_cropped_IMG.png", cropped)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("Image got some error Please fix it then again TRY!")