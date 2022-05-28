import socket

HOST = '10.235.1.127' # Use this for client
PORT = 12345 # Pick an open Port (1000+ recommended), must match the client sport
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print('Socket created')

#managing error exception
try:
	s.bind((HOST, PORT))
except socket.error:
    print ('Bind failed ')

s.listen(5)
print ('Socket awaiting messages')
(conn, addr) = s.accept()
print ('Connected')

# awaiting for message
while True:
	data = conn.recv(1024)
	print (data)

	# # Sending reply
	conn.send(data+bytes(" works",'utf-8'))
	# conn.close() # Close connections
