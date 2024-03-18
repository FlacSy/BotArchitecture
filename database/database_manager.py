import aiosqlite
import logging

class SQLiteDatabaseManager:
    def __init__(self, mode: str = "development"):
        """
        Параметр `mode` это режим для базы данных. Возможные значения: 'development' для розроботки, 'production' для продакшина
        """
        self.mode = mode
        self.conn = None
        self.cursor = None

    async def __aenter__(self):
        try:
            if self.mode == "development":
                self.conn = await aiosqlite.connect("./development/development.db")

            elif self.mode == "production":
                self.conn = await aiosqlite.connect("./production/production.db")
            else:
                self.conn = await aiosqlite.connect("./development/development.db")
            self.cursor = await self.conn.cursor()
            logging.info(f"Connected to the database: {self.mode}")
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