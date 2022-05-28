import socket
import threading

HOST = '10.235.1.145' # Enter IP or Hostname of your server
PORT = 12345 # Pick an open Port (1000+ recommended), must match the server port
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST,PORT))

#Lets loop awaiting for your input

def telemetryReceive():
	while True:
		reply = s.recv(1024)
		if reply != None:
			print(reply)

def telemetrySend():
	while True:
		command = input('Enter your command: ')
		if command != None:
			s.send(bytes(command, 'utf-8'))

def main():
	threading.Thread(target=telemetryReceive).start()
	threading.Thread(target=telemetrySend).start()

main()