import numpy as np
import cv2 as cv

image = cv.imread('/home/pi/Documents/TD/photo/samba/photo_diff/image2_diff_binary.jpg')
opening = cv.morphologyEx(image, cv.MORPH_OPEN, cv.getStructuringElement(cv.MORPH_RECT,(5,5)))
closing = cv.morphologyEx(image, cv.MORPH_CLOSE, cv.getStructuringElement(cv.MORPH_RECT,(9,9)))

cv.imwrite('/home/pi/Documents/TD/photo/samba/photo_diff/opening9.jpg', opening)
cv.imwrite('/home/pi/Documents/TD/photo/samba/photo_diff/closing9.jpg', closing)