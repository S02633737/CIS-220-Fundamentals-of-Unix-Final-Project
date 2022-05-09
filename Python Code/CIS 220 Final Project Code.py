#Standard Library Imports
from time import sleep

#Third Party Imports
from gpiozero import MotionSensor, LED, TonalBuzzer

sensor = MotionSensor(4)
led = LED(17)
buzzer = TonalBuzzer(26)

num = 0
while True:
    sensor.wait_for_motion()
    led.on()
    buzzer.play("C4")
    print("Alarm", num)
    num += 1
    sensor.wait_for_no_motion()
    led.off()
    buzzer.stop()
    #sleep(5)
