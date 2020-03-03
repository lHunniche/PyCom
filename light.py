# Measuring light with an LDR
import socket
import utime
import binascii
import pycom
import ustruct
import machine
import time
import LTR329ALS01
from machine import Pin
from pysense import Pysense

py = Pysense()
lt = LTR329ALS01(py)

adc = machine.ADC()               # create an ADC object
apin = adc.channel(pin=Pin.exp_board.G31) # Lopy4 specific: (pin = 'P17')   create an analog pin on P17 & connect TMP36

# Light measurment
def light_measure():
    print("")
    print("Reading LDR Sensor...")
    value = apin()
    print("ADC count = %d" %(value))

    # LoPy  has 1.1 V input range for ADC
    light = value
    print("light = %5.1f" % (light))

    return light

#for number in range (10):
#    light_level = light_measure()
#    print(light_level)
#    time.sleep(1)
for x in range(5):
    #print(light_measure())
    lt.light()
    time.sleep(5)