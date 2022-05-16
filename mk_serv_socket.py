#! /usr/bin/python3


import socket
from socket import *
import time

HOST = ""
PORT = 5000
def main():
    with socket() as s:
        s.setsockopt(IPPROTO_TCP, TCP_MAXSEG, 8000)
        s.bind((HOST, PORT))
        s.listen()
        con, addr = s.accept()
        st = con.recv(2**15)
        print(f'recieved {st}')

        time.sleep(60)



if __name__ == '__main__':
    main()
