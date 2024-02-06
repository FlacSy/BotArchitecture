import re
import logging
import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram import executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage  
from config.secrets import BOT_TOKEN
from bot.handlers import start, help
from utils import helpers

storage = MemoryStorage()

bot = Bot(token=BOT_TOKEN, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot, storage=storage)

logging.info('Bot has been started')

async def register_handlers():
    # Хендлеры команд
    dp.register_message_handler(start.start_command, commands=['start', 'about'])
    dp.register_message_handler(help.help_command, commands=['help', 'info'])

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(register_handlers())
    executor.start_polling(dp, on_startup=helpers.on_startup, on_shutdown=helpers.on_shutdown, skip_updates=True)