from gpiozero import MotionSensor
from signal import pause

pir = MotionSensor(4)

while True:
    print("Continue scanning...")
    pir.wait_for_motion()

    print("Moving human detected!")
    pir.wait_for_no_motion()
    
    print("Motion stopped")
