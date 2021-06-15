import socket, sys
from log import set_logger
ADDR = (socket.gethostbyname(socket.gethostname()), 5050)

logger = set_logger(__name__)

class Connection:
    def __init__(self):
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            self.server.bind(ADDR)
        except Exception:
            logger.exception()
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