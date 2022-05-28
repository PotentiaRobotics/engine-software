# Commands for arduino

import serial
import time

ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1) # fix
ser.reset_input_buffer()

def onAndOfffLed():
    ser.write("ON\n".encode('utf-8'))
    line = ser.readline().decode('utf-8').rstrip()
    print(line)

    time.sleep(4)

    ser.write("OFF\n".encode('utf-8'))
    line = ser.readline().decode('utf-8').rstrip()
    print(line)
    time.sleep(4)

    if line == "You sent me: OFF":
        return 1
    else:
        return 0