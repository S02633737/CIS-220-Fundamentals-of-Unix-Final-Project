#Standard Library Imports
from time import sleep

#Third Party Imports
from gpiozero import MotionSensor, LED

sensor = MotionSensor(4)
led = LED(17)

num = 0
while True:
    sensor.wait_for_motion()
    led.on()
    print("Alarm", num)
    num += 1
    sensor.wait_for_no_motion()
    led.off()
    #sleep(5)