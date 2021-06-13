import json
from thread_handler import remove_thread, connected_devices, send_msg_to_su
# from cmd_func import shutdown_cmd
from log import set_logger

ex_logger = set_logger(__name__)

def disconnect(thread):
    if thread.user_name == "su":
        ex_logger.debug("su disconnect msg sended")
        su_disconnect()
    elif thread.user_id != None:
        ex_logger.debug("disconnect msg sended to {}".format(thread.user_id))
        send_disconnect_msg(thread)
    remove_thread(thread)

def su_disconnect():
    for device in connected_devices:
        if device.connected_sid != []:
            for sid in device.connected_sid:
                method = b'__disconnect__|'
                msg = { 
                        'sid': sid,        
                    }
                try:
                    msg = method + json.dumps(msg).encode('utf-8')
                except Exception:
                    ex_logger.exception("su_disconenct {}".format(msg))
                else:
                    device.data_handler.send_data(msg)

def send_disconnect_msg(thread):
    if thread.connected_sid != None:
        for sid in thread.connected_sid:
            data = {
                'disconnect': True,
                'sid': sid
            }
            try:
                json_data = json.dumps(data)
            except Exception:
                ex_logger.exception("send_disconnect_msg {}".format(json_data))
            else:
                send_msg_to_su(json_data)
