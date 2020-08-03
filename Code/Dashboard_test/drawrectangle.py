import cv2 as cv
import numpy as np
import imutils

image = cv.imread('/home/pi/Documents/TD/photo/photo_test/test3_vers_image1.jpg')
gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
canimg = cv.Canny(gray, 50, 200)

lines = cv.HoughLines(canimg, 1, np.pi/180, 120, np.array([]))

for line in lines:
    rho, theta = line[0]
    a = np.cos(theta)
    b = np.sin(theta)
    
    x0 = a*rho
    y0 = b*rho
    
    x1 = int(x0+1000*(-b))
    y1 = int(y0 + 1000*(a))
    x2 = int(x0-1000*(-b))
    y2 = int(y0 - 1000*(1))
    
    cv.line(image, (x1, y1), (x2, y2), (0,0,255), 2)
    cv.line(image, (x1+950, y1),(x2+950, y2), (0,0,255), 2)
    
cv.imwrite('/home/pi/Documents/TD/photo/openCV/test1.jpg', image)
    
#cv.imshow('line detection', image)
#cv.imshow('cany detection', canimg)

img = cv.imread('/home/pi/Documents/TD/photo/openCV/test1.jpg')
imgray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)

# Converting image to a binary image  
# (black and white only image). 
_,threshold = cv.threshold(imgray, 100, 255,  
                            cv.THRESH_BINARY) 
   
# Detecting shapes in image by selecting region  
# with same colors or intensity. 
contours,_=cv.findContours(threshold, cv.RETR_TREE, 
                            cv.CHAIN_APPROX_SIMPLE) 

cv.imshow('test', threshold)
cv.waitKey(0)
cv.destroyAllWindows()