from database_connection import Database

database = Database()

def client_table():
    q = '''
    CREATE TABLE client (
        clientId INTEGER PRIMARY KEY AUTOINCREMENT,
        name text,
        last_login TIMESTAMP CURRENT_TIMESTAMP
        )
    '''
    database.create_table(q)

client_table()