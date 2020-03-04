import time

steps = 10000

timestamps = []
while True:
    timestamps.append(time.time())
    if len(timestamps) > steps:
        break

print(timestamps[steps] - timestamps[0])
