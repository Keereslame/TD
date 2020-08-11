import numpy as ny
import cv2 as cv

nb_photo = 5
nb_series = 5
imageA_temp = None
imageB_temp = None
imageC_temp = None
imageD_temp = None
image_diff_left = None
image_diff_right = None
image_diff_left_binary = None
image_diff_right_binary = None

for i in range(nb_series):
    for j in range(nb_photo-1):

        imageA = cv.imread('/home/pi/Documents/TD/photo/samba/photo_rotate_crop/crop_all/serie{}'.format(i+1) + '_image{0}'.format(j) + '_right_crop_all.jpg')
        imageB = cv.imread('/home/pi/Documents/TD/photo/samba/photo_rotate_crop/crop_all/serie{}'.format(i+1) + '_image{0}'.format(j+1) + '_right_crop_all.jpg')
            
        grayA = cv.cvtColor(imageA, cv.COLOR_BGR2GRAY)
        grayB = cv.cvtColor(imageB, cv.COLOR_BGR2GRAY)
            
        imageA_temp = cv.convertScaleAbs(grayA,imageA_temp, 0.5, 128);
        imageB_temp = cv.convertScaleAbs(grayB, imageB_temp, 0.5, 0);
        image_diff_right = cv.subtract(imageA_temp, imageB_temp);
        cv.imwrite('/home/pi/Documents/TD/photo/samba/photo_diff/diff_avec_rotation_avec_perte/serie{0}'.format(i+1) + '_image{0}'.format(j) + '_diff_right.jpg', image_diff_right)
        image_diff_right_binary = ny.ndarray(image_diff_right.shape)
        ny.copyto(image_diff_right_binary,image_diff_right);
        for x in range(image_diff_right.shape[0]):
            for y in range(image_diff_right.shape[1]):
                if image_diff_right[x,y] != 128 :
                    image_diff_right_binary[x,y] = 255
                else:
                    image_diff_right_binary[x,y] = 0
        opening_right = cv.morphologyEx(image_diff_right_binary, cv.MORPH_OPEN, cv.getStructuringElement(cv.MORPH_RECT,(5,5)))
        cv.imwrite('/home/pi/Documents/TD/photo/samba/photo_diff/diff_avec_rotation_avec_perte/serie{0}'.format(i+1) + '_image{0}'.format(j) + '_diff_right_binary.jpg', opening_right)
        
        imageC = cv.imread('/home/pi/Documents/TD/photo/samba/photo_rotate_crop/crop_all/serie{0}'.format(i+1) + '_image{0}'.format(j) + '_left_crop_all.jpg')
        imageD = cv.imread('/home/pi/Documents/TD/photo/samba/photo_rotate_crop/crop_all/serie{0}'.format(i+1) + '_image{0}'.format(j+1) + '_left_crop_all.jpg')
            
        grayC = cv.cvtColor(imageC, cv.COLOR_BGR2GRAY)
        grayD = cv.cvtColor(imageD, cv.COLOR_BGR2GRAY)
            
        imageC_temp = cv.convertScaleAbs(grayC,imageC_temp, 0.5, 128);
        imageD_temp = cv.convertScaleAbs(grayD, imageD_temp, 0.5, 0);
        image_diff_left = cv.subtract(imageC_temp, imageD_temp);
        cv.imwrite('/home/pi/Documents/TD/photo/samba/photo_diff/diff_avec_rotation_avec_perte/serie{0}'.format(i+1) + '_image{0}'.format(j) + '_diff_left.jpg', image_diff_left)
        image_diff_left_binary = ny.ndarray(image_diff_left.shape)
        ny.copyto(image_diff_left_binary,image_diff_left);
        for x in range(image_diff_left.shape[0]):
            for y in range(image_diff_left.shape[1]):
                if image_diff_left[x,y] != 128 :
                    image_diff_left_binary[x,y] = 255
                else:
                    image_diff_left_binary[x,y] = 0
        opening_left = cv.morphologyEx(image_diff_left_binary, cv.MORPH_OPEN, cv.getStructuringElement(cv.MORPH_RECT,(5,5)))
        cv.imwrite('/home/pi/Documents/TD/photo/samba/photo_diff/diff_avec_rotation_avec_perte/serie{0}'.format(i+1) + '_image{0}'.format(j) + '_diff_left_binary.jpg', opening_left)
