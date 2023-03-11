import socket
host=''
port=2345
s=socket.socket()
s.bind((host,port))
s.listen(10)
while True:
	conn,addr=s.accept()
	print("Connected by",addr)
	data=conn.recv(1024)
	print("received data:",data)
	conn.send(data)
	conn.close()
