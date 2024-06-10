from aiogram import types
from managers import DatabaseManager
from aiogram.filters import CommandStart
from main import user_router

@user_router.message(CommandStart())
async def start_command(message: types.Message):
    await message.answer(f"*Здраствуй, {message.from_user.first_name}*\n" 
                         "/help для отображения списка команд.")

    user_id = message.from_user.id
    username = message.from_user.username

    async with DatabaseManager() as cursor:
        await cursor.execute('''CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username TEXT, user_id INTEGER)''')  
        await cursor.execute('''INSERT INTO users (username, user_id) VALUES (?, ?)''', (username, user_id))
