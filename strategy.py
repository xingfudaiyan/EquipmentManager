'''
Created on Mar 26, 2013

@author: kang
'''
import socket
import sys
from struct import *


class Client:
    def __init__(self):
        self.host = 'localhost'
        self.port = 10001
        self.size = 1024
        self.client = None

    
    def bind_socket(self):        
        try:
            self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.client.connect((self.host, self.port))
        except socket.error, (message):
            if self.client:
                self.client.close()
            print "Could not open socket:" + message
            sys.exit(1)
    
    def pack_msg(self, clientsend):
        header_value = len(clientsend)
        header = pack('!I', header_value)
        clientsend = header + clientsend + pack('x',)
        '''        
        clientmap = map(hex, map(ord, clientsend))        
        print clientmap
        '''
        return clientsend

    def identify(self, identsend):
        clientsend = self.pack_msg(identsend)
        sendsize = self.client.send(clientsend)
           
             
        
    def fun(self, recvdata):
        if recvdata:
            msglen = unpack('!I', recvdata[0:4])
            msglen1 = msglen[0]+4
            msg = recvdata[4:msglen1]
            if msg != "ping"+pack('x',):
                print 'recived:', str(msglen[0]) + ':' + msg
            #print 'recived:', str(msglen[0]) + ':' + msg 
            self.fun(recvdata[msglen1:])
            
                    
    def client_run(self):
        self.bind_socket()       
        self.identify("identify-strategy echo-client abcd")
        
        while True:
            clientsend = raw_input(":")
            #clientsend = "commond echo-client strategy hello"
            if clientsend:                          
                self.pack_msg(clientsend)
                self.client.send(clientsend)
                 
            recvdata = self.client.recv(self.size)
            self.fun(recvdata)  
        

if __name__ == "__main__":
    c = Client()
    c.client_run()
