import numpy as np
import cv2

im = cv2.imread('/home/pi/Documents/TD/photo/photo_test/test1_vers_image1.jpg')
imgray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
thresh = cv2.threshold(imgray, 115, 255, cv2.THRESH_BINARY)[1]
cv2.imwrite('/home/pi/Desktop/Photo/Surface/threshold_115/original.jpg', im)
cv2.imwrite('/home/pi/Desktop/Photo/Surface/threshold_115/gray.jpg', imgray)
cv2.imwrite('/home/pi/Desktop/Photo/Surface/threshold_115/threshold.jpg', thresh)
#contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)

#cnt = contours[4]
#img = cv2.drawContours(imgray, contours, -1, (0,255,0), 3)

#cv2.imshow('testcontours2', img)

cv2.waitKey(0)
