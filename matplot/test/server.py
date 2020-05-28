#! /usr/bin/env python3

import sys
from socket import *

server_socket = socket(AF_INET, SOCK_STREAM)

address = ('', 9090)
server_socket.bind(address)
server_socket.listen(5)

global client_socket
client_socket = None

try:
    client_socket, client_address = server_socket.accept()
    sys.stderr.write("client %s:%d\n" % client_address)
    while True:
        line = client_socket.recv(1024)
        if not line:
            break;
        sys.stdout.write(line.decode())
        sys.stdout.flush()
except KeyboardInterrupt:
    pass

if client_socket:
    client_socket.close()
server_socket.close()
