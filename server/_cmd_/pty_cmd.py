import json, threading
from thread_handler import send_msg_to_client, send_msg_to_su, set_sid, remove_sid
FORMAT = 'utf-8'

def pty_connect(raw_data,data):
    #identify_su user
    data = json.loads(data)
    client_id = int(data["data"]["id"])
    sid = data["sid"]
    is_set_sid = set_sid(client_id, data["sid"]) # connect client and front connection
    if is_set_sid:
        send_msg_to_client(sid,raw_data)
    else: print("Sid Set Failed")
    # send_msg_to_client(raw_data)

def disconnect(raw_data, data):
    data = json.loads(data)
    sid = data["sid"]
    send_msg_to_client(sid, raw_data)
    remove_sid(sid)

def pty_input(raw_data, data):
    data = json.loads(data)
    sid = data["sid"]
    send_msg_to_client(sid, raw_data)

def pty_resize(raw_data,data):
    data = json.loads(data)
    sid = data["sid"]
    send_msg_to_client(sid, raw_data)

def pty_output(data):
    send_msg_to_su(data)