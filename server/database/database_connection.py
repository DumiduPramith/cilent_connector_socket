import sqlite3

class Database:
    def __init__(self):
        self.connection = sqlite3.connect('/mnt/d/Python/python_socket/server/test.db')
        self.c = self.connection.cursor()
    
    def __del__(self):
        self.connection.close()

    def run_query(self, query):
        self.c.execute(query)
        self.connection.commit()
    def create_table(self, query):
        self.run_query(query)
        self.connection.commit()
    def get_data(self, query):
        self.run_query(query)
        raw_data = self.c.fetchall() 
        self.c.close()
        return raw_data