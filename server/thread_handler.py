import threading

lock = threading.Lock()

connected_devices = []

def add_new_thread(thread):
    lock.acquire()
    connected_devices.append(thread)
    lock.release()

def remove_thread(thread):
    for count, saved_thread in enumerate(connected_devices):
        if saved_thread is thread:
            lock.acquire()
            del connected_devices[count]
            lock.release()
            print("device removed from list")
            break

def set_su():
    thread = threading.current_thread()
    print("user name su set")
    thread.user_name = 'su'

def set_sid(client_id, sid):
    for device in connected_devices:
        if device.user_id != None:
            if int(device.user_id) == client_id:
                device.connected_sid.append(sid)
                return True
    return False

def remove_sid(sid):
    for device in connected_devices:
        if device.connected_sid != []:
            for count,list_sid in enumerate(device.connected_sid):
                if str(list_sid) == sid:
                    lock.acquire()
                    del device.connected_sid[count]
                    lock.release()
                    break
            else: continue
            break

def send_msg_to_client(sid, rawdata):
    for device in connected_devices:
        # print("user id",device.user_id)
        if device.connected_sid != []:
            for list_sid in device.connected_sid:
                if str(list_sid) == str(sid):
                    device.data_handler.send_data(rawdata)
                    # print("sended msg1", rawdata)
                    break
            else: continue
            break

def send_msg_to_su(data):
    for device in connected_devices:
        if device.user_name != None:
            if device.user_name == 'su':
                # print("data sended su")
                device.data_handler.send_data(data)
                # print("sended msg2", data)
                break