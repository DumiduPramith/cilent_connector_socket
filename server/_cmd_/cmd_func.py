import threading
from database.database_handler import \
 register_new_user, get_user_name_by_id
from get_connected_devices import show_connected_devices

def register_user(host_name):
    host_id = register_new_user(host_name)
    cmd = f'__register_id__|{host_id}'
    send_cmd(cmd)

def send_cmd(cmd):
    current_Thread = threading.current_thread()
    current_Thread.data_handler.send_data(cmd)

def identify_user(user_id):
    current_Thread = threading.current_thread()
    user_name = get_user_name_by_id(user_id)
    current_Thread.user_name = user_name
    current_Thread.user_id = user_id
    show_connected_devices()
