import numpy as np
import cv2

nb_series = 5
nb_photo = 5
for i in range(nb_series):
    for j in range(nb_photo):        
        img = cv2.imread('/home/pi/Documents/TD/photo/samba/photo_dashboard/serie{0}'.format(i+1) + '_image{0}'.format(j) +'.jpg')
        row = img.shape[0]
        col = img.shape[1]
        imCrop1 = img[0:int(row), 0:int(col/2)]
        imCrop2 = img[0:int(row), int(col/2)+1:int(col)]

        cv2.imwrite('/home/pi/Documents/TD/photo/samba/photo_split/serie{0}'.format(i+1) + '_image{0}'.format(j) + '_left.jpg', imCrop1)
        cv2.imwrite('/home/pi/Documents/TD/photo/samba/photo_split/serie{0}'.format(i+1) + '_image{0}'.format(j) + '_right.jpg', imCrop2)
