from machine import UART
import time
import pycom

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


set_led_to(GREEN)

my_file = open("/flash/output.txt", "w")
my_file.write("ASDASDASD")
for i in range(5):
    if uart.any():
        local_color = 0x7F7F7F
        incoming_message = uart.readline()
        my_file.write(incoming_message)
        my_file.write("asdasd")
        if incoming_message == '0\n':
            local_color = RED
        elif incoming_message == '1\n':
            local_color = GREEN
        #file.write(incoming_message)
        if isOn:
            set_led_to(OFF)
        else:
            set_led_to(local_color)
        isOn = not isOn
    time.sleep(0.25)

my_file.close()