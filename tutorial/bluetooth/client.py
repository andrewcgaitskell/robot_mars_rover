#http://blog.kevindoran.co/bluetooth-programming-with-python-3/

"""
A simple Python script to send messages to a server over Bluetooth using
Python sockets (with Python 3.3 or above).
"""

import socket

serverMACAddress = 'B4:E6:2D:97:8B:0F'
port = 1
s = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)
s.connect((serverMACAddress,port))
while 1:
    text = input()
    if text == "quit":
        break
    s.send(bytes(text, 'UTF-8'))
s.close()
