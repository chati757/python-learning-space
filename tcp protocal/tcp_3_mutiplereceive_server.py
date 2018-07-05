#!/usr/bin/python           # This is server.py file

import socket# Import socket module
import threading

def on_new_client(clientsocket,addr):
    check_current_thread("in on_new_client")
    print("connection form : "+str(addr))
    clientsocket.send("server connected..")
    while True:
        print("listening connection from", addr)
        msg = clientsocket.recv(1024) 
        #do some checks and if msg == someWeirdSignal: break:
        if msg=="server -s":
            print("in break..")
            return
        print("addr", " >> ", msg.decode("utf-8"))
        #sending stage
        msg = input('SERVER >> ') 
        #Maybe some code to compute the last digit of PI, play game or anything else can go here and when you are done.
        clientsocket.send(msg.decode("utf-8")) 
    print("client is exit")
    clientsocket.close()

def check_current_thread(note):
    print("current thread.. "+note)
    print(threading.enumerate())#show all thread actually running  

def serv_console():
    print("serv_console")

if __name__=="__main__":
    check_current_thread("start main")
    print("create console")
    s = socket.socket()         # Create a socket object
    host = '127.0.0.1'          # Get local machine name
    port = 3000                 # Reserve a port for your service.

    print("Server started!")
    print("Waiting for clients...")

    s.bind((host, port))        # Bind to the port
    s.listen(3)                 # Now wait for client connection.
    while True:
        check_current_thread("in before accept")
        c, addr = s.accept()     # Establish connection with client.
        #print("connect from ",c,addr)
        #thread.start_new_thread(on_new_client,(c,(addr,)))
        client_thread=threading.Thread(target=on_new_client,args=(c,(addr,)),name="client thread")
        client_thread.setDaemon(True)
        client_thread.start()
        #check number of client 
        if(threading.active_count()<2):
            break    
        #on_new_client(c,addr)
    #Note it's (addr,) not (addr) because second parameter is a tuple
    #Edit: (c,addr)
    #that's how you pass arguments to functions when creating new threads using thread module.
    s.close()
