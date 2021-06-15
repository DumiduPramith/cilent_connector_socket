from log import set_logger

ex_logger = set_logger(__name__)
HEADER = 64
FORMAT = 'utf-8'
class DataHandler:
    def __init__(self,socket):
        self.socket = socket
    def receive_data(self):
        from _cmd_.command_checker import cmd_check
        is_cmd = False
        data = self.socket.recv(HEADER).decode(FORMAT)
        if data:
            data = data.strip('|')
            try:
                buffer_size = int(data)
            except Exception:
                ex_logger.exception("")
                return ''
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
