import serial
import time

serial_out = serial.Serial(port = "COM5", baudrate = 115200)
serial_in = serial.Serial(port = "COM6", baudrate = 115200)

'''
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
'''

def double_sleep_to_hertz(seconds):
    time.sleep((1/2)/seconds)

def send(value):
    start_time = time.time_ns()
    serial_out.write('{}'.format(value).encode('utf-8'))
    print("Sent a: ", str(value))
    return start_time

def receive():
    input_from_serial = serial_in.read().decode('utf-8')
    end_time = time.time_ns()
    print("Received a:", str(input_from_serial))
    return end_time

def log_stamps(send, receive):
    log_file.write(str(send))
    log_file.write(str(receive))
    log_file.write("\n")


log_file = open("latency_log.csv")
log_file.open()

for _ in range(100):
    send_stamp = send(0)
    receive_stamp = receive()
    print("Sent and received a 0")
    log_stamps(send_stamp, receive_stamp)

    send_stamp = send(1)
    receive_stamp = receive()
    print("Sent and received a 1")
    log_stamps(send_stamp, receive_stamp)
    
    #send(0)
    #double_sleep_to_hertz(10)
    #send(1)
    #double_sleep_to_hertz(10)
    


 