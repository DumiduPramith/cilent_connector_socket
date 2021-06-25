import socketio
import json
from connection_handler import HandleConnection

FORMAT = 'utf-8'
sio = socketio.Server(
    cors_allowed_origins='*'
    )

thread = HandleConnection()
thread.start()

app = socketio.Middleware(sio)

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
    msg = method + json.dumps(msg).encode(FORMAT)
    thread.send_data(msg)

@sio.event
def resize(sid, data):
    # print("resize", sid)
    method = b'__resize__|'
    msg = {
            'sid' : sid,
            'resize': data
    }
    msg = method + json.dumps(msg).encode(FORMAT)
    thread.send_data(msg)
    # print("sid", sid)

@sio.event
def archive_folder(sid, data):
    method = b'__archive__|'
    msg = {
        'sid': sid,
        'data': data
        }
    # print(data)
    msg = method + json.dumps(msg).encode(FORMAT)
    thread.send_data(msg)

@sio.event
def get_device_list(sid, data):
    method = b'__GET_DEVICES__|'
    msg = {
        'sid': sid,
        'data': data
    }
    msg = method + json.dumps(msg).encode(FORMAT)
    thread.send_data(msg)

def output(data):
    try:
        json_data = json.loads(data)
    except: pass
    else:
        value = False
        for count, key in enumerate(json_data, start=1):
            if count == 1:
                value = key
                break
        if value != False:
            if json_data != None:
                sid = json_data['sid']
                if value == 'output':
                    data = json_data['output']
                    data = {
                        "output": data
                    }
                    sio.emit('pty_output',data, to=sid)
                    # print("emited 1 sid: ", sid)
                elif value == 'error':
                    data = json_data['error']
                    sio.emit('error',data,to=sid)
                    # print("emited 2")
                elif value == 'password':
                    data = json_data['password']
                    sio.emit('password',data,to=sid)
                elif value == 'disconnect':
                    data = json_data['disconnect']
                    sio.emit('disconnect',data,to=sid)
                elif value == 'devices':
                    data = json_data['devices']
                    sio.emit('list', data,to=sid)
