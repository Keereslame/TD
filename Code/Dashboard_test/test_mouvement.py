import cv2 as cv

nb_photo = 5
nb_series = 5
nb_pixel_white_right = 0
nb_pixel_black_right = 0
total_pixel_right = 0
pourcent_per_image_right = 0
nb_pixel_white_left = 0
nb_pixel_black_left = 0
total_pixel_left = 0
pourcent_per_image_left = 0

for i in range(nb_series):
    for j in range(nb_photo-1):
        nb_pixel_white_right = 0
        nb_pixel_black_right = 0
        total_pixel_right = 0
        pourcent_per_image_right = 0
        # load the two input image_rights
        image_right = cv.imread('/home/pi/Documents/TD/photo/samba/photo_diff/serie{0}'.format(i+1) + '_image{0}'.format(j) +'_diff_right_binary.jpg', cv.COLOR_BGR2GRAY)
        row = image_right.shape[0]
        col = image_right.shape[1]
        for x in range(row):
            for y in range(col):
                if image_right[x,y] == 0:
                    nb_pixel_black_right+=1
                else:
                    nb_pixel_white_right+=1
        total_pixel_right = image_right.size
        pourcent_per_image_right = nb_pixel_white_right/total_pixel_right
        # if pourcent_per_image_right > max_pourcent:
        #     max_pourcent = pourcent_per_image_right
        # if pourcent_per_image_right < min_pourcent:
        #     min_pourcent = pourcent_per_image_right
        #     
        # print(str(max_pourcent*100) + '%')
        # print(str(min_pourcent*100) + '%')
        print('serie{0}'.format(i) + '_image{0}'.format(j) + '_right: ' +str(pourcent_per_image_right*100))
        
        nb_pixel_white_left = 0
        nb_pixel_black_left = 0
        total_pixel_left = 0
        pourcent_per_image_left = 0
        # load the two input image_rights
        image_left = cv.imread('/home/pi/Documents/TD/photo/samba/photo_diff/serie{0}'.format(i+1) + '_image{0}'.format(j) +'_diff_left_binary.jpg', cv.COLOR_BGR2GRAY)
        row = image_left.shape[0]
        col = image_left.shape[1]
        for x in range(row):
            for y in range(col):
                if image_left[x,y] == 0:
                    nb_pixel_black_left+=1
                else:
                    nb_pixel_white_left+=1
        total_pixel_left = image_left.size
        pourcent_per_image_left = nb_pixel_white_left/total_pixel_left
        # if pourcent_per_image_right > max_pourcent:
        #     max_pourcent = pourcent_per_image_right
        # if pourcent_per_image_right < min_pourcent:
        #     min_pourcent = pourcent_per_image_right
        #     
        # print(str(max_pourcent*100) + '%')
        # print(str(min_pourcent*100) + '%')
        print('serie{0}'.format(i) + '_image{0}'.format(j) + '_left: ' +str(pourcent_per_image_left*100))
