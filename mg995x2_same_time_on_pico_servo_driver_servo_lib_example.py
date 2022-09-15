from machine import Pin, PWM

class Servo:
    # these defaults work for the standard TowerPro SG90
    __servo_pwm_freq = 50
    __min_u16_duty = 1640 + 400 # offset for correction
    __max_u16_duty = 7864 - 35  # offset for correction
    min_angle = -90
    max_angle = 90    
    current_angle = 0.001
    
    def __init__(self, pin):
        self.__initialise(pin)
        
    def update_settings(self, servo_pwm_freq, min_u16_duty, max_u16_duty, min_angle, max_angle, pin):
        self.__servo_pwm_freq = servo_pwm_freq
        self.__min_u16_duty = min_u16_duty
        self.__max_u16_duty = max_u16_duty
        self.min_angle = min_angle
        self.max_angle = max_angle
        self.__initialise(pin)
        
    def move(self, angle):
        # round to 2 decimal places, so we have a chance of reducing unwanted servo adjustments
        angle = round(angle, 2)
        # do we need to move?
        if angle == self.current_angle:
            return
        self.current_angle = angle
        # calculate the new duty cycle and move the motor
        duty_u16 = self.__angle_to_u16_duty(angle)        
        self.__motor.duty_u16(duty_u16)
        
    def __angle_to_u16_duty(self, angle):
        return int((angle - self.min_angle) * self.__angle_conversion_factor) + self.__min_u16_duty
    
    def __initialise(self, pin):
        self.current_angle = -0.001
        self.__angle_conversion_factor = (self.__max_u16_duty - self.__min_u16_duty) / (self.max_angle - self.min_angle)
        self.__motor = PWM(Pin(pin))
        self.__motor.freq(self.__servo_pwm_freq)

#from servo import Servo
from time import sleep

pwm0Pin=0 #change for your pin
motor0=Servo(pwm0Pin)
pwm1Pin=1
motor1=Servo(pwm1Pin)

# Step back and forward loop
while True:
    sleep(1)
    motor0.move(0) # move to 45 degrees
    motor1.move(0)
    sleep(1)
    motor0.move(90)
    motor1.move(90)
    