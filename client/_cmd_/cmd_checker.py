from _cmd_.cmd_func import add_register_id
from _cmd_.pty_cmd import pty_connect, disconnect, pty_input, pty_resize

def cmd_check(raw_data):
    if raw_data.startswith('__'):
        data = raw_data.split("|")
        if data[0] == ('__register_id__'):
            add_register_id(raw_data[1])
            return True
        elif data[0] == '__connect__':
            pty_connect(data[1])
            return True
        elif data[0] == '__disconnect__':
            disconnect(data[1])
            return True
        elif data[0] == '__pty_input__':
            pty_input(data[1])
            return True
        elif data[0] == '__resize__':
            pty_resize(data[1])
            return True
    else: return False
