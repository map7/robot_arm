# import machine
# import time
# button = machine.Pin(0, machine.Pin.IN, machine.Pin.PULL_UP)
# 
# while True:
#     first = button.value()
#     time.sleep(0.01)
#     second = button.value()
#     if first and not second:
#         print('Button pressed!')
#     elif not first and second:
#         print('Button released!')
# 
# from ir_rx.test import test
# test()
from servo import Servo
import time
from machine import Pin
from ir_rx.nec import NEC_8  # NEC remote, 8 bit addresses

def free(self):
  self.__motor.duty_u16(0)

movementsArr = []

lastData = 0

pwm0Pin=0 #change for your pin
base=Servo(pwm0Pin)
basePos=0
base.move(basePos)

pwm1Pin=1 #change for your pin
thick=Servo(pwm1Pin)
thickPos=20
thick.move(thickPos)

pwm3Pin=3 
claw=Servo(pwm3Pin)
clawPos=-53
claw.move(clawPos)

time.sleep(0.4)
free(claw)
free(thick)
free(base)

def callback(data, addr, ctrl):
  global movementsArr, basePos, thickPos, clawPos, lastData
  
  if data < 0:
    data = lastData
  
  if data > 0:  # NEC protocol sends repeat codes.
    print('Data {:02x}'.format(data))
    if data == 0x13:
        print("RESET")
        basePos = 0
        base.move(basePos)
        thickPos = 20
        thick.move(20)
        claw.move(-53)
    elif data == 0x0c:
        print("UP")
        thickPos = thickPos + 10
        thick.move(thickPos)
    elif data == 0x10:
        print("DOWN")
        thickPos = thickPos - 10
        thick.move(thickPos)
    elif data == 0x08:
        print("LEFT")
        if basePos > -90:
          basePos = basePos - 10
          base.move(basePos)
    elif data == 0x04:
        print("RIGHT")
        if basePos < 90:
          basePos = basePos + 10
          base.move(basePos)
    elif data == 0x5b:
        print("OPEN")
        claw.move(50)
        clawPos = 50
    elif data == 0x5f:
        print("CLOSE")
        claw.move(-53)
        clawPos = -53
       
    movements = {"base": basePos, "thick": thickPos, "claw": clawPos}
    print(f'movements={movements}')

    movementsArr.append(movements)
    print(f'Array={len(movementsArr)}')
    
    time.sleep(0.4)
    free(claw)
    free(base)
    free(thick)
    lastData = data
    
ir = NEC_8(Pin(16, Pin.IN), callback)