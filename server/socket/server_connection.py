import socket, sys,os
from log import set_logger

try:
    is_docker=os.environ['is_docker']
except:
    is_docker=False
if is_docker:
    PORT = os.environ['SOCKET_PORT']
else:
    PORT = 5050
ADDR = (socket.gethostbyname(socket.gethostname()), int(PORT))

logger = set_logger(__name__)

class Connection:
    def __init__(self):
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            self.server.bind(ADDR)
            print(f"binded {ADDR}")
        except Exception:
            logger.exception("bin error")
            sys.exit(1)
        else:
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