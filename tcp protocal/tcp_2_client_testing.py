import socket

def Main():
    host = '192.168.1.35'
    port = 3000
    
    try:
        s = socket.socket()
        s.connect((host,port))
        print(s)
        message = "empty"
        message = input("-> ")
        #while message !=q:
        s.send(message.encode('utf-8'))

        data = s.recv(1024)
        print('response form server: '+data.decode("utf-8"))
        
        s.close()

    except IOError as e:
        print(e.errno)
        if(e.errno==10061):
            print("cannot connect , trying..")
        else:
            print(e)
    
if __name__ == '__main__':
    Main()
