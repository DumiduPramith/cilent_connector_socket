import socket

# ADDR = (socket.gethostbyname(socket.gethostname()), 5051)

with open("hos.txt",'r') as f:
    data = f.read().split(':')
    data[1] = int(data[1])
    ADDR=tuple(data)
    
class Connection():
    def __init__(self):
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.connect(ADDR)
        self.server.setblocking(0)
    
    def send(self,msg):
        self.server.send(msg)
    def recv(self,msg):
        return self.server.recv(msg)