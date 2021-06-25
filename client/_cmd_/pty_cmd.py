import json
from shell.terminal import connect_, pty_input_, resize_, thread_list, tabs

def pty_connect(data):
    json_data = json.loads(data)
    sid = json_data['sid']
    connect_(sid, json_data)

def disconnect(data):
    sid = json.loads(data)['sid']
    try:
        fd = tabs[sid]
    except: return
    for thread in thread_list:
        if int(thread.fd) == int(fd):
            thread.Connected = False
            for count, t in enumerate(thread_list):
                if t is thread:                   
                    del thread_list[count]
                    del tabs[sid]
                    # print("thread removed")

def pty_input(data):
    json_data = json.loads(data)
    sid = json_data['sid']
    pty_input_(sid,json_data)

def pty_resize(data):
    json_data = json.loads(data)
    sid = json_data['sid']
    resize_data = json_data['resize']
    resize_(sid,resize_data)