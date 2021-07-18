#!/usr/bin/env python3
import serial
if __name__ == '__main__':
    ser = serial.Serial('/dev/tty.usbserial-01BE27D0', 115200, timeout=1) #Declaring Serial Object. First parameter is the usb port. Second is Baud Rate.
    ser.flush()
    while True:
        if ser.in_waiting > 0:
            line = ser.readline().decode('utf-8').rstrip() #Stores serial data in utf 8 format.
            print(line) 
