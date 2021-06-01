from thread_handler import connected_devices

def show_connected_devices():
    for device in connected_devices:
        print(device.user_name)
        print(device.user_id)