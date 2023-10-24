import cv2
import numpy as np
import matplotlib.pyplot as plt

import sys
sys.stdout = open('output.txt', 'w')

cap = cv2.VideoCapture(0) # infinitely capture image
# load cascades
face_cascade = cv2.CascadeClassifier('FaceDetection\haarcascade_frontalface_alt.xml')
eye_cascade = cv2.CascadeClassifier('FaceDetection\haarcascade_eye.xml')

# print(face_cascade)
while True:
    ''' continuously read frames from video '''
    ret, frame = cap.read() # returns (bool, img_matrix) 
    # print(frame.shape, ret)
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    if not ret:
        continue

    faces = face_cascade.detectMultiScale(image=gray_frame, scaleFactor=1.3, minNeighbors=5, flags=cv2.CASCADE_SCALE_IMAGE) # can read gray frame only
    eyes = eye_cascade.detectMultiScale(gray_frame, 1.15, 5, flags=cv2.CASCADE_SCALE_IMAGE)

    for (x, y, w, h) in faces:
        cv2.rectangle(img=frame, pt1=(x, y), pt2=(x+w, y+h), color=(0,0,255), thickness=2)
    
    for (x, y, w, h) in eyes:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 255, 0), 2)
    
    cv2.imshow('Frame', frame)
    # cv2.imshow('Gray frame', gray_frame)  # black and white window

    #Wait input - q, then you will stop the loop
    key_pressed = cv2.waitKey(1) & 0xFF
    if key_pressed == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()
 

'''
scaleFactor - Parameter specifying how much the image size is reduced at each image scale.
Basically the scale factor is used to create your scale pyramid. More explanation can be found here. In short, as described here, your model has a fixed size 
1.05 is a good possible value for this, which means you use a small step for resizing, i.e. reduce size by 5%, you increase the chance of a matching size with
minNeighbors
Parameter specifying how many neighbors each candidate rectangle should have to retain it
This parameter will affect the quality of the detected faces. Higher value results in less detections but with higher quality. 3-6 is a good value for it.

read ~ 
https://www.analyticsvidhya.com/blog/2022/10/face-detection-using-haar-cascade-using-python/

'''


'''
Steps:
- load haarcascade files for detection face, eyes, body, vehicle etc.
- capture video(0) infinitely or paste image or load video
- read as frame from video, 
- convert image in gray scale image bcoz "detectMultiScale" can reads gray scale image only
- for all faces draw boundaries 
- show in cv2
- don't forget to release cap and destroy windows
'''


