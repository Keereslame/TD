import cv2 as cv
import numpy as ny

imageA_temp = None
imageB_temp = None
image_diff = None
image_diff_binary = None
imageC_temp = None
imageD_temp = None
image_diff_left = None
image_diff_left_binary = None

imageA = cv.imread('/home/pi/Documents/TD/photo/samba/photo_rotate_crop/crop_all/serie4_image0_right_crop_all.jpg')
imageB = cv.imread('/home/pi/Documents/TD/photo/samba/photo_rotate_crop/crop_all/serie4_image1_right_crop_all.jpg')
              
grayA = cv.cvtColor(imageA, cv.COLOR_BGR2GRAY)
grayB = cv.cvtColor(imageB, cv.COLOR_BGR2GRAY)
            
imageA_temp = cv.convertScaleAbs(grayA, imageA_temp, 0.5, 128);
imageB_temp = cv.convertScaleAbs(grayB, imageB_temp, 0.5, 0);
image_diff = cv.subtract(imageA_temp, imageB_temp);
image_diff_binary = ny.ndarray(image_diff.shape)
ny.copyto(image_diff_binary,image_diff);
for x in range(image_diff.shape[0]):
    for y in range(image_diff.shape[1]):
        if image_diff[x,y] != 128:
            image_diff_binary[x,y]=255
        else:
            image_diff_binary[x,y] = 0
cv.imwrite('/home/pi/Desktop/binary.jpg', image_diff_binary)
opening = cv.morphologyEx(image_diff_binary, cv.MORPH_OPEN, cv.getStructuringElement(cv.MORPH_RECT,(5,5)))
cv.imwrite('/home/pi/Desktop/binary_open.jpg', opening)

imageC = cv.imread('/home/pi/Documents/TD/photo/samba/photo_rotate_crop/crop_all/serie4_image0_right_crop_all.jpg')
imageD = cv.imread('/home/pi/Documents/TD/photo/samba/photo_rotate_crop/crop_all/serie4_image1_right_crop_all.jpg')
            
grayC = cv.cvtColor(imageC, cv.COLOR_BGR2GRAY)
grayD = cv.cvtColor(imageD, cv.COLOR_BGR2GRAY)
            
imageC_temp = cv.convertScaleAbs(grayC,imageC_temp, 0.5, 128);
imageD_temp = cv.convertScaleAbs(grayD, imageD_temp, 0.5, 0);
image_diff_left = cv.subtract(imageC_temp, imageD_temp);
image_diff_left_binary = ny.ndarray(image_diff_left.shape)
ny.copyto(image_diff_left_binary,image_diff_left);
for x in range(image_diff_left.shape[0]):
    for y in range(image_diff_left.shape[1]):
        if image_diff_left[x,y] != 128 :
            image_diff_left_binary[x,y] = 255
        else:
            image_diff_left_binary[x,y] = 0
cv.imwrite('/home/pi/Desktop/binary2.jpg', image_diff_left_binary)
opening_left = cv.morphologyEx(image_diff_left_binary, cv.MORPH_OPEN, cv.getStructuringElement(cv.MORPH_RECT,(5,5)))
cv.imwrite('/home/pi/Desktop/binary_open2.jpg', opening_left)

