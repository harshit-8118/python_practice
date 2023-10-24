import cv2

# face_cascade = cv2.CascadeClassifier('FaceDetection\haarcascade_frontalface_alt.xml')

# img = cv2.imread('FaceDetection\/test.jpg')
# print(img.shape)
# img = cv2.resize(img, (1200, 700))
# if img.shape[0] == 0:
#     exit(1)
# gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# results = face_cascade.detectMultiScale(gray_img, 1.15, 10)

# for (x, y, w, h) in results:
#     cv2.rectangle(img, pt1=(x, y), pt2=(x + w, y + h), color=(244,0,0), thickness=2)

# cv2.imshow('Image', img)

# cv2.waitKey(0)
# cv2.destroyAllWindows()

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret: 
        continue
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
