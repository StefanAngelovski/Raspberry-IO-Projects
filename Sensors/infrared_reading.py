import RPi.GPIO as GPIO
import time

# Declare the sensor pin
sensor_pin = 14

# GPIO setup
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(sensor_pin, GPIO.IN)

try:
    while True:
        if GPIO.input(sensor_pin):
            # If no object is near
            print("No object detected")
            while GPIO.input(sensor_pin):
                time.sleep(0.2)
        else:
            # If an object is detected
            print("Object detected")
        time.sleep(0.1)  # Small delay to avoid excessive CPU usage

except KeyboardInterrupt:
    GPIO.cleanup()
