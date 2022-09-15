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
from ir_rx.test import test
test()
