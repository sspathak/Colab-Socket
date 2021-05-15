#!/usr/bin/env python3

import socket
import math
HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 65432        # Port to listen on (non-privileged ports are > 1023)

# with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
#     s.bind((HOST, PORT))
#     s.listen()
#     conn, addr = s.accept()
#     with conn:
#         print('Connected by', addr)
#         while True:
#             data = conn.recv(1024)
#             if not data:
#                 break
#             conn.sendall(data)
#

import asyncio, socket


async def split_read_bytes(reader):
    request = b''
    data_len = int((await reader.read(1024)).decode('utf8'))
    print(data_len)
    for i in range(data_len // 1024):
        request += (await reader.read(1024))
    if data_len % 1024 != 0:
        request += (await reader.read(data_len % 1024))

    if request == b'':
        print("EMPTY BYTES RECEIVED: CONNECTION ERROR")
    return request

async def split_write_bytes(data, writer):
    data_len = len(data)
    header = str(data_len).encode()
    writer.write(b'0' * (1024 - len(header)) + header)
    await writer.drain()
    for i in range(data_len // 1024):
        writer.write(data[i * 1024:i * 1024 + 1024])
        await writer.drain()
    if data_len % 1024 != 0:
        writer.write(data[-(data_len % 1024):])
        await writer.drain()



async def handle_client(reader, writer):
    r = ''
    try:
        while r != 'quit':
            r = (await split_read_bytes(reader)).decode('utf8')
            print(r)
            (await split_write_bytes(r.encode('utf8'), writer))

        writer.close()
    except ConnectionResetError:
        print("ConnectionReset")


async def run_server():
    server = await asyncio.start_server(handle_client, HOST, PORT)
    async with server:
        await server.serve_forever()

asyncio.run(run_server())

'''
1024102410241024102410241024102410241024102410241024102410241024102410241024102410241024102410241024102410241024102410241024102410241024102410241024102410241024102410241024102410241024102410241024102410241024102410241024102410241024102410241024102410241024102410241024102410241024102410241024102410241024102410241024102410241024102410241024102410241024102410241024102410241024102410241024102410241024102410241024102410241024102410241024102410241024102410241024102410241024102410241024102410241024102410241024102410241024102410241024102410241024102410241024102410241024102410241024102410241024102410241024102410241024102410241024102410241024102410241024102410241024102410241024102410241024102410241024102410241024102410241024102410241024102410241024102410241024102410241024102410241024102410241024102410241024102410241024102410241024102410241024102410241024102410241024102410241024102410241024102410241024102410241024102410241024102410241024102410241024102410241024102410241024102410241024102410241024102410241024102410241024
'''