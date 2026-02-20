import cv2
vdo = cv2.VideoCapture("Video/input_video.mp4")
while True:
    ret, frame = vdo.read()
    if not ret:
        break

    resized = cv2.resize(frame, (640, 720))
    cv2.imshow("Original Vdo !", frame)
    cv2.imshow("Resized Vdo !", resized)

    if cv2.waitKey(100) & 0xFF == ord('q'):
        break

vdo.release()
cv2.destroyAllWindows()
