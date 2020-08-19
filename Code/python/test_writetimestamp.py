import picamera 
import time
import datetime as dt

camera = picamera.PiCamera()
camera.start_preview()
for i in range(5):
    camera.annotate_background = picamera.Color('black')
    camera.annotate_text = dt.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    time.sleep(5)
    camera.capture('/home/pi/Documents/TD/photo/samba/photo_dashboard/serie{0}'.format(nb_series-1) + '_image{0}.jpg'.format(nb_photo-1))
camera.stop_preview()