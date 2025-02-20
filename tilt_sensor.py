import RPi.GPIO as GPIO
from time import sleep


sensorPin = 14
GPIO.setmode(GPIO.BCM)
GPIO.setup(sensorPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

try:
    while True:
        print(GPIO.input(sensorPin))
        sleep(0.1)
except KeyboardInterrupt:
    GPIO.cleanup()
