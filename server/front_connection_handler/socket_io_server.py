import socketio
import json
from connection_handler import HandleConnection

FORMAT = 'utf-8'
sio = socketio.Server(
    cors_allowed_origins='*'
    )

app = socketio.WSGIApp(sio)

thread = HandleConnection()
thread.start()

terminal_list = {}

@sio.event
def connect(sid, environ):
    pass

@sio.event
def user_id(sid, data):
    method = b'__connect__|'
    msg = {
            'user_name': 'superuser',
            'sid': sid,
            'data' : data,
    }
    msg = method + json.dumps(msg).encode(FORMAT)
    thread.send_data(msg)

@sio.event
def disconnect(sid):
    method = b'__disconnect__|'
    msg = { 
            'sid': sid,        
    }
    msg = method + json.dumps(msg).encode(FORMAT)
    thread.send_data(msg)

@sio.event
def pty_input(sid, data):
    method = b'__pty_input__|'
    msg = {
            'sid' : sid,
            'data': data,
    }
    msg = method + json.dumps(msg).encode('utf-8')
    thread.send_data(msg)

@sio.event
def resize(sid, data):
    # print("resize", sid)
    method = b'__resize__|'
    msg = {
            'sid' : sid,
            'resize': data
    }
    msg = method + json.dumps(msg).encode('utf-8')
    thread.send_data(msg)


def output(data):
    json_data = json.loads(data)
    # print(json_data)
    if json_data != None:
        sid = json_data['sid']
        data = json_data['output']
        data = {
            "output": data
        }
        sio.emit('pty_output', data, to=sid)