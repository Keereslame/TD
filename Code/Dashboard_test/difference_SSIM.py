# import the necessary packages
from skimage.metrics import structural_similarity
import cv2

nb_series = 5
nb_photo = 5

for i in range(nb_series):
    for j in range(nb_photo-1):
        # load the two input images
        imageA = cv2.imread('/home/pi/Documents/TD/photo/samba/photo_split/serie{0}'.format(i+1) + '_image{0}'.format(j) + '_left.jpg')
        imageB = cv2.imread('/home/pi/Documents/TD/photo/samba/photo_split/serie{0}'.format(i+1) + '_image{0}'.format(j+1) + '_left.jpg')
        # convert the images to grayscale
        grayA = cv2.cvtColor(imageA, cv2.COLOR_BGR2GRAY)
        grayB = cv2.cvtColor(imageB, cv2.COLOR_BGR2GRAY)

        # compute the Structural Similarity Index (SSIM) between the two
        # images, ensuring that the difference image is returned
        (score, diff) = structural_similarity(grayA, grayB, full=True)
        diff = (diff * 255).astype("uint8")
        print("SSIM: {}".format(score))

        # threshold the difference image, followed by finding contours to
        # obtain the regions of the two input images that differ
        thresh = cv2.threshold(diff, 210, 255,
            cv2.THRESH_BINARY_INV)[1]
#         cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,
#             cv2.CHAIN_APPROX_SIMPLE)
#         cnts = imutils.grab_contours(cnts)
        

        # loop over the contours
#         for c in cnts:
#             # compute the bounding box of the contour and then draw the
#             # bounding box on both input images to represent where the two
#             # images differ
#             (x, y, w, h) = cv2.boundingRect(c)
#             cv2.rectangle(imageA, (x, y), (x + w, y + h), (0, 0, 255), 2)
#             cv2.rectangle(imageB, (x, y), (x + w, y + h), (0, 0, 255), 2)
            
        # show the output images
        #cv2.imshow("Original", imageA)
        #cv2.imshow("Modified", imageB)
        #cv2.imshow("Diff", thresh)
        #cv2.imwrite('/home/pi/Documents/TD/photo/samba/photo_diff/ssim/diff_sans_modif/serie{0}'.format(i+1) + '_image{0}'.format(j) + '_left_tresh.jpg', thresh)
        
        # load the two input images
        imageC = cv2.imread('/home/pi/Documents/TD/photo/samba/photo_split/serie{0}'.format(i+1) + '_image{0}'.format(j) + '_right.jpg')
        imageD = cv2.imread('/home/pi/Documents/TD/photo/samba/photo_split/serie{0}'.format(i+1) + '_image{0}'.format(j+1) + '_right.jpg')
        # convert the images to grayscale
        grayC = cv2.cvtColor(imageC, cv2.COLOR_BGR2GRAY)
        grayD = cv2.cvtColor(imageD, cv2.COLOR_BGR2GRAY)

        # compute the Structural Similarity Index (SSIM) between the two
        # images, ensuring that the difference image is returned
        (score_r, diff_r) = structural_similarity(grayC, grayD, full=True)
        diff_r = (diff_r * 255).astype("uint8")
        print("SSIM: {}".format(score_r))

        # threshold the difference image, followed by finding contours to
        # obtain the regions of the two input images that differ
        thresh_r = cv2.threshold(diff_r, 210, 255,
            cv2.THRESH_BINARY_INV)[1]
#         cnts = cv2.findContours(thresh_r.copy(), cv2.RETR_EXTERNAL,
#             cv2.CHAIN_APPROX_SIMPLE)
#         cnts = imutils.grab_contours(cnts)

        # loop over the contours
#         for c in cnts:
#             # compute the bounding box of the contour and then draw the
#             # bounding box on both input images to represent where the two
#             # images differ
#             (x, y, w, h) = cv2.boundingRect(c)
#             cv2.rectangle(imageA, (x, y), (x + w, y + h), (0, 0, 255), 2)
#             cv2.rectangle(imageB, (x, y), (x + w, y + h), (0, 0, 255), 2)
            
        # show the output images
        #cv2.imshow("Original", imageA)
        #cv2.imshow("Modified", imageB)
        cv2.imshow("Diff", thresh)
        cv2.imshow("Diff", thresh_r)
#         cv2.imshow('diff', diff)
#         cv2.imshow('tresh', thresh)
#         cv2.imshow('diff_r', diff_r)
#         cv2.imshow('tresh_r', thresh_r)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        #cv2.imwrite('/home/pi/Documents/TD/photo/samba/photo_diff/ssim/diff_sans_modif/serie{0}'.format(i+1) + '_image{0}'.format(j) + '_right_tresh.jpg', thresh_r)
