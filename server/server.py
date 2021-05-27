import threading
from main_server_connection import server, Users
from thread_handler import connected_devices
from get_connected_devices import show_connected_devices

while True:
    user_conn, user_addr = server.accept()
    user_conn.setblocking(0)
    print("New User Has Been Connected")
    conn = Users(user_conn, user_addr)
    connected_devices.append(conn)
    conn.start()
    print(f"[Active Thread] {threading.active_count()-1}")


