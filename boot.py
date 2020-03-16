
from LTR329ALS01 import LTR329ALS01
from pysense import Pysense
import time
import sys
import pycom

pycom.heartbeat(False) # Disable the heartbeat LEDp

py = Pysense()
lt = LTR329ALS01(py, rate=LTR329ALS01.ALS_RATE_50)

low_t = 0
high_t = 3



on = False

def measure_light_between_turn_offs():
    hasBeenLow = False
    while True:
        measured_light = lt.light()[0]
        if measured_light > high_t and hasBeenLow:
                print(measured_light)
                sys.stdout.write("1\r")
                hasBeenLow = False
        elif measured_light <= low_t:
            hasBeenLow = True
            sys.stdout.write("0\r")
        time.sleep(0.001)
    


def measure_light_given_millis(millis):
    while True:
        print(lt.light()[0])
        time.sleep(millis/1000)


def measure_hertz(low, high):
    time.sleep(3)
    counter = 0
    hasBeenLow = False
    start_time = time.time() + 1
    while True:
        light_measure = lt.light()[0]
        if (light_measure > high) and hasBeenLow:
            counter = counter + 1
            print(str(counter / (time.time()-start_time)), " Hz")
            hasBeenLow = False

        elif light_measure < low:
            hasBeenLow = True


measure_light_given_millis(200)
#measure_light_between_turn_offs()
#measure_hertz(low_t, high_t)

'''
while True:
    light_level1 = lt.light()[0]
    light_level2 = lt.light()[1]
    avg_light = (light_level1 + light_level2)/2
    if avg_light > light_threshold:
        big_change = abs(last_measured - avg_light) > change_threshold
        if big_change and not on:
            change = abs(last_measured - ((light_level1 + light_level2)/2))
            print("\n")
            print(avg_light)
            last_measured = avg_light
            on = True
    else:
        last_measured = avg_light
        on = False

    time.sleep(.001)
'''
