import sqlite3, os

class Database:
    def __init__(self):
        self.connection = sqlite3.connect(os.path.join(os.path.dirname(os.path.dirname(__file__)),"test.db"), check_same_thread=False)
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
        return raw_data