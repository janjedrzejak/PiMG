import RPi.GPIO as GPIO

GPIO.setwarings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

if GPIO.input(10) == GPIO.HIGH:
    print("Take a photo")
