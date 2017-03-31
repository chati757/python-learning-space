import asyncore
import collections
import logging
import socket

#asynio server
#ref https://github.com/eloyz/aioui
#ref https://github.com/jpwatts/aioserver

MAX_MESSAGE_LENGTH = 1024


class RemoteClient(asyncore.dispatcher):

    """Wraps a remote client socket."""

    def __init__(self, host, socket, address):
        asyncore.dispatcher.__init__(self, socket)
        self.host = host
        self.outbox = collections.deque()

    def say(self, message):
        self.outbox.append(message)

    def handle_read(self):
        client_message = self.recv(MAX_MESSAGE_LENGTH)
        self.host.broadcast(client_message)

    def handle_write(self):
        if not self.outbox:
            return
        message = self.outbox.popleft()
        if len(message) > MAX_MESSAGE_LENGTH:
            raise ValueError('Message too long')
        self.send(message)


class Host(asyncore.dispatcher):

    log = logging.getLogger('Host')

    def __init__(self, address=('localhost', 0)):
        asyncore.dispatcher.__init__(self)
        self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
        self.bind(address)
        self.listen(1)
        self.remote_clients = []

    def handle_accept(self):
        socket, addr = self.accept() # For the remote client.
        self.log.info('Accepted client at %s', addr)
        self.remote_clients.append(RemoteClient(self, socket, addr))

    def handle_read(self):
        self.log.info('Received message: %s', self.read())

    def broadcast(self, message):
        self.log.info('Broadcasting message: %s', message)
        for remote_client in self.remote_clients:
            remote_client.say(message)


class Client(asyncore.dispatcher):

    def __init__(self, host_address, name):
        asyncore.dispatcher.__init__(self)
        self.log = logging.getLogger('Client (%7s)' % name)
        self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
        self.name = name
        self.log.info('Connecting to host at %s', host_address)
        self.connect(host_address)
        self.outbox = collections.deque()

    def say(self, message):
        self.outbox.append(message)
        self.log.info('Enqueued message: %s', message)

    def handle_write(self):
        if not self.outbox:
            return
        message = self.outbox.popleft()
        if len(message) > MAX_MESSAGE_LENGTH:
            raise ValueError('Message too long')
        self.send(message)

    def handle_read(self):
        message = self.recv(MAX_MESSAGE_LENGTH)
        self.log.info('Received message: %s', message)


if __name__ == '__main__':
    #create server stage
    logging.basicConfig(level=logging.INFO)
    logging.info('Creating host')
    host = Host()
    
    #create client stage 
    logging.info('Creating clients')
    alice = Client(host.getsockname(), 'Alice')
    bob = Client(host.getsockname(), 'Bob')
    alice.say('Hello, everybody!')

    logging.info('Looping')
    asyncore.loop()

'''
OUTPUT
INFO:root:Creating host
INFO:root:Creating clients
INFO:Client (  Alice):Connecting to host at ('127.0.0.1', 51117)
INFO:Client (    Bob):Connecting to host at ('127.0.0.1', 51117)
INFO:Client (  Alice):Enqueued message: Hello, everybody!
INFO:root:Looping
INFO:Host:Accepted client at ('127.0.0.1', 55628)
INFO:Host:Accepted client at ('127.0.0.1', 55629)
INFO:Host:Broadcasting message: Hello, everybody!
INFO:Client (  Alice):Received message: Hello, everybody!
INFO:Client (    Bob):Received message: Hello, everybody!
'''