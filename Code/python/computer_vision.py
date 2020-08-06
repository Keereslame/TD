import numpy as ny
import cv2 as cv
import picamera 
from time import sleep
from skimage.measure import compare_ssim
import argparse
import imutils
import datetime as dt

nb_photo = 0
nb_series = 0
camera = None

def take_pictures():
    global nb_photo
    global nb_series
    nb_photo = 0
    global camera
    camera = picamera.PiCamera()
    
    camera.start_preview()
    nb_series += 1
    for i in range(5):
        sleep(5)
        camera.capture('/home/pi/Documents/TD/photo/samba/photo_dashboard/serie{0}'.format(nb_series) + '_image{0}.jpg'.format(nb_photo))    
        nb_photo += 1
    camera.stop_preview()
    
    
    
def split():
    global nb_photo
    global nb_series
    for j in range(nb_photo):        
        img = cv.imread('/home/pi/Documents/TD/photo/samba/photo_dashboard/serie{0}'.format(nb_series) + '_image{0}.jpg'.format(j))
        row = img.shape[0]
        col = img.shape[1]
        imCrop1 = img[0:int(row), 0:int(col/2)]
        imCrop2 = img[0:int(row), int(col/2):int(col/2)*2]

        cv.imwrite('/home/pi/Documents/TD/photo/samba/photo_split/serie{0}'.format(nb_series) + '_image{0}'.format(j) + '_left.jpg', imCrop1)
        cv.imwrite('/home/pi/Documents/TD/photo/samba/photo_split/serie{0}'.format(nb_series) + '_image{0}'.format(j) + '_right.jpg', imCrop2)
        
def difference(path_imageA, path_imageB, side, number):
    global nb_photo 
    global nb_series
    imageA_temp = None
    imageB_temp = None
    image_diff = None
    image_diff_binary = None 
    for j in range(nb_photo-1):           
        grayA = cv.cvtColor(path_imageA, cv.COLOR_BGR2GRAY)
        grayB = cv.cvtColor(path_imageB, cv.COLOR_BGR2GRAY)
    
        imageA_temp = cv.convertScaleAbs(grayA,imageA_temp, 0.5, 128);
        #cv.imwrite('/home/pi/Desktop/imageA_temp{0}'.format(j)+'.jpg', imageA_temp)
        imageB_temp = cv.convertScaleAbs(grayB, imageB_temp, 0.5, 0);
        #cv.imwrite('/home/pi/Desktop/imageB_temp{0}'.format(j)+'.jpg', imageB_temp)
        image_diff = cv.subtract(imageA_temp, imageB_temp);
        image_diff_binary = ny.ndarray(image_diff.shape)
        ny.copyto(image_diff_binary,image_diff);
        #cv.imwrite('/home/pi/Desktop/Substract{0}'.format(j)+'.jpg', image_diff)
        for x in range(image_diff.shape[0]):
            for y in range(image_diff.shape[1]):
                if image_diff[x,y] < 118:
                    image_diff_binary[x,y] = 255
                elif image_diff[x,y] > 141:
                    image_diff_binary[x,y] = 255
                else:
                    image_diff_binary[x,y] = 0
                
        cv.imwrite('/home/pi/Documents/TD/photo/samba/photo_thresh/serie{0}'.format(nb_series) + '_image{0}'.format(number) + '_thresh' + side + '.jpg', image_diff_binary)
                    
def difference_left():
    global nb_photo
    global nb_series
    for j in range(nb_photo-1):        
        # load the two input images
        imageA = cv.imread('/home/pi/Documents/TD/photo/samba/photo_split/serie{0}'.format(nb_series) + '_image{0}'.format(j) + '_left.jpg')
        imageB = cv.imread('/home/pi/Documents/TD/photo/samba/photo_split/serie{0}'.format(nb_series) + '_image{0}'.format(j+1) + '_left.jpg')
        
        difference(imageA, imageB, 'left', j)       
        
def difference_right():
    global nb_photo
    global nb_series
    for j in range(nb_photo-1):      
        # load the two input images
        imageA = cv.imread('/home/pi/Documents/TD/photo/samba/photo_split/serie{0}'.format(nb_series) + '_image{0}'.format(j) + '_right.jpg')
        imageB = cv.imread('/home/pi/Documents/TD/photo/samba/photo_split/serie{0}'.format(nb_series) + '_image{0}'.format(j+1) + '_right.jpg')
        
        difference(imageA, imageB, 'right', j)
        
def mouvement_left():
    global nb_photo
    global nb_series
    nb_pixel_white = 0
    nb_pixel_black = 0
    total_pixel = 0
    pourcent_per_image = 0
    max_pourcent = 0
    min_pourcent = 1
    for j in range(nb_photo-1):
        nb_pixel_white = 0
        nb_pixel_black = 0
        total_pixel = 0
        pourcent_per_image = 0
        # load the two input images
        image = cv.imread('/home/pi/Documents/TD/photo/samba/photo_thresh/serie{0}'.format(nb_series) + '_image{0}'.format(j) + '_threshleft.jpg', cv.COLOR_BGR2GRAY)
        row = image.shape[0]
        col = image.shape[1]
        for x in range(row):
            for y in range(col):
                if image[x,y] == 0:
                    nb_pixel_black+=1
                else:
                    nb_pixel_white+=1
        total_pixel = image.size
        pourcent_per_image = nb_pixel_white/total_pixel;
        if pourcent_per_image > max_pourcent:
            max_pourcent = pourcent_per_image
        if pourcent_per_image < min_pourcent:
            min_pourcent = pourcent_per_image
    
    print(str(max_pourcent*100) + '%')
    print(str(min_pourcent*100) + '%')
    
def mouvement_right():
#     global nb_photo
#     global nb_series
    nb_photo = 5
    nb_series = 1
    nb_pixel_white = 0
    nb_pixel_black = 0
    total_pixel = 0
    pourcent_per_image = 0
    max_pourcent = 0
    min_pourcent = 1
    for j in range(nb_photo-1):
        nb_pixel_white = 0
        nb_pixel_black = 0
        total_pixel = 0
        pourcent_per_image = 0
        # load the two input images
        image = cv.imread('/home/pi/Documents/TD/photo/samba/photo_thresh/serie{0}'.format(nb_series) + '_image{0}'.format(j) + '_threshright.jpg', cv.COLOR_BGR2GRAY)
        row = image.shape[0]
        col = image.shape[1]
        for x in range(row):
            for y in range(col):
                if image[x,y] == 0:
                    nb_pixel_black+=1
                else:
                    nb_pixel_white+=1
        total_pixel = image.size
        pourcent_per_image = nb_pixel_white/total_pixel
        if pourcent_per_image > max_pourcent:
            max_pourcent = pourcent_per_image
        if pourcent_per_image < min_pourcent:
            min_pourcent = pourcent_per_image
    
    print(str(max_pourcent*100) + '%')
    print(str(min_pourcent*100) + '%')
    
    
def write_timestamp():
    global nb_photo
    global nb_series
    global camera
#    camera = PiCamera()
    camera.start_preview()
    for i in range(5):
        camera.annotate_background = picamera.Color('black')
        camera.annotate_text = dt.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        sleep(5)
        camera.capture('/home/pi/Documents/TD/photo/samba/photo_dashboard/serie{0}'.format(nb_series) + '_image{0}.jpg'.format(nb_photo-5))
        nb_photo+=1
    camera.stop_preview()

if __name__ == '__main__':
    date_start = dt.datetime.now()
    print('Take pictures')
    take_pictures();
    print('split')
    split();
    print('Difference left')
    difference_left();
    print('Difference right')
    difference_right();
    print('mouvement left')
    mouvement_left();
    print('mouvement right')
    mouvement_right();
    print('Timestamp')
    write_timestamp();
    date_end = dt.datetime.now()
    print(date_end - date_start)
    
    