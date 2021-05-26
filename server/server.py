import select
import threading, sys
from server_connection import Connection
from data_handler import DataHandler
HEADER = 64
FORMAT = 'utf-8'

connected_devices = []

class Users(threading.Thread, DataHandler):
    def __init__(self, user_conn, user_adr):
        threading.Thread.__init__(self)
        self.user_conn = user_conn
        self.user_addr = user_adr
    
    def on_read(self):
        msg = sys.stdin.readline()
        msg = msg.strip('\n')
        if msg == ' ':
            pass
        else:
            DataHandler.send_data(self.user_conn,msg)
            # self.user_conn.send(msg.encode(FORMAT))

    def run(self):
        CONNECTED = True
        socket_list = [self.user_conn, sys.stdin]
        while CONNECTED:     
            read_socket, write_socket, error = select.select(socket_list,[],socket_list,0.5)
            for socket in read_socket:
                if socket is self.user_conn:
                    msg = DataHandler.receive_data(socket)
                    # msg = socket.recv(6).decode('utf-8')
                    if msg == '':
                        socket.close()
                        print(f"[User {self.user_addr} Disconnected]")
                        CONNECTED = False
                    print(msg.strip('\n'))
                elif socket is socket_list[1]:
                    self.on_read()
    def conn_name(self):
        print("dumidu")
        
server = Connection()

while True:
    user_conn, user_addr = server.accept()
    user_conn.setblocking(0)
    print("New User Has Been Connected")
    conn = Users(user_conn, user_addr)
    connected_devices.append(conn)
    conn.start()
    connected_devices[0].conn_name()

