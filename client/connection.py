import socket

ADDR = (socket.gethostbyname(socket.gethostname()), 5051)

class Connection():
    def __init__(self):
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.connect(ADDR)
        self.server.setblocking(0)
    
    def send(self,msg):
        self.server.send(msg)
    def recv(self,msg):
        return self.server.recv(msg)