from .database_connection import Database
import socket
database = Database()

def get_user_data():
    q = '''
    SELECT clientId, name FROM HostName
    '''
    return database.get_data(q)

def add_user_id(id):
    id = int(id)
    host_name = socket.gethostname()
    q = f'''
    INSERT INTO HostName (clientId, name)
    VALUES ({id},"{host_name}");
    '''
    database.run_query(q)
    database.commit_query()

def main():
    data = get_user_data()
    if data == []:
        return False
    else: return data[0][0]
