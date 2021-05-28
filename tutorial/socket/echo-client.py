#!/usr/bin/env python3

import socket

serverMACAddress = 'B4:E6:2D:97:8B:0F'
port = 1 # this was 3, it works as 1
#s = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)
#s.connect((serverMACAddress,port))


HOST = serverMACAddress  # The server's hostname or IP address
PORT = 1        # The port used by the server

with socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM) as s:
    s.connect((HOST, PORT))
    s.sendall(b'Hello, world')
    data = s.recv(1024)

print('Received', repr(data))
