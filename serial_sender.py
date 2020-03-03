import serial
ser = serial.Serial()
ser.port='COM5'
ser.open()
ser.write(b'hello\n')
print(b'hello\n')
