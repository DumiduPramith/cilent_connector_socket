from _cmd_.cmd_func import register_user, identify_user
from _cmd_.pty_cmd import pty_connect, disconnect, pty_input, pty_resize, pty_output
from thread_handler import set_su

def cmd_check(raw_data):
    if raw_data.startswith('__'):
        data = raw_data.split("|")
        if data[0] == '__register_user__':
            register_user(data[1])
        elif data[0] == '__user_id__':
            identify_user(data[1])
        elif data[0] == '__su__':
            set_su()
            return True
        elif data[0] == '__connect__':
            pty_connect(raw_data,data[1])
            return True
        elif data[0] == '__disconnect__':
            disconnect(raw_data, data[1])
            return True
        elif data[0] == '__pty_input__':
            pty_input(raw_data, data[1])
            return True
        elif data[0] == '__resize__':
            pty_resize(raw_data, data[1])
            return True
        elif data[0] == '__pty_output__':
            pty_output(data[1])
            return True

