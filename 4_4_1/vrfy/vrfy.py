#!/usr/bin/env python
import socket, sys

if __name__ == '__main__':

	if len(sys.argv) != 3:
		print("[!] Usage: vrfy.py [username] [ip]")
		sys.exit()

	# Create a socket
	sox = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	
	# Connect to the Server
	connect = sox.connect((sys.argv[2], 25))
	
	# Grab the banner
	banner = sox.recv(1024).decode('utf-8')
	
	# VRFY a user
	vrfy_string = ('VRFY ' + sys.argv[1] + '\r\n').encode('utf-8')
	sox.send(vrfy_string)
	result = sox.recv(1024).decode('utf-8')
	
	# print the output
	print("[*] Banner: {0}".format(banner.strip('\n')))
	print("[*] Query Result: {0}".format(result))
	
	# Close the socket
	sox.close()
