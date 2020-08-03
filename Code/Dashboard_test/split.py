import numpy as np
import cv2

nb_test = 3
nb_photo = 5
for i in range(nb_test):
    for j in range(nb_photo):
        path1 = '/home/pi/Documents/TD/photo/photo_test/test{0}_vers_'.format(i+1)
        path2 = 'image{0}.jpg'.format(j)
        print(path1+path2)
        
        img = cv2.imread(path1+path2)
        row = img.shape[0]
        col = img.shape[1]
        imCrop1 = img[0:int(row), 0:int(col/2)]
        imCrop2 = img[0:int(row), int(col/2)+1:int(col/2)*2]

        pathCrop1_1 = path1
        pathCrop1_2 = 'image{0}'.format(j) + '_1.jpg'
        pathCrop2_1 = path1
        pathCrop2_2 = 'image{0}'.format(j) + '_2.jpg'
        cv2.imwrite(pathCrop1_1 + pathCrop1_2, imCrop1)
        cv2.imwrite(pathCrop2_1 + pathCrop2_2, imCrop2)


#cv2.waitKey(0)
#cv2.destroyAllWindows()