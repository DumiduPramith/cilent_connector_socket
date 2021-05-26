HEADER = 64
FORMAT = 'utf-8'
class DataHandler:
    def __init__(self):
        pass
    @staticmethod
    def receive_data(socket):
        data = socket.recv(HEADER).decode(FORMAT)
        if data:
            buffer_size = int(data)
            data = socket.recv(buffer_size).decode(FORMAT)
        return data
    @staticmethod
    def send_data(socket, msg):
        msg = DataHandler.set_header(msg)
        socket.send(msg)
    @staticmethod
    def set_header(msg):
        val_len = len(str(len(msg)))
        length = str(len(msg)).encode(FORMAT)
        new_value = length + b' ' * (HEADER - val_len-1) + b'|' + msg.encode(FORMAT)
        return new_value
