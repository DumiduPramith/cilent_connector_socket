from database.id_checker import main
from connection_handler import conn
import socket 

def authenticate():
    has_id = check_has_id()
    if has_id is False:
        return True
    else:
        send_user_authentication_id(has_id)
        return False

def check_has_id():
    id_or_false = main() #return id or false
    if id_or_false is False: 
        get_user_id_from_server()
        return False
    else: return id_or_false

def get_user_id_from_server():
    host_name = socket.gethostname()
    conn.send_data(f'__register_user__|{host_name}')

def send_user_authentication_id(id):
    msg = f'__user_id__|{id}'
    conn.send_data(msg)
    return True


