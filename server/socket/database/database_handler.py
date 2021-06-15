from database.database_connection import Database
database = Database()
from log import set_logger

logger = set_logger(__name__)

def register_new_user(host_name):
    data_insert_query = f'''
    INSERT INTO client (name)
    VALUES ("{host_name}");
    '''
    last_insert_id_query = '''
    select last_insert_rowid();
    '''
    try:
        database.run_query(data_insert_query)
        host_id = database.get_data(last_insert_id_query)
    except Exception:
        logger.exception("register_new_user")
    else:
        logger.info(f"new user registered [user_name:{host_name}, user_name:{host_id}]")
        try:
            host_id = host_id[0][0]
        except IndexError:
            logger.exception(f"register_new_user [host_id: {host_id}]")
        else:
            return host_id

def add_password(password):
    import threading
    cur_thread = threading.current_thread()
    clientid = cur_thread.user_id
    q = f'''
    UPDATE client SET 
    password={password}
    WHERE clientId = {clientid}
    '''
    try:    
        database.run_query(q)
        logger.info(f"password added to database [client_id: {clientid}]")
        logger.debug(f"password added to database [client_id: {clientid}, password: {password}]")
    except Exception:
        logger.exception(f"add_password [query: {q}]")

def get_user_name_by_id(user_id):
    user_id = int(user_id)
    q = f'''
    SELECT name FROM client WHERE clientId={user_id} 
    '''
    try:
        user_name = database.get_data(q)[0][0]
    except Exception:
        logger.exception(f"get_user_name_by [query: {q}]")
    else:
        return user_name

def password_check(user_id):
    q = f'''
    SELECT password FROM client WHERE clientId={user_id}
    '''
    try:
        password = database.get_data(q)
    except Exception:
        logger.exception(f"password_check [query: {q}]")
    else:
        if isinstance(password[0][0],type(None)):
            return False
        else:
            return password[0][0]