from gpiozero import Button
from picamera import picamera
from time import sleep

camera = PiCamera()
button = Button(17)

frame = 1

camera.resolution = (1920, 1080)
camera.start_preview()

while True:
    try:
    button.wait_for_press()
        if counter < 10:
            camera.capture('/home/pi/Desktop/obrazy/img0' + counter + '.jpg')
        else:
            camera.capture('/home/pi/Desktop/obrazy/img' + counter + '.jpg')
        frame +=1
    except KeyboardInterrupt:
        camera.stop_preview()
        break