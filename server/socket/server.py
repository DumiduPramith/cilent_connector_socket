import threading, sys
from main_server_connection import Users, server
from thread_handler import connected_devices
from log import set_logger

logger = set_logger(__name__)

while True:
    try:
        user_conn, user_addr = server.accept()
    except KeyboardInterrupt:
        sys.exit(0)
    else:
        try:
            user_conn.setblocking(0)
            logger.info('new user {} Connected'.format(user_addr))
        except Exception as e:
            logger.exception('User Connection Error')
        else:
            print("New User Has Been Connected")
            try:
                conn = Users(user_conn, user_addr)
            except:
                logger.exception("User Object Cretion Failed")
            else:
                connected_devices.append(conn)
                conn.start()
                print(f"[Active Thread] {threading.active_count()-1}")
