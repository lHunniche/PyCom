import pycom
import time

RED = 0xFF00FF
YELLOW = 0xFFFF33
GREEN = 0x007F00
OFF = 0x000000

def set_led_to(color=GREEN):
    pycom.heartbeat(False) # Disable the heartbeat LED
    pycom.rgbled(color)

def flash_led_to(color=GREEN, t1=1):
    set_led_to(color)
    time.sleep(t1)
    set_led_to(OFF)

#flash_led_to(RED)
#flash_led_to(YELLOW)
#set_led_to(OFF)

def blink_every_second():
    #for number in range(100):
        #color = generate_random_color()
    set_led_to(GREEN)
        #time.sleep(1)
        #set_led_to(OFF)
        #time.sleep(1)

blink_every_second()


#print("Hello")