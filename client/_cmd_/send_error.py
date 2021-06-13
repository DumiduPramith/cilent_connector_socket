import json
from connection_handler import conn

def send_err(msg, sid=None):
    method = b'__error__|'
    msg = {
        "error": msg,
        "sid" : sid
        }
    try:
        output = method + json.dumps(msg).encode('utf-8')
        conn.send_data(output, 'json')
    except: pass