import serial
import time

arduino_serial = serial.Serial('/dev/ttyS0', 9600, timeout= 0.1)
arduino_serial.flush()
while True:
    line = arduino_serial.readline().decode('utf-8').rstrip()
    print(line)
    time.sleep(1)