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
import ujson
from machine import Pin
from ir_rx.nec import NEC_8  # NEC remote, 8 bit addresses

def free(self):
  self.__motor.duty_u16(0)

movementsArr = []
lastData = 0
record = 0

pwm0Pin=0
base=Servo(pwm0Pin)
basePos=0
base.move(basePos)

pwm1Pin=1
thick=Servo(pwm1Pin)
thickPos=10
thick.move(thickPos)

pwm2Pin=2
thin=Servo(pwm2Pin)
thinPos =50 # 50,60,70,80,90
thin.move(thinPos)

pwm3Pin=3 
claw=Servo(pwm3Pin)
clawPos=-53
claw.move(clawPos)

time.sleep(0.4)
free(claw)
free(thin)
free(thick)
free(base)

def callback(data, addr, ctrl):
  global record,movementsArr, basePos, thinPos, thickPos, clawPos, lastData
  
  if data < 0:
    data = lastData
  
  if data > 0:  # NEC protocol sends repeat codes.
    print('Data {:02x}'.format(data))
    
    if data == 0x13:
        print("RESET")
        basePos = 0
        base.move(basePos)
        thickPos = 10
        thick.move(thickPos)
        thinPos=50
        thin.move(thinPos)
        claw.move(-53)
        
    elif data == 0x0c:
        print("UP")
        thickPos = thickPos + 10
        thick.move(thickPos)
        print(thickPos)
        
    elif data == 0x10:
        print("DOWN")
        thickPos = thickPos - 10
        thick.move(thickPos)
        print(thickPos)
        
    elif data == 0x5a:
        print("THIN SHORT")
        if thinPos > 50:
            thinPos = thinPos - 10
            thin.move(thinPos)
        else:
            print("MIN")
        print(thinPos)
        
    elif data == 0x5e:
        print("THIN REACH")
        if thinPos < 90:
            thinPos = thinPos + 10
            thin.move(thinPos)
        else:
            print("MAX")
        print(thinPos)

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
          
    elif data == 0x5b: # channel up
        print("OPEN")
        claw.move(50)
        clawPos = 50
        
    elif data == 0x5f: # channel down
        print("CLOSE")
        claw.move(-53)
        clawPos = -53
        
    elif data == 0x47: # record
        print("RECORD")
        movementsArr=[]
        record = 1
        
    elif data == 0x46: # stop
        print("STOP")
        record = 0
        output = ujson.dumps(movementsArr)
        print(f'JSON={output}')
        f=open("movements.json","w")
        f.write(str(output))
        f.close()
        
    elif data == 0x43: # play
        print("PLAY")
        f=open("movements.json", "r")
        data = f.read()
        print(f'{data}')
        movementsArr=ujson.loads(data)
        f.close()
        
        print(f'Array={len(movementsArr)}')
        
        # Step through movementsArr
        print("Moving")
        for move in movementsArr:
            print(f'{move["base"]}')
            base.move(move["base"])
            thick.move(move["thick"])
            claw.move(move["claw"])
            time.sleep(0.5)
            free(claw)
            free(base)
            free(thick)
            
    if record == 1:
        movements = {"base": basePos, "thick": thickPos, "claw": clawPos}
        movementsArr.append(movements)
        print(f'Array={len(movementsArr)}')
    
    time.sleep(0.4)
    free(claw)
    free(thin)
    free(base)
    free(thick)
    lastData = data
    
ir = NEC_8(Pin(16, Pin.IN), callback) 