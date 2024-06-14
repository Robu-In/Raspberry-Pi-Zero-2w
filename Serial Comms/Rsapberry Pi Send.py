from serial import Serial
import time

arduino_serial = Serial('/dev/ttyS0', 9600, timeout = 0.1)
arduino_serial.flush()

while True:
        try:
                arduino_serial.write(b"ON\n")
                time.sleep(1)
                arduino_serial.write(b"OFF\n")
                time.sleep(1)

        except KeyboardInterrupt:
                arduino_serial.close()
                break