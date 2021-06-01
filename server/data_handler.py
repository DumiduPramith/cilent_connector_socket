from _cmd_.command_checker import cmd_check

HEADER = 64
FORMAT = 'utf-8'
class DataHandler:
    def __init__(self,socket):
        self.socket = socket

    def receive_data(self):
        is_cmd = False
        data = self.socket.recv(HEADER).decode(FORMAT)
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
        try:
            new_value = length + b' ' * (HEADER - val_len-1) + b'|' + msg.encode(FORMAT)
        except:
            new_value = length + b' ' * (HEADER - val_len-1) + b'|' + msg
        return new_value
