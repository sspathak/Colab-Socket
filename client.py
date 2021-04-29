#!/usr/bin/env python3

import socket
import math

HOST = '127.0.0.1'  # The server's hostname or IP address
# HOST = '35.209.32.35'  # The server's hostname or IP address
PORT = 65432        # The port used by the server

def split_send_bytes(s, inp):
    data_len = (len(inp))
    header = str(data_len).encode()
    s.send(b'0' * (1024 - len(header)) + header)
    for i in range(data_len // 1024):
        s.send(inp[i * 1024:i * 1024 + 1024])
    if data_len % 1024 != 0:
        s.send(inp[-(data_len % 1024):])

def split_recv_bytes(s):
    dat = b''
    data_len = int((s.recv(1024)).decode('utf8'))
    for i in range(data_len // 1024):
        dat += s.recv(1024)
    if data_len % 1024 != 0:
        dat += s.recv(data_len % 1024)

    return dat


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    data = None
    s.connect((HOST, PORT))
    while data != "quit":
        while (inp := input("Enter text to send:")) == "":
            continue
        inp = inp.encode('utf8')

        split_send_bytes(s, inp)
        data = split_recv_bytes(s).decode('utf8')
        print('Received          :' + data)
        print(inp.decode('utf8') == data)
