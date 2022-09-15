from servo import Servo

#from servo import Servo
from time import sleep

pwm0Pin=0 #change for your pin
motor0=Servo(pwm0Pin)
pwm1Pin=1
motor1=Servo(pwm1Pin)
pwm2Pin=2
motor2=Servo(pwm2Pin)
pwm3Pin=3
motor3=Servo(pwm3Pin)

# Step back and forward loop
while True:
    sleep(1)
    motor0.move(0) # move to 45 degrees
    motor1.move(0)
    motor2.move(0)
    motor3.move(0)
    sleep(1)
    motor0.move(90)
    motor1.move(90)
    motor2.move(90)
    motor3.move(90)
   