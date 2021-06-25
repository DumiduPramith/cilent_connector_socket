from _cmd_.cmd_func import register_user, identify_user, archive_cmd, \
    send_error_to_su, send_device_list
from _cmd_.pty_cmd import pty_connect, disconnect, pty_input,\
    pty_resize, pty_output
from thread_handler import set_su
from _cmd_.exec_handler import exec_handler_

def cmd_check(raw_data):
    if raw_data.startswith('__'):
        data = raw_data.split("|")
        if data[0] == '__register_user__':
            register_user(data[1])
        elif data[0] == '__user_id__':
            identify_user(data[1])
        elif data[0] == '__su__':
            set_su()         
        elif data[0] == '__connect__':
            pty_connect(raw_data,data[1])     
        elif data[0] == '__disconnect__':
            disconnect(raw_data, data[1])    
        elif data[0] == '__pty_input__':
            pty_input(raw_data, data[1])
        elif data[0] == '__resize__':
            pty_resize(raw_data, data[1])
        elif data[0] == '__pty_output__':
            pty_output(data[1])
        elif data[0] == '__archive__':
            archive_cmd(raw_data,data[1])
        elif data[0] == '__error__':
            print(data[1])
            send_error_to_su(data[1])
        elif data[0] == '__exec_value__':
            exec_handler_(data[1])
        elif data[0] == '__GET_DEVICES__':
            send_device_list(data[1])
        return True