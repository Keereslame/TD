import cv2 as cv
from skimage.metrics import structural_similarity

nb_series=5
nb_photo=5
for i in range(nb_series):
    for j in range(nb_photo-1):
        
        # load the two input images
        imageC = cv.imread('/home/pi/Documents/TD/photo/samba/photo_rotate_crop/crop_all/serie{}'.format(i+1) + '_image{0}'.format(j) + '_right_crop_all.jpg')
        imageD = cv.imread('/home/pi/Documents/TD/photo/samba/photo_rotate_crop/crop_all/serie{}'.format(i+1) + '_image{0}'.format(j+1) + '_right_crop_all.jpg')
            
         # convert the images to grayscale
        grayC = cv.cvtColor(imageC, cv.COLOR_BGR2GRAY)
        grayD = cv.cvtColor(imageD, cv.COLOR_BGR2GRAY)

        # compute the Structural Similarity Index (SSIM) between the two
        # images, ensuring that the difference image is returned
        (score_r, diff_r) = structural_similarity(grayC, grayD, full=True)
        diff_r = (diff_r * 255).astype("uint8")
        cv.imwrite('/home/pi/Documents/TD/photo/samba/photo_diff/ssim/diff_avec_rotation_avec_perte/serie{0}'.format(i+1)+'_image{0}'.format(j) + '_right_ssim.jpg', diff_r)
        
        # threshold the difference image, followed by finding contours to
        # obtain the regions of the two input images that differ
        thresh = cv.threshold(diff_r, 210, 255,
            cv.THRESH_BINARY_INV)[1]
        
        cv.imwrite('/home/pi/Documents/TD/photo/samba/photo_diff/ssim/diff_avec_rotation_avec_perte/serie{0}'.format(i+1)+'_image{0}'.format(j) + '_right_tresh.jpg', thresh)
