from _cmd_.cmd_checker import cmd_check

HEADER = 64
FORMAT = 'utf-8'
class DataHandler:
    def __init__(self,socket):
        self.socket = socket

    def receive_data(self):
        data = self.socket.recv(HEADER).decode(FORMAT)
        is_cmd = False
        if data:
            data = data.strip('|')
            buffer_size = int(data)
            data = self.socket.recv(buffer_size).decode(FORMAT)
            is_cmd = cmd_check(data)
        if not is_cmd:
            return data

    def send_data(self, msg):
        msg = self.set_header(msg)
        self.socket.send(msg)

    def set_header(self,msg):
        val_len = len(str(len(msg)))
        length = str(len(msg)).encode(FORMAT)
        new_value = length + b' ' * (HEADER - val_len-1) + b'|' + msg.encode(FORMAT)
        return new_value
