#! /usr/bin/env python3

import sys
import socket

address = ('127.0.0.1', 9090)
client = socket.socket()
client.connect(address)

try:
    while True:
        line = sys.stdin.readline()
        if not line:
            break
        client.send(line.encode())
except (EOFError, KeyboardInterrupt):
    pass
client.close()
