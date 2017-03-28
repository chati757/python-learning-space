#!/usr/bin/python           # This is server.py file

import socket# Import socket module
import threading

def on_new_client(clientsocket,addr):
    while True:
        print 'Got connection from', addr
        msg = clientsocket.recv(1024) 
        #do some checks and if msg == someWeirdSignal: break:
        if data=="server -s":
            break
        print addr, ' >> ', msg
        msg = raw_input('SERVER >> ') 
        #Maybe some code to compute the last digit of PI, play game or anything else can go here and when you are done.
        clientsocket.send(msg) 
    clientsocket.close()
    
if __name__=="__main__":
    s = socket.socket()         # Create a socket object
    host = '127.0.0.1' # Get local machine name
    port = 3000                 # Reserve a port for your service.

    print 'Server started!'
    print 'Waiting for clients...'

    s.bind((host, port))        # Bind to the port
    s.listen(5)                 # Now wait for client connection.

    while True:
        c, addr = s.accept()     # Establish connection with client.
        #thread.start_new_thread(on_new_client,(c,addr))
        client_thread=threading.Thread(target=on_new_client(c,addr))
        client_thread.start()
    #Note it's (addr,) not (addr) because second parameter is a tuple
    #Edit: (c,addr)
    #that's how you pass arguments to functions when creating new threads using thread module.
    s.close()
