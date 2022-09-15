# Author: peppe8o
# Blog: https://peppe8o.com
# Date: Jun 3st, 2021
# Version: 1.0

from machine import Pin, PWM
from time import sleep

servoPin = PWM(Pin(16))
servoPin.freq(50) # 50Hz
speed = 0.03

def servo(degrees):
    # limit degrees beteen 0 and 180
    if degrees > 180: degrees=180
    if degrees < 0: degrees=0
    
    # set max and min duty
    maxDuty=9000
    minDuty=1000
    
    # new duty is between min and max duty in proportion to its value
    newDuty=minDuty+(maxDuty-minDuty)*(degrees/180)
    
    # servo PWM value is set
    servoPin.duty_u16(int(newDuty))

servo(90)
sleep(1)
servo(110)
sleep(1)
servo(90)
sleep(1)
servo(110)
sleep(1)
servo(90)
sleep(1)
servo(110)
sleep(1)
servo(90)
sleep(1)
servo(110)
sleep(1)

# while True:
#   # start increasing loop
#   for degree in range(0,180,1):
#     servo(degree)
#     sleep(speed)
#     print("increasing -- "+str(degree))
#   
#   # start decreasing loop
#   for degree in range(180, 0, -1):
#     servo(degree)
#     sleep(speed)
#     print("decreasing -- "+str(degree))