import serial
import time
from machine import UART

#ser = serial.Serial()
#ser.port='COM6'
#ser.open()

uart = UART(0, baudrate=115200)
uart.init(115200,bits=8,parity=None, stop=1)

while True:
    if uart.any():
        print(uart.readline())
    time.sleep(0.1)
