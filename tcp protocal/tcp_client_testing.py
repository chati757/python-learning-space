import socket

def Main():
    host = '127.0.0.1'
    port = 3000

    s = socket.socket()
    s.connect((host,port))
    message = "empty"
    #message = raw_input("->")
    #while message !=q:
    while message !='server -s':
        #s.send(message)
        data = s.recv(3072)
        print 'response form server: '+data
        message = raw_input("->")
        s.send(message)
    s.close()
    
if __name__ == '__main__':
    Main()