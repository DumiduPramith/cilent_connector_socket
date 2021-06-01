import select, sys
from connection import Connection
from data_handler import DataHandler

class HandleConnection(DataHandler, Connection):
    def __init__(self):
        self.server = Connection()
        super().__init__(self.server.server)
        
    def run(self):
        socket_list = [self.server.server]
        read_socket, write_socket, error = select.select(socket_list,[],socket_list,0.5)
        for socket in read_socket:
            if socket is self.server.server:
                msg = self.receive_data()
                if msg == '':
                    socket.close()
                    return False
                # print("main ", msg)
            
        # self.on_read()
        # print(write_socket)
    
    def on_read(self):
        msg = sys.stdin.readline()
        if msg:
            self.send_data(msg)

conn = HandleConnection()