from thread_handler import connected_devices
from log import set_logger
import threading

logger = set_logger(__name__)

def show_connected_devices():
    device_list = {
        "kasun" : 50
    }
    for device in connected_devices:
        if device is threading.current_thread():
            pass
        else:
            device_list[device.user_name] = device.user_id
    logger.debug(f'device list returned')
    return device_list