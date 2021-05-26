from database_connection import Database

database = Database()
def host_name_table():
    q = '''
    CREATE TABLE HostName (
        clientId INTEGER PRIMARY KEY,
        name text
        )
    '''
    database.create_table(q)

# host_name_table()



