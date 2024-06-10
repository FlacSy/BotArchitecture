import aiosqlite
import logging

class DatabaseManager:
    def __init__(self):
        self.conn = None
        self.cursor = None

    async def __aenter__(self):
        try:
            self.conn = await aiosqlite.connect("./local/database.sql")
            self.cursor = await self.conn.cursor()
            logging.info(f"Connected to the database")
            return self.cursor
        except aiosqlite.Error as e:
            logging.error(f"Error connecting to the database: {e}")
            raise

    async def __aexit__(self, exc_type, exc_value, traceback):
        if self.cursor:
            await self.cursor.close()
            logging.info("Cursor closed")
        if self.conn:
            await self.conn.commit()
            await self.conn.close()
            logging.info("Connection closed")

        if exc_type is not None:
            logging.error(f"An error occurred: {exc_type}, {exc_value}")

        return False