import cv2
vdo = cv2.VideoCapture("Video/input_video.mp4")
while True:
    ret, frame = vdo.read()
    if not ret:
        break

    (h, w) = frame.shape[:2]
    center = (w//2, h//2)
    M = cv2.getRotationMatrix2D(center, 90, 1.0)
    rotated_vdo = cv2.warpAffine(frame, M, (w, h))

    cv2.imshow("Original vdo !", frame)
    cv2.imshow("Rotated vdo !", rotated_vdo)

    if cv2.waitKey(25) & 0xFF  == ord('q'):
        break
vdo.release()
cv2.destroyAllWindows()

