from database_connection import Database


def host_name_table():
    database = Database()
    q = '''
    CREATE TABLE HostName (
        clientId INTEGER PRIMARY KEY,
        name text
        )
    '''
    database.create_table(q)

host_name_table()



