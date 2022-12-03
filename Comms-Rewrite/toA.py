#!/usr/bin/env python3
 
###############################################################################
# Program: Send Strings to an Arduino From a Raspberry Pi
# File: send_strings_to_arduino.py
# Description: This program runs on a Raspberry Pi. It sends strings
#   to Arduino. It also receives the  string it sent
#   and prints it to the screen. This provides bi-directional (2-way) communication
#   between Arduino and Raspberry Pi.
# Author: Addison Sears-Collins
# Website: https://automaticaddison.com
# Date: July 5, 2020
###############################################################################
 
import serial # Module needed for serial communication
import time # Module needed to add delays in the code
 
# Set the port name and the baud rate. This baud rate should match the
# baud rate set on the Arduino.
# Timeout parameter makes sure that program doesn't get stuck if data isn't
# being received. After 1 second, the function will return with whatever data
# it has. The readline() function will only wait 1 second for a complete line 
# of input.
ser = serial.Serial('/dev/ttyACM1', 9600, timeout=1)
 
# Get rid of garbage/incomplete data
ser.flush()
 
# Infinite loop
i = 0
while (1):
  i+=1
  send_string = ("Data\n")
   
  # Send the string. Make sure you encode it before you send it to the Arduino.
  ser.write(send_string.encode('utf-8'))
   
  # Do nothing for 500 milliseconds (0.5 seconds)
  time.sleep(0.02)
 
  # Receive data from the Arduino
  receive_string = ser.readline().decode('utf-8').rstrip()
 
  # Print the data received from Arduino to the terminal
  print(receive_string)