import numpy as np
import cv2 as cv

 
# read image as grey scale
image = cv.imread('/home/pi/Documents/TD/photo/samba/photo_split/serie4_image4_right.jpg')
# get image height, width
(h, w) = image.shape[:2]
# calculate the center of the image
center = (w / 2, h / 2)
 
angle = 3
 
scale = 1.0

# Perform the counter clockwise rotation holding at the center
# 90 degrees
M = cv.getRotationMatrix2D(center, angle, scale)
rotated = cv.warpAffine(image, M, (h, w))

# cv.imshow('Rotated',rotated)
# cv.waitKey(0) # waits until a key is pressed
# cv.destroyAllWindows() # destroys the window showing image

crop_image = rotated[0:int(h),60:int(w-60)]

cv.imwrite('/home/pi/Documents/TD/photo/samba/photo_split/serie4_image4_right_crop.jpg', crop_image)