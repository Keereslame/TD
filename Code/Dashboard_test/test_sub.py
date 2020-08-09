import cv2 as cv
import numpy as np

nb_photo = 5
nb_series = 1
imageA_temp = None
imageB_temp = None
image_diff = None
image_diff_binary = None 
for j in range(nb_photo-1):        
    # load the two input images
    imageA = cv.imread('/home/pi/Documents/TD/photo/samba/photo_split/serie{0}'.format(nb_series) + '_image{0}'.format(j) + '_left.jpg')
    imageB = cv.imread('/home/pi/Documents/TD/photo/samba/photo_split/serie{0}'.format(nb_series) + '_image{0}'.format(j) + '_right.jpg')
    
    grayA = cv.cvtColor(imageA, cv.COLOR_BGR2GRAY)
    grayB = cv.cvtColor(imageB, cv.COLOR_BGR2GRAY)
    
    imageA_temp = cv.convertScaleAbs(grayA,imageA_temp, 0.5, 128);
    cv.imwrite('/home/pi/Desktop/imageA_temp{0}'.format(j)+'.jpg', imageA_temp)
    imageB_temp = cv.convertScaleAbs(grayB, imageB_temp, 0.5, 0);
    cv.imwrite('/home/pi/Desktop/imageB_temp{0}'.format(j)+'.jpg', imageB_temp)
    image_diff = cv.subtract(imageA_temp, imageB_temp);
    image_diff_binary = np.ndarray(image_diff.shape)
    np.copyto(image_diff_binary,image_diff);
    cv.imwrite('/home/pi/Desktop/Substract{0}'.format(j)+'.jpg', image_diff)
    for x in range(image_diff.shape[0]):
        for y in range(image_diff.shape[1]):
            if image_diff[x,y] < 118:
                image_diff_binary[x,y] = 255
            elif image_diff[x,y] > 141:
                image_diff_binary[x,y] = 255
            else:
                image_diff_binary[x,y] = 0
                
    cv.imwrite('/home/pi/Desktop/Binary_diff{0}'.format(j)+'.jpg', image_diff_binary)
    retval, dst =cv.threshold(image_diff, 118, 255, cv.THRESH_BINARY_INV)
    cv.imwrite('/home/pi/Desktop/Thresh{0}'.format(j)+'.jpg', dst)

        
  