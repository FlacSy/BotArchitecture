import sqlite3
import logging

class SQLiteDatabaseManager:
    def __init__(self, db_name = "database/bot.db"):
        self.db_name = db_name
        self.conn = None
        self.cursor = None

    def __enter__(self):
        try:
            self.conn = sqlite3.connect(self.db_name)
            self.cursor = self.conn.cursor()
            logging.info(f"Connected to the database: {self.db_name}")
            return self.cursor
        except sqlite3.Error as e:
            logging.error(f"Error connecting to the database: {e}")
            raise

    def __exit__(self, exc_type, exc_value, traceback):
        if self.cursor:
            self.cursor.close()
            logging.info("Cursor closed")
        if self.conn:
            self.conn.commit()
            self.conn.close()
            logging.info("Connection closed")

        if exc_type is not None:
            logging.error(f"An error occurred: {exc_type}, {exc_value}")

        return False

#
#                       Пример использования 
#
#    
# with SQLiteDatabaseManager() as cursor:
#     # Выполняем SQL-запросы
#     cursor.execute('''CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT, age INTEGER)''')
#     cursor.execute('''INSERT INTO users (name, age) VALUES (?, ?)''', ('John Doe', 25))
#
#
# # Запрос данных
# with SQLiteDatabaseManager() as cursor:
#     cursor.execute("SELECT * FROM users")
#     rows = cursor.fetchall()
#     for row in rows:
#         print(row)
