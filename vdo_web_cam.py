# import cv2

# vdo = cv2.VideoCapture(0)
# while True:
#     ret, frame = vdo.read() #ret = True/False, frame = image
#     if not ret:
#         print("Could not read frame !")
#         break

#     cv2.imshow("Webcap !", frame)

#     if cv2.waitKey(1) & 0xFF == ord('q'):  # cv2.waitKey(1) & 0xFF This genrate the 113 == 113(q)
#         print("Quiting,.........")
#         break
# vdo.release()
# cv2.destroyAllWindows()

