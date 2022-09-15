from machine import Pin
import sys

led = Pin(25, Pin.OUT)

while True:
    
    data = sys.stdin.read(1)
    
    #pippo = data.decode("utf-8")
    pippo = data[0]
    
    if pippo == "a":
        led.on()

    else:
        led.off()