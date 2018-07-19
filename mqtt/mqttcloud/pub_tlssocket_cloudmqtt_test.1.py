import socket
import ssl

# SET VARIABLES
HOST, PORT = 'm13.cloudmqtt.com',34081

# CREATE SOCKET
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.settimeout(10)

# WRAP SOCKET
wrappedSocket = ssl.wrap_socket(
    sock,ssl_version=ssl.PROTOCOL_TLSv1_2,
    do_handshake_on_connect=True
    )

# CONNECT AND PRINT REPLY
wrappedSocket.connect((HOST,PORT))

print("after connect")
wrappedSocket.send('test'.encode())
print(wrappedSocket.recv(1280))

# CLOSE SOCKET CONNECTION
print("closing")
wrappedSocket.close()