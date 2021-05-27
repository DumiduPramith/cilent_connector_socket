from _cmd_.cmd_func import add_register_id

def cmd_check(data):
    if data.startswith('__register_id__'):
        raw_data = data.split('|')
        add_register_id(raw_data[1])
        return True
    else: return False
