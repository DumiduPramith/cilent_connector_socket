import socket

ADDR = (socket.gethostbyname(socket.gethostname()), 5051)

class Connection:
    def __init__(self):
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind(ADDR)
        self.server.listen()
        # self.server.setblocking(0)
    def fileno(self):
        return self.server.fileno()
    def accept(self):
        return self.server.accept()

    def send(self,msg):
        self.server.send(msg)

    def recv(self,msg):
        self.server.recv(msg)