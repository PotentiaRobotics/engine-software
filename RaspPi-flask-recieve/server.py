import socket
#!/usr/bin/env python

import serial
import time

ser = serial.Serial('/dev/ttyACM0', 9600, timeout=2)


host = '0.0.0.0'
port = 2345
s = socket.socket()
s.bind((host, port))
s.listen(2)
while True:
    conn, addr = s.accept()
    print("Connected by", addr)
    data = conn.recv(1024)

    print("received data:", data)
    # Get rid of garbage/incomplete data
    ser.flush()

    # Infinite loop
    i = 0
    while (1):
        i += 1
        send_string = ("Data\n")
        ser.write(send_string.encode('utf-8'))
        time.sleep(0.01)
        receive_string = ser.readline().decode('utf-8').rstrip()
        print(receive_string)

    conn.send(data)
    conn.close()
