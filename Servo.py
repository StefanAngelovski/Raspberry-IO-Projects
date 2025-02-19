import RPi.GPIO as GPIO
import time

# Set up GPIO
SERVO_PIN = 18  # Change this to your GPIO pin
GPIO.setmode(GPIO.BCM)
GPIO.setup(SERVO_PIN, GPIO.OUT)

# Create PWM instance with 50Hz frequency
pwm = GPIO.PWM(SERVO_PIN, 50)
pwm.start(0)

try:
    # Spin clockwise (adjust duty cycle as needed)
    pwm.ChangeDutyCycle(5)   # ~1ms pulse (counter-clockwise at full speed)
    time.sleep(2)            # Run for 2 seconds (adjust for full rotation)
    
    # Spin counter-clockwise
    pwm.ChangeDutyCycle(10)  # ~2ms pulse (clockwise at full speed)
    time.sleep(2)            # Run for 2 seconds
    
finally:
    # Clean up
    pwm.stop()
    GPIO.cleanup()
