#! /usr/bin/python3


import socket
from socket import *
import time

HOST = ""
PORT = 5000
def main():
    s = socket()
    s.setsockopt(IPPROTO_TCP, TCP_MAXSEG, 8000)
    s.connect((HOST, PORT))
    print('Connected to ', HOST)
    r = b'a' * 7000
    print(f"sending {r}")
    s.send(r)
    time.sleep(60)



if __name__ == '__main__':
    main()
