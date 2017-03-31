import socket
import time

def Main():
    host = '127.0.0.1'
    port = 3000

    s = socket.socket()
    s.bind((host,port))

    s.listen(1)
    print "server is running..."
    print "waiting for client..."
    c, addr = s.accept()
    print "Connection from: "+str(addr)

    c.send("server connected..")

    while True:
        data = c.recv(3072)
        if data=="server -s":
            break
        print "send back form server to user: "+data
        data = str(data).upper()
        print "sending: "+data
        c.send(data)
    c.close()

if __name__=='__main__':
    Main()