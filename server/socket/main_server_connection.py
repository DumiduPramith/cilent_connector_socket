import select
import threading, sys
from server_connection import Connection
from data_handler import DataHandler
from user_data import UserData
from disconnect_handler import disconnect
from log import set_logger

logger = set_logger(__name__)

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
        self.data_handler.send_data("hellow")
        while CONNECTED:     
            read_socket, _, _ = select.select(socket_list,[],socket_list,0.5)
            for socket in read_socket:
                if socket is self.user_conn:
                    try:
                        msg = self.data_handler.receive_data()
                    except Exception:
                        logger.exception("data handler error")
                        msg = ''
                    if msg == '':
                        socket.close()
                        logger.info("[User {} Disconnected, ip: {}]".format(self.user_id, self.user_addr))
                        print(f"[User {self.user_addr} Disconnected]")
                        print(f'[Active Threads] {threading.active_count()}')
                        disconnect(threading.current_thread())
                        CONNECTED = False
                    elif msg != None:
                        print('main server: ',msg.strip('\n'))
                        logger.debug(f"main_server [msg: {msg}]")

server = Connection()