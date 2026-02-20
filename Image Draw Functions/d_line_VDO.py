import cv2
vdo = cv2.VideoCapture("Video/input_video.mp4")
while True:
    ret, frame = vdo.read()
    if not ret:
        break

    P1 = (50, 100)
    P2 = (300, 100)
    color = (250, 0 , 0)
    thikness = 4
    cv2.line(frame, P1, P2, color, thikness)
    cv2.imshow("Draw line vdo !", frame)
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break
vdo.release()
cv2.destroyAllWindows()