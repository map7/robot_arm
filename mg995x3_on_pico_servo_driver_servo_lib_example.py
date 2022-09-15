from servo import Servo
from time import sleep
from machine import Pin, PWM


pwm0Pin=0 #change for your pin
motor0=Servo(pwm0Pin) # Base
pwm1Pin=1
motor1=Servo(pwm1Pin) # Thick Arm
pwm2Pin=2
motor2=Servo(pwm2Pin) # Thin Arm
pwm3Pin=3
motor3=Servo(pwm3Pin) # Claw

# # Base motor (-90 to 90)
# sleep(1)
# motor0.move(-90)
# sleep(2)
# motor0.move(90)
# sleep(2)
# motor0.move(0)
#  
# # Think Arm
# # 
# # Think arm work out
# direction = 1
# count = 0
# 
# while 1:
#     if count == 90 and direction == 1:
#         direction = -1
#     elif count == -75:
#         direction = 1
# 
#     if direction == 1:
#         count = count + 1
#     else:
#         count = count - 1
#         
#     print(count)
#     motor1.move(count)
#     motor2.move(count)
#     sleep(0.01)

motor1.move(20)
motor2.move(80)
sleep(2)
motor1.free()
motor2.free()

# count = -90
# 
# while count < 90:
#     print(count)
#     motor2.move(count)
#     sleep(0.05)
#     count = count + 1

# sleep(1)
# motor1.move(90)
# sleep(1)
# motor1.move(20)
# sleep(1)

# # Thin Arm (50 to 100 @ main arm 0)
# # NOTE: I've got a problem here with noise
# motor2.move(30)
# sleep(1)

# # Claw (50 to -53[close])

# motor3.move(-53)
# sleep(1)
# motor3.move(-53)
# sleep(1)
# motor1.move(90)
# motor2.move(90)
# motor3.move(90)
   
