import cv2
vdo = cv2.VideoCapture("Video/input_video.mp4")

while True:
    ret, frame = vdo.read()
    if not ret:
        break

    cropped = frame[100:200, 50:150]
    cv2.imshow("Original vod : ", frame)
    cv2.imshow("Cropped vod : ", cropped)
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break
vdo.release()
cv2.destroyAllWindows()