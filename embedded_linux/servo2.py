from gpiozero import Servo
from time import sleep

myGPIO = 19

myCorrection = 0
maxPW = (2.0 + myCorrection) / 1000
minPW = (1.0 + myCorrection) / 1000

servo = Servo(myGPIO, min_pulse_width=minPW, max_pulse_width=maxPW)

while True:
    
    print("Set value range -1.0 to +1.0")
    for i in range(0, 21):
        value = (float(i) - 10.0) / 10.0
        servo.value = value
        print("value: ", value)
        sleep(0.5)
        
    print ("Set value range +1.0 to -1.0")
    for i in range(20, -1, -1):
        value = (float(i) - 10.0) / 10.0
        servo.value = value
        print("value: ", value)
        sleep(0.5)