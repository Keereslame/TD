#Source : https://stackoverflow.com/questions/43892506/opencv-python-rotate-image-without-cropping-sides

import numpy as np
import cv2 as cv

nb_photo = 5
nb_series = 5


for i in range(nb_series):
    for j in range(nb_photo):
        """
        Rotates an image (angle in degrees) and expands image to avoid cropping
        """
        mat_left = cv.imread('/home/pi/Documents/TD/photo/samba/photo_split/serie{0}'.format(i+1) + '_image{0}'.format(j) + '_left.jpg')

        height, width = mat_left.shape[:2] # image shape has 3 dimensions
        image_center = (width/2, height/2) # getRotationMatrix2D needs coordinates in reverse order (width, height) compared to shape

        rotation_mat_left = cv.getRotationMatrix2D(image_center, 3, 1.)

        # rotation calculates the cos and sin, taking absolutes of those.
        abs_cos = abs(rotation_mat_left[0,0]) 
        abs_sin = abs(rotation_mat_left[0,1])

        # find the new width and height bounds
        bound_w = int(height * abs_sin + width * abs_cos)
        bound_h = int(height * abs_cos + width * abs_sin)

        # subtract old image center (bringing image back to origo) and adding the new image center coordinates
        rotation_mat_left[0, 2] += bound_w/2 - image_center[0]
        rotation_mat_left[1, 2] += bound_h/2 - image_center[1]

        # rotate image with the new bounds and translated rotation matrix
        rotation_mat_left = cv.warpAffine(mat_left, rotation_mat_left, (bound_w, bound_h))
        cv.imwrite('/home/pi/Documents/TD/photo/samba/photo_rotate_crop/crop_all/serie{0}'.format(i+1) + '_image{0}'.format(j)+ '_left_rotation.jpg', rotation_mat_left)

        crop_image_left = rotation_mat_left[40:int(height),120:int(width-30)]
        
        mat_right = cv.imread('/home/pi/Documents/TD/photo/samba/photo_split/serie{0}'.format(i+1) + '_image{0}'.format(j) + '_right.jpg')

        height_r, width_r = mat_right.shape[:2] # image shape has 3 dimensions
        image_center_r = (width_r/2, height_r/2) # getRotationMatrix2D needs coordinates in reverse order (width, height) compared to shape

        rotated_mat_right = cv.getRotationMatrix2D(image_center_r, 3, 1.)

        # rotation calculates the cos and sin, taking absolutes of those.
        abs_cos_r = abs(rotated_mat_right[0,0]) 
        abs_sin_r = abs(rotated_mat_right[0,1])

        # find the new width and height bounds
        bound_w_r = int(height_r * abs_sin_r + width_r * abs_cos_r)
        bound_h_r = int(height_r * abs_cos_r + width_r * abs_sin_r)

        # subtract old image center (bringing image back to origo) and adding the new image center coordinates
        rotated_mat_right[0, 2] += bound_w_r/2 - image_center_r[0]
        rotated_mat_right[1, 2] += bound_h_r/2 - image_center_r[1]

        # rotate image with the new bounds and translated rotation matrix
        rotated_mat_right = cv.warpAffine(mat_right, rotated_mat_right, (bound_w_r, bound_h_r))
        cv.imwrite('/home/pi/Documents/TD/photo/samba/photo_rotate_crop/crop_all/serie{0}'.format(i+1) + '_image{0}'.format(j)+ '_right_rotation.jpg', rotated_mat_right)
        
        crop_image_right = rotated_mat_right[40:int(height_r),60:int(width_r-60)]

#         cv.imshow('Crop left',crop_image_left)
#         cv.imshow('Crop right', crop_image_right)
#         cv.waitKey(0) # waits until a key is pressed
#         cv.destroyAllWindows() # destroys the window showing image
        cv.imwrite('/home/pi/Documents/TD/photo/samba/photo_rotate_crop/crop_all/serie{0}'.format(i+1) + '_image{0}'.format(j) + '_left_crop_all.jpg', crop_image_left)
        cv.imwrite('/home/pi/Documents/TD/photo/samba/photo_rotate_crop/crop_all/serie{0}'.format(i+1) + '_image{0}'.format(j) + '_right_crop_all.jpg', crop_image_right)