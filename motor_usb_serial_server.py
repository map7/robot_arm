#!/usr/bin/env python3
import serial
import time

port = serial.Serial("/dev/ttyACM0", 115200)
port.write(b"w")
time.sleep(1)
port.write(b"s")
time.sleep(1)
port.write(b"w")
time.sleep(1)
port.write(b"s")
time.sleep(1)
