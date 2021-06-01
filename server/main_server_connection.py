import select
import threading, sys
from server_connection import Connection
from data_handler import DataHandler
from user_data import UserData
from disconnect_handler import disconnect

class Users(threading.Thread, DataHandler, UserData):
    def __init__(self, user_conn, user_adr):
        threading.Thread.__init__(self)
        self.user_conn = user_conn
        self.user_addr = user_adr
        self.data_handler = DataHandler(self.user_conn)
        UserData.__init__(self,None, None, [])

    def run(self):
        CONNECTED = True
        socket_list = [self.user_conn, sys.stdin]
        while CONNECTED:     
            read_socket, write_socket, error = select.select(socket_list,[],socket_list,0.5)
            for socket in read_socket:
                if socket is self.user_conn:
                    msg = self.data_handler.receive_data()
                    if msg == '':
                        socket.close()
                        print(f"[User {self.user_addr} Disconnected]")
                        print(f'[Active Threads] {threading.active_count()}')
                        disconnect(threading.current_thread())
                        CONNECTED = False
                    elif msg != None:
                        print('main server: ',msg.strip('\n'))

        
server = Connection()
