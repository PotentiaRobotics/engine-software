#!/usr/bin/env python
 
import serial #
import time 

ser = serial.Serial('/dev/ttyACM0', 9600, timeout=2)
 
# Get rid of garbage/incomplete data
ser.flush()
 
# Infinite loop
i = 0
while (1):
  i+=1
  send_string = ("Data\n")
  ser.write(send_string.encode('utf-8'))
  time.sleep(0.02)
  receive_string = ser.readline().decode('utf-8').rstrip()
  print(receive_string)