import json
from thread_handler import remove_thread, connected_devices
# from cmd_func import shutdown_cmd

def disconnect(thread):
    if thread.user_name == "su":
        su_disconnect()
    remove_thread(thread)

def su_disconnect():
    for device in connected_devices:
        if device.connected_sid != []:
            for sid in device.connected_sid:
                method = b'__disconnect__|'
                msg = { 
                        'sid': sid,        
                    }
                msg = method + json.dumps(msg).encode('utf-8')
                device.data_handler.send_data(msg)