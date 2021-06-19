import socket, os

try:
    is_docker=os.environ['IS_DOCKER']
except:
    is_docker=False
if bool(is_docker):
    PORT = os.environ['SOCKET_PORT']
    ADDR = ('socket',int(PORT))
else:
    PORT = 5050
    ADDR = (socket.gethostbyname(socket.gethostname()), int(PORT))
    
class Connection():
    def __init__(self):
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print(f"connected {ADDR}")
        self.server.connect(ADDR)
        self.server.setblocking(0)
    
    def send(self,msg):
        self.server.send(msg)
    def recv(self,msg):
        return self.server.recv(msg)