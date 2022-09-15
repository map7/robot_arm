from machine import Pin, PWM
from servo import Servo
import utime

pwmPin=0 #change for your pin
motor=Servo(pwmPin)
# motor.move(0) # move to 45 degrees
# utime.sleep(1)
# motor.move(90)

 
analog_value = machine.ADC(28)

def translate(value, leftMin, leftMax, rightMin, rightMax):
    # Figure out how 'wide' each range is
    leftSpan = leftMax - leftMin
    rightSpan = rightMax - rightMin

    # Convert the left range into a 0-1 range (float)
    valueScaled = float(value - leftMin) / float(leftSpan)

    # Convert the 0-1 range into a value in the right range.
    return rightMin + (valueScaled * rightSpan)
 
while True:
    reading = analog_value.read_u16()     
    print("ADC: ",reading)
    utime.sleep(0.2)
    moving = translate(reading, 0, 65536, -90, 90)
    print(moving)
    motor.move(moving)      
   