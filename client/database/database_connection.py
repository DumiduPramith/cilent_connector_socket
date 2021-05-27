import sqlite3

class Database:
    def __init__(self):
        self.connection = sqlite3.connect('/mnt/d/Python/python_socket/client/test.db', check_same_thread=False)
        self.c = self.connection.cursor()
    def run_query(self, query):
        self.c.execute(query)
    
    def commit_query(self):
        self.connection.commit()
    def create_table(self, query):
        self.run_query(query)
        self.connection.commit()
    def get_data(self, query):
        self.run_query(query)
        return self.c.fetchall()    
    def close_connection(self):
        self.connection.close()