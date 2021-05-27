from _cmd_.cmd_func import register_user, identify_user

def cmd_check(data):
    if data.startswith('__'):
        data = data.split("|")
        if data[0] == '__register_user__':
            register_user(data[1])
        elif data[0] == '__user_id__':
            identify_user(data[1])

