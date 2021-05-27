from database.database_connection import Database

def register_new_user(host_name):
    database = Database()
    data_insert_query = f'''
    INSERT INTO client (name)
    VALUES ("{host_name}");
    '''
    last_insert_id_query = '''
    select last_insert_rowid();
    '''
    database.run_query(data_insert_query)
    host_id = database.get_data(last_insert_id_query)
    host_id = host_id[0][0]
    return host_id


def get_user_name_by_id(user_id):
    user_id = int(user_id)
    database = Database()
    q = f'''
    SELECT name FROM client WHERE clientId={user_id} 
    '''
    user_name = database.get_data(q)[0][0]
    return user_name

