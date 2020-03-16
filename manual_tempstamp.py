import time

my_file = open("real_temp_stamps.csv", "w")
my_file.write("time, temp\n")
while True:
    temp = input("How hot are you? ")
    if(temp == '0'):
        break
    current_time = time.time_ns()
    my_file.write(str(current_time) + ", " + str(temp) + "\n")

my_file.close()

    
