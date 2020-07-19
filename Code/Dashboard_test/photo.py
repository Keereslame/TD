from picamera import PiCamera
from time import sleep

camera = PiCamera()

#sleep(10)
camera.start_preview()
for i in range(5):
    sleep(5)
    camera.capture('/home/pi/Documents/TD/photo/original/test3_vers_image%s.jpg' % i)    
camera.stop_preview()