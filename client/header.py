HEADER = 64

def set_header(value):
    val_len = len(str(len(value)))
    length = str(len(value)).encode('utf-8')
    new_value = length + b' ' * (HEADER - val_len-1) + b'|' + value
    return new_value
