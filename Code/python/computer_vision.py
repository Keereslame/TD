import numpy as ny
import cv2 as cv
from picamera import PiCamera
from time import sleep
from skimage.measure import compare_ssim
import argparse
import imutils
import datetime

nb_photo = 0
nb_series = 0

def take_pictures():
    global nb_photo
    global nb_series
    nb_photo = 0
    camera = PiCamera()
    
    nb_series += 1
    camera.start_preview()
    
    for i in range(5):
        sleep(5)
        camera.capture('/home/pi/Documents/TD/photo/samba/photo_dashboard/serie{0}'.format(nb_series) + '_image{0}.jpg'.format(nb_photo))    
        nb_photo += 1
    camera.stop_preview()
    
def split():
    global nb_photo
    global nb_series
    for j in range(nb_photo):        
        img = cv2.imread('/home/pi/Documents/TD/photo/samba/photo_dashboard/serie{0}'.format(nb_series) + '_image{0}.jpg'.format(j))
        row = img.shape[0]
        col = img.shape[1]
        imCrop1 = img[0:int(row), 0:int(col/2)]
        imCrop2 = img[0:int(row), int(col/2)+1:int(col/2)*2]

        cv2.imwrite('/home/pi/Documents/TD/photo/samba/photo_split/serie{0}'.format(nb_series) + '_image{0}'.format(j) + '_left.jpg', imCrop1)
        cv2.imwrite('/home/pi/Documents/TD/photo/samba/photo_split/serie{0}'.format(nb_series) + '_image{0}'.format(j) + '_right.jpg', imCrop2)
        
def difference(path_imageA, path_imageB, side):
        # convert the images to grayscale
        grayA = cv2.cvtColor(imageA, cv2.COLOR_BGR2GRAY)
        grayB = cv2.cvtColor(imageB, cv2.COLOR_BGR2GRAY)
        
        # compute the Structural Similarity Index (SSIM) between the two
        # images, ensuring that the difference image is returned
        (score, diff) = compare_ssim(grayA, grayB, full=True)
        diff = (diff * 255).astype("uint8")
        #print("SSIM: {}".format(score))
        
        # threshold the difference image, followed by finding contours to
        # obtain the regions of the two input images that differ
        thresh = cv2.threshold(diff, 0, 255,
            cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]
        cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,
            cv2.CHAIN_APPROX_SIMPLE)
        cnts = imutils.grab_contours(cnts)
        
        cv2.imwrite('/home/pi/Documents/TD/photo/samba/photo_thresh/serie{0}'.format(nb_series) + '_image{0}'.format(j) + '_thresh' + side + '.jpg', thresh)
            
def difference_left():
    global nb_photo
    global nb_series
    for j in range(nb_photo-1):        
        # load the two input images
        imageA = cv.imread('/home/pi/Documents/TD/photo/samba/photo_split/serie{0}'.format(nb_series) + '_image{0}'.format(j) + '_left.jpg')
        imageB = cv.imread('/home/pi/Documents/TD/photo/samba/photo_split/serie{0}'.format(nb_series) + '_image{0}'.format(j+1) + '_left.jpg')
        
        difference(imageA, imageB, 'left')       
        
def difference_right():
    global nb_photo
    global nb_series
    for j in range(nb_photo-1):      
        # load the two input images
        imageA = cv.imread('/home/pi/Documents/TD/photo/samba/photo_split/serie{0}'.format(nb_series) + '_image{0}'.format(j) + '_right.jpg')
        imageB = cv.imread('/home/pi/Documents/TD/photo/samba/photo_split/serie{0}'.format(nb_series) + '_image{0}'.format(j+1) + '_right.jpg')
        
        difference(imageA, imageB, 'right')
        
def mouvement_left():
    
def mouvement_right():
    global nb_photo
    global nb_series
    nb_pixel_white = 0
    nb_pixel_black = 0
    for j in range(nb_photo-1):      
        # load the two input images
        image = cv.imread('/home/pi/Documents/TD/photo/samba/photo_thresh/serie{0}'.format(nb_series) + '_image{0}'.format(j) + '_right.jpg')
        row = image.shape[0]
        col = image.shape[1]
        for x in row:
            for y in col:
                if image[x,y] == 0:
                    print("wihte")
                else
                    print("black")
    
def write_timestamp():
    global nb_photo
    global nb_series
    camera = PiCamera()
    camera.start_preview()
    for i in range(5):
        camera.annotate_size = 120
        camera.annotate_foreground = Color('red')
        camera.annotate_background = Color('black')
        camera.annotate_text = str(datetime.datetime.now())
        sleep(5)
        camera.capture('/home/pi/Documents/TD/photo/samba/photo_dashboard/serie{0}'.format(nb_series-1) + '_image{0}.jpg'.format(nb_photo-1))    
        nb_photo += 1
    camera.stop_preview()

if __name__ == '__main__':
    take_pictures();
    split();
    difference_left();
    difference_right();
    mouvement_left();
    mouvement_right();
    write_timestamp();
    
    