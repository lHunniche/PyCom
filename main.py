from machine import UART
import time
import pycom
import sys

# this uses the UART_1 default pins for TXD and RXD (``P3`` and ``P4``)
uart = UART(0, baudrate=115200)
uart.init(115200,bits=8,parity=None, stop=1)


GREEN = 0x007F00
BLUE = 0x99cccc
RED = 0x7F0000
OFF = 0x000000
isOn = True

def set_led_to(color=GREEN):
    pycom.heartbeat(False) # Disable the heartbeat LED
    pycom.rgbled(color)


set_led_to(OFF)
'''
while True:
    if uart.any():
        incoming_message = uart.readline()
        if isOn:
            set_led_to(OFF)
        else:
            set_led_to(GREEN)
        isOn = not isOn
    time.sleep(0.25)
'''

try:
    while True:
        value_in = sys.stdin.read(1)
        
        if value_in == "1":
            set_led_to(OFF)
        elif value_in == "0":
            set_led_to(OFF)


except (KeyboardInterrupt, SystemExit):
    raise