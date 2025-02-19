import RPi.GPIO as GPIO
import time

# Set up GPIO
SERVO_PIN = 18
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(SERVO_PIN, GPIO.OUT)

# Create PWM instance with 50Hz frequency
pwm = GPIO.PWM(SERVO_PIN, 50)
pwm.start(0)

def set_angle(angle):
    duty = angle / 18 + 2  # Convert angle to duty cycle
    GPIO.output(SERVO_PIN, True)
    pwm.ChangeDutyCycle(duty)
    time.sleep(1)  # Wait for the servo to reach the position
    GPIO.output(SERVO_PIN, False)
    pwm.ChangeDutyCycle(0)

try:
    while True:
        set_angle(0)    # Move to 0 degrees
        time.sleep(5)
        print("0")
        set_angle(90)   # Move to 90 degrees
        time.sleep(5)
        print("90")
        set_angle(180)  # Move to 180 degrees
        time.sleep(5)
        print("180")

except KeyboardInterrupt:
    pwm.stop()
    GPIO.cleanup()
