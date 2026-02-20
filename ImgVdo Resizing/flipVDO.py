import cv2
vdo = cv2.VideoCapture("Video/input_video.mp4")
while True:
    ret, frame = vdo.read()
    if not ret:
        break
    

    # flip_horizontal = cv2.flip(img, 1)
    # cv2.imshow("Ori IMG!", img)
    # cv2.imshow("Fliped IMG!", flip_horizontal)

    # flip_vertical = cv2.flip(img, 0)
    # cv2.imshow("Ori IMG!", img)
    # cv2.imshow("Fliped IMG!", flip_vertical)


    flip_both = cv2.flip(frame, 0)
    cv2.imshow("Ori IMG!", frame)
    cv2.imshow("Fliped IMG!", flip_both)
    if cv2.waitKey(25) & 0xFF  == ord('q'):
        break
vdo.release()
cv2.destroyAllWindows()