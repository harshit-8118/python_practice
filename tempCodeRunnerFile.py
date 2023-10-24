import cv2
import matplotlib.pyplot as plt
import sys
sys.stdout = open('output.txt', 'w')

img = cv2.imread('11.jpg')

print(img.shape)

img = img[80:450, 200:600, :3]
cv2.imshow('frame', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

