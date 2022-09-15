import sys

from machine import Pin, PWM
from servo import Servo
import utime

pwmPin=0 #change for your pin
motor=Servo(pwmPin)

# motor.move(0) # move to 45 degrees
# utime.sleep(1)
# motor.move(90)


led = Pin(25, Pin.OUT)

position = 0

while True:
    
    data = sys.stdin.read(1)
    pippo = data[0]
    
    if pippo == "w":
        if position < 90:
            position += 10
        motor.move(position)
        
    else:
        if position > -90:
            position -= 10
        motor.move(position)

