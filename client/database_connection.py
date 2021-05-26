import sqlite3

class Database:
    def __init__(self):
        self.connection = sqlite3.connect('/mnt/d/Python/python_socket/client/test.db')
        self.c = self.connection.cursor()
    def run_query(self, query):
        self.c.execute(query)
  
    def create_table(self, query):
        self.run_query(query)
        self.connection.commit()
    def get_data(self, query):
        self.run_query(query)
        return self.c.fetchall()    
    def close_connection(self):
        self.connection.close()