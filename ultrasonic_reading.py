import RPi.GPIO as GPIO
import time

# Pin configuration
TRIG = 14  # GPIO pin 14 for trigger
ECHO = 15  # GPIO pin 15 for echo

# GPIO setup
GPIO.setmode(GPIO.BCM)
GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)

# Function to measure distance
def get_distance():
    GPIO.output(TRIG, True)
    time.sleep(0.00001)  # Send a short pulse
    GPIO.output(TRIG, False)
    
    start_time = time.time()
    stop_time = time.time()
    
    timeout = time.time() + 0.1  # 100ms timeout to avoid infinite loop
    while GPIO.input(ECHO) == 0:
        start_time = time.time()
        if time.time() > timeout:
            return None  # Timeout occurred
    
    timeout = time.time() + 0.1  # Reset timeout for echo high
    while GPIO.input(ECHO) == 1:
        stop_time = time.time()
        if time.time() > timeout:
            return None  # Timeout occurred
    
    # Calculate distance
    elapsed_time = stop_time - start_time
    distance = (elapsed_time * 34300) / 2  # Speed of sound = 34300 cm/s
    
    return round(distance, 2)

try:
    while True:
        dist = get_distance()
        if dist is not None and 2 <= dist <= 400:  # Valid range for HC-SR04
            print(f"Distance: {dist} cm")
        else:
            print("Invalid measurement, ignoring...")
        time.sleep(0.01)  # 10ms delay
except KeyboardInterrupt:
    print("Measurement stopped by user")
    GPIO.cleanup()
