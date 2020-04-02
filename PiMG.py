import RPi.GPIO as GPIO
from picamera import picamera
from time import sleep

camera = PiCamera()

GPIO.setwarings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

counter = 0

camera.start_preview()

while 1==1:
    if GPIO.input(10) == GPIO.HIGH:
        print("Take a photo")
        if counter < 10:
            camera.capture('/home/pi/Desktop/obrazy/img0' + counter + '.jpg')
        else:
            camera.capture('/home/pi/Desktop/obrazy/img' + counter + '.jpg')
        counter +=1

camera.stop_preview()
