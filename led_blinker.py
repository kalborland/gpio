import time
import RPi.GPIO as GPIO

bopunce_time = 200
GPIO.setmode(GPIO.BCM)

GPIO.setup(19, GPIO.OUT)

while 1:
    GPIO.output(19,0)

    if GPIO.input(19) == 0:
        GPIO.output(19, 1)
        time.sleep(1)
        GPIO.output(19, 0)
        time.sleep(1)
