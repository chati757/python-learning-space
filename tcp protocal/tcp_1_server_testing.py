import socket
import time

def Main():
    host = '192.168.1.35'
    port = 3000

    s = socket.socket()
    s.bind((host,port))

    s.listen(1)
    for i in range(2):
        print("server is running...")
        print("waiting for client...")
        print(s)
        print("server busy")
        time.sleep(50) 
        # ในขณะที่มัน busy โดย sleep มันจะ listen แค่ 1 client เท่านั้น หาก cline 2 หรือมากกว่านั้นเข้ามา
        # client มันจะ error รหัส 10061 ทันที่ 
        c,addr = s.accept()
        print("Connection from: " +str(addr))
    
        data=c.recv(1024)
        print(c)
        print(str(data.decode("utf-8")))
        re_msg="receive"
        c.send(re_msg.encode("utf-8"))
        print("delay")
    c.close()

if __name__=='__main__':
    Main()
