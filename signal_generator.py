import serial
import time

ser = serial.Serial()
ser.port='COM5'
ser.open()

sendZero = True
while True:
    if sendZero:
        ser.write(b'0\n')
        print("Sent 0")
    else:
        ser.write(b'1\n')
        print("Sent 1")
    sendZero = not sendZero
    time.sleep(0.25)

 