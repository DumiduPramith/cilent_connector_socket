import select, sys
from connection import Connection
from data_handler import DataHandler
import threading

class HandleConnection(DataHandler, Connection, threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.server = Connection()
        super().__init__(self.server.server)
        
    def run(self):
        su_msg = '__su__|'.encode('utf-8')
        self.send_data(su_msg)
        CONNECTED = True
        while CONNECTED:
            socket_list = [self.server.server]
            read_socket, write_socket, error = select.select(socket_list,[],socket_list,0.5)
            for socket in read_socket:
                if socket is self.server.server:
                    msg = self.receive_data()
                    if msg == '':
                        socket.close()
                        CONNECTED = False