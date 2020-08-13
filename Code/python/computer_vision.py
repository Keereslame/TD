import numpy as ny
import cv2 as cv
import picamera 
from time import sleep
from skimage.metrics import structural_similarity
import datetime as dt
from influxdb import InfluxDBClient

#Global variables
nb_photo = 5
camera = None

def take_pictures():
    global nb_photo
    nb_photo = 0
    global camera
    camera = picamera.PiCamera()
    
    camera.start_preview()
    nb_series += 1
    for i in range(5):
        sleep(5)
        camera.capture('/home/pi/Documents/TD/photo/samba/photo/image{0}.jpg'.format(nb_photo))    
        nb_photo += 1
    camera.stop_preview()
    
def split():
    global nb_photo
    for j in range(nb_photo):        
        img = cv.imread('/home/pi/Documents/TD/photo/samba/photo/image{0}.jpg'.format(j))
        row = img.shape[0]
        col = img.shape[1]
        imCrop1 = img[0:int(row), 0:int(col/2)]
        imCrop2 = img[0:int(row), int(col/2):int(col)]

        cv.imwrite('/home/pi/Documents/TD/photo/samba/photo_split/image{0}'.format(j) + '_left.jpg', imCrop1)
        cv.imwrite('/home/pi/Documents/TD/photo/samba/photo_split/image{0}'.format(j) + '_right.jpg', imCrop2)

#Source : https://stackoverflow.com/questions/43892506/opencv-python-rotate-image-without-cropping-sides
def rotate_crop():
    global nb_photo
    for j in range(nb_photo):
        """
        Rotates an image (angle in degrees) and expands image to avoid cropping
        """
        mat_left = cv.imread('/home/pi/Documents/TD/photo/samba/photo_split/image{0}'.format(j) + '_left.jpg')

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
        cv.imwrite('/home/pi/Documents/TD/photo/samba/photo_rotate_crop/crop_all/image{0}'.format(j)+ '_left_rotation.jpg', rotation_mat_left)
        new_height, new_width = rotation_mat_left.shape[:2]
        crop_image_left = rotation_mat_left[40:int(new_height-40),120:int(new_width-80)]
        
        mat_right = cv.imread('/home/pi/Documents/TD/photo/samba/photo_split/image{0}'.format(j) + '_right.jpg')

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
        cv.imwrite('/home/pi/Documents/TD/photo/samba/photo_rotate_crop/crop_all/image{0}'.format(j)+ '_right_rotation.jpg', rotated_mat_right)
        new_height_r, new_width_r = rotated_mat_right.shape[:2]
        crop_image_right = rotated_mat_right[40:int(new_height_r-40),60:int(new_width_r-130)]

        cv.imwrite('/home/pi/Documents/TD/photo/samba/photo_rotate_crop/crop_all/image{0}'.format(j) + '_left_crop_all.jpg', crop_image_left)
        cv.imwrite('/home/pi/Documents/TD/photo/samba/photo_rotate_crop/crop_all/image{0}'.format(j) + '_right_crop_all.jpg', crop_image_right)
        
def difference_subtract(path_imageA, path_imageB, side, number):
    imageA_temp = None
    imageB_temp = None
    image_diff = None
    image_diff_binary = None 
              
    grayA = cv.cvtColor(path_imageA, cv.COLOR_BGR2GRAY)
    grayB = cv.cvtColor(path_imageB, cv.COLOR_BGR2GRAY)
            
    imageA_temp = cv.convertScaleAbs(grayA, imageA_temp, 0.5, 128);
    imageB_temp = cv.convertScaleAbs(grayB, imageB_temp, 0.5, 0);
    image_diff = cv.subtract(imageA_temp, imageB_temp);
    cv.imwrite('/home/pi/Documents/TD/photo/samba/photo_diff/subtract/diff_avec_rotation_avec_perte/image{0}'.format(number) + '_diff_'+ side+'.jpg', image_diff_right)
    image_diff_binary = ny.ndarray(image_diff.shape)
    ny.copyto(image_diff_binary,image_diff);
    for x in range(image_diff.shape[0]):
        for y in range(image_diff.shape[1]):
            if image_diff[x,y] != 128 :
                image_diff_binary[x,y] = 255
            else:
                image_diff_binary[x,y] = 0
    opening = cv.morphologyEx(image_diff_binary, cv.MORPH_OPEN, cv.getStructuringElement(cv.MORPH_RECT,(5,5)))
    cv.imwrite('/home/pi/Documents/TD/photo/samba/photo_diff/subtract/diff_avec_rotation_avec_perte/image{0}'.format(number) + '_diff_'+ side+'_binary.jpg', opening)
                    
def difference_left():
    global nb_photo
    for j in range(nb_photo-1):        
        # load the two input images
        imageA = cv.imread('/home/pi/Documents/TD/photo/samba/photo_rotate_crop/crop_all/image{0}'.format(j) + '_left_crop_all.jpg')
        imageB = cv.imread('/home/pi/Documents/TD/photo/samba/photo_rotate_crop/crop_all/image{0}'.format(j+1) + '_left_crop_all.jpg')
        
        difference_subtract(imageA, imageB, 'left', j)       
        
def difference_right():
    global nb_photo
    for j in range(nb_photo-1):      
        # load the two input images
        imageA = cv.imread('/home/pi/Documents/TD/photo/samba/photo_rotate_crop/crop_all/image{0}'.format(j) + '_right_crop_all.jpg')
        imageB = cv.imread('/home/pi/Documents/TD/photo/samba/photo_rotate_crop/crop_all/image{0}'.format(j+1) + '_right_crop_all.jpg')
        
        difference_subtract(imageA, imageB, 'right', j)
        
def difference_ssim():
    global nb_photo
    for j in range(nb_photo-1):
        # load the two input images
        imageA = cv.imread('/home/pi/Documents/TD/photo/samba/photo_rotate_crop/crop_all/image{0}'.format(j) + '_left_crop_all.jpg')
        imageB = cv.imread('/home/pi/Documents/TD/photo/samba/photo_rotate_crop/crop_all/image{0}'.format(j+1) + '_left_crop_all.jpg')
        # convert the images to grayscale
        grayA = cv.cvtColor(imageA, cv.COLOR_BGR2GRAY)
        grayB = cv.cvtColor(imageB, cv.COLOR_BGR2GRAY)

        # compute the Structural Similarity Index (SSIM) between the two
        # images, ensuring that the difference image is returned
        (score, diff) = structural_similarity(grayA, grayB, full=True)
        diff = (diff * 255).astype("uint8")
        cv.imwrite('/home/pi/Documents/TD/photo/samba/photo_diff/ssim/diff_avec_rotation_avec_perte/image{0}'.format(j) + '_left_ssim.jpg', diff)
        #print("SSIM: {}".format(score))

        # threshold the difference image, followed by finding contours to
        # obtain the regions of the two input images that differ
        thresh = cv.threshold(diff, 210, 255,
            cv.THRESH_BINARY_INV)[1]

        cv.imwrite('/home/pi/Documents/TD/photo/samba/photo_diff/ssim/diff_avec_rotation_avec_perte/image{0}'.format(j) + '_left_tresh.jpg', thresh)
        
        # load the two input images
        imageC = cv.imread('/home/pi/Documents/TD/photo/samba/photo_rotate_crop/crop_all/image{0}'.format(j) + '_right_crop_all.jpg')
        imageD = cv.imread('/home/pi/Documents/TD/photo/samba/photo_rotate_crop/crop_all/image{0}'.format(j+1) + '_right_crop_all.jpg')
        # convert the images to grayscale
        grayC = cv.cvtColor(imageC, cv.COLOR_BGR2GRAY)
        grayD = cv.cvtColor(imageD, cv.COLOR_BGR2GRAY)

        # compute the Structural Similarity Index (SSIM) between the two
        # images, ensuring that the difference image is returned
        (score_r, diff_r) = structural_similarity(grayC, grayD, full=True)
        diff_r = (diff_r * 255).astype("uint8")
                cv.imwrite('/home/pi/Documents/TD/photo/samba/photo_diff/ssim/diff_avec_rotation_avec_perte/image{0}'.format(j) + '_right_ssim.jpg', diff_r)

        #print("SSIM: {}".format(score_r))

        # threshold the difference image, followed by finding contours to
        # obtain the regions of the two input images that differ
        thresh_r = cv.threshold(diff_r, 210, 255,
            cv.THRESH_BINARY_INV)[1]
        
        cv.imwrite('/home/pi/Documents/TD/photo/samba/photo_diff/ssim/diff_avec_rotation_avec_perte/image{0}'.format(j) + '_right_tresh.jpg', thresh_r)
        
def movement(method, side):
    global nb_photo
    nb_pixel_white = 0
    nb_pixel_black = 0
    total_pixel = 0
    percent_per_image = 0
    total_percent = 0
    average_percent = 0
    measurement = ""
    path = ''
    for j in range(nb_photo-1):
        nb_pixel_white = 0
        nb_pixel_black = 0
        total_pixel = 0
        pourcent_per_image = 0
        # load the two input image_rights
        if method == 'ssim':
            path = '/home/pi/Documents/TD/photo/samba/photo_diff/subtract/diff_avec_rotation_avec_perte/image{0}'.format(j) + '_{0}'.format(side) + '_tresh.jpg'
        if method == 'subtract':
            path = '/home/pi/Documents/TD/photo/samba/photo_diff/subtract/diff_avec_rotation_avec_perte/image{0}'.format(j) + '_diff_'+ side+'_binary.jpg'
        image = cv.imread(path, cv.COLOR_BGR2GRAY)
        row = image.shape[0]
        col = image.shape[1]
        for x in range(row):
            for y in range(col):
                if image[x,y] == 0:
                    nb_pixel_black+=1
                else:
                    nb_pixel_white+=1
        total_pixel = image.size
        percent_per_image = nb_pixel_white/total_pixel
        total_percent += (percent_per_image*100)
        #print(method + side + 'percent_per_image' + str(percent_per_image*100))
        #print(method + side + 'total_percent' + str(total_percent))
        print('serie{0}'.format(i) + '_image{0}'.format(j) + '_{0}'.format(side) +str(pourcent_per_image_right*100))
    average_percent = total_percent/(nb_photo-1)
    #print(method + side + 'average_percent' + str(average_percent))
#     if method == 'ssim':
#         measurement = "movement_ssim";
#     if method == 'subtract':
#         measurement = "movement_subtract";
#             
#     json_body = [
#     {
#         "measurement": measurement,
#         "tags": {
#         },
#         #"time": int(seconds)-7200,
#         "fields": {
#             side: average_percent,
#         }
#     }
#     ]
#     if len(json_body) != 0:
#         sendData = client.write_points(json_body, 'n', 'lowimpact_food')
    
    
def write_timestamp():
    global camera
#    camera = PiCamera()
    camera.start_preview()
    camera.annotate_background = picamera.Color('black')
    date = dt.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    camera.annotate_text = date
    sleep(5)
    camera.capture('/home/pi/Documents/TD/photo/samba/photo_dashboard/dashboard'+date+'.jpg')
    camera.stop_preview()
    image = cv.imread('/home/pi/Documents/TD/photo/samba/photo_dashboard/dashboard'+date+'.jpg')
    cv.imwrite('/var/www/html/TD/dashboard.jpg', image)
    

if __name__ == '__main__':
    client = InfluxDBClient(host='localhost', port=8086)
    date_start = dt.datetime.now()
#     print('Take pictures')
#     take_pictures();
    print('split')
    split();
    print('Crop and rotate')
    rotate_crop();
    print('Difference left')
    difference_left();
    print('Difference right')
    difference_right();
    print('Differenc ssim')
    difference_ssim();
    print('mouvement subtract left')
    movement('subtract', 'left');
    print('mouvement subtract right')
    movement('subtract', 'right');
    print('mouvement ssim left')
    movement('ssim', 'left');
    print('mouvement ssim right')
    movement('ssim', 'right');
#     print('Timestamp')
#     write_timestamp();
    date_end = dt.datetime.now()
    print(date_end - date_start)
    
    