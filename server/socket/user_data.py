class UserData:
    def __init__(self,user_name, user_id, sid, password=None):
        self.user_name = user_name
        self.user_id = user_id
        self.connected_sid = sid
        self.password = password