import mysql.connector
#database class to handle all database operations
class Database:
    def __init__(self):
        self.connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='enter your password here',
            database='library_db'
        )
        self.cursor = self.connection.cursor()

    def close_connection(self):
        self.cursor.close()
        self.connection.close()

    def execute_query(self, query, params=None):
        self.cursor.execute(query, params)
        self.connection.commit()

    def fetch_all(self, query, params=None):
        self.cursor.execute(query, params)
        result = self.cursor.fetchall()
        self.cursor.fetchall()
        return result

    def fetch_one(self, query, params=None):
        self.cursor.execute(query, params)
        result = self.cursor.fetchone()
        self.cursor.fetchall()
        return result