# Client Code -- The client just try to GET a http page for testing that the controller_pox.py does not report false positive

## (c) Mehdi Mtimet and Geoffrey Boulanger 
## PFE - Monitoring de botnets a travers des reseaux SDN
## 2015 - 2016

import sys
from socket import * 

HOST = '10.0.0.2'
PORT = 80
ADDR = (HOST,PORT)
BUFSIZE = 2048

client = socket(AF_INET,SOCK_STREAM)
client.connect((ADDR))

client.send("GET /%s HTTP/1.1\r\n" % message)

data = client.recv(BUFSIZE)
data = data.rstrip()
print data

client.close()
