import select
import threading, sys
from server_connection import Connection
from data_handler import DataHandler
from user_data import UserData

class Users(threading.Thread, DataHandler, UserData):
    def __init__(self, user_conn, user_adr):
        threading.Thread.__init__(self)
        self.user_conn = user_conn
        self.user_addr = user_adr
        self.data_handler = DataHandler(self.user_conn)
        UserData.__init__(self,None, None)
    def on_read(self):
        msg = sys.stdin.readline()
        msg = msg.strip('\n')
        if msg == ' ':
            pass
        else:
            self.data_handler.send_data(msg)
            # self.user_conn.send(msg.encode(FORMAT))

    def run(self):
        CONNECTED = True
        socket_list = [self.user_conn, sys.stdin]
        while CONNECTED:     
            read_socket, write_socket, error = select.select(socket_list,[],socket_list,0.5)
            for socket in read_socket:
                if socket is self.user_conn:
                    msg = self.data_handler.receive_data()
                    # msg = socket.recv(6).decode('utf-8')
                    if msg == '':
                        socket.close()
                        print(f"[User {self.user_addr} Disconnected]")
                        CONNECTED = False
                    print(msg.strip('\n'))
                elif socket is socket_list[1]:
                    self.on_read()

        
server = Connection()
