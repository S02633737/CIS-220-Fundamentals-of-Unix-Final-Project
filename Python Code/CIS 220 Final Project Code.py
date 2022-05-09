#Standard Library Imports
from time import sleep

#Third Party Imports
from gpiozero import MotionSensor

sensor = MotionSensor(4)

num = 0
while True:
    sensor.wait_for_motion()
    print("Alarm", num)
    num += 1
    sleep(1)