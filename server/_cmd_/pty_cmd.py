import json
from logging import Logger
from thread_handler import send_msg_to_client,\
 send_msg_to_su, set_sid, remove_sid, get_password
FORMAT = 'utf-8'
from log import set_logger

logger = set_logger(__name__)

def pty_connect(raw_data,data):
    #identify_su user
    try:
        data = json.loads(data)
        client_id = int(data["data"]["id"])
        sid = data["sid"]
    except Exception:
        logger.exception("pty_connect")
    else:
        is_set_sid = set_sid(client_id, data["sid"]) # connect client and front connection
        if is_set_sid:
            send_msg_to_client(sid,raw_data)
        else:
            logger.error(f"sid set failed: [sid:{sid}, client_id:{client_id}]")
            print("Sid Set Failed")
        # send user password from database to front connection
        send_password(client_id, sid)
        # send_msg_to_client(raw_data)

def send_password(client_id, sid):
    password = get_password(client_id)
    data = {
        "password" : password,
        "sid" : sid
    }
    output = json.dumps(data).encode('utf-8')
    send_msg_to_su(output)
    logger.debug(f"password sended to [sid: {sid}, pass: {password}]")
        
def disconnect(raw_data, data):
    data = json.loads(data)
    try:
        sid = data["sid"]
    except KeyError:
        logger.exception(f"Disconnect Key error [data: {data}]")
    else:
        send_msg_to_client(sid, raw_data)
        remove_sid(sid)

def pty_input(raw_data, data):
    try:
        data = json.loads(data)
        sid = data["sid"]
    except Exception:
        logger.exception(f"pty_input [data: {data}]")
    else:
        send_msg_to_client(sid, raw_data)

def pty_resize(raw_data,data):
    try:
        data = json.loads(data)
        sid = data["sid"]
    except Exception:
        logger.exception(f"pty_resize [data: {data}")
    else:
        send_msg_to_client(sid, raw_data)

def pty_output(data):
    send_msg_to_su(data)