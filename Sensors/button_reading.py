import RPi.GPIO as GPIO
from time import sleep

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)


Button = 14

GPIO.setup(Button,GPIO.IN, pull_up_down=GPIO.PUD_UP)

while True:
    button_state = GPIO.input(Button)
    if button_state == 0:
        print("Pressed")
    else:
        print("Not pressed")
    sleep(0.1)
