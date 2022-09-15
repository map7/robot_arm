from machine import Pin, PWM
from time import sleep
from servo import Servo

pwmPin=0 #change for your pin
motor=Servo(pwmPin)
motor.move(-90) # move to 45 degrees
sleep(1)
motor.move(90)
