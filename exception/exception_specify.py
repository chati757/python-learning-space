try:
        s = socket.socket()
        s.connect((host,port))
        message = "empty"
        #message = raw_input("->")
        #while message !=q:
        while message !='server -s':
            #s.send(message)
            data = s.recv(1024)
            print 'response form server: '+data
            message = raw_input("->")
            s.send(message)
        s.close()
        
except IOError as e:
        print(e.errno)
        if(e.errno==10061):
            print("cannot connect , trying..")
        else:
            print(e)