import socket

def Main():
    host = '127.0.0.1'
    port = 3000
    
    try:
        s = socket.socket()
        s.connect((host,port))
        message = "empty"
        #message = raw_input("->")
        #while message !=q:
        while message !='server -s':
            #s.send(message)
            data = s.recv(1024)
            print('response form server: '+data)
            message = input("->")
            s.send(message)
        s.close()
    except IOError as e:
        print(e.errno)
        if(e.errno==10061):
            print("cannot connect , trying..")
        else:
            print(e)
    
if __name__ == '__main__':
    Main()