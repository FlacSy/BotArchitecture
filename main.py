import os
import asyncio
import importlib.util
from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode

from managers import ConfigManager
from utils.logger import Logger

from bot.user.handlers.router.user_router import user_router 

config_manager = ConfigManager() 
TOKEN = config_manager.get_config_value('Bot', 'BotToken')

dp = Dispatcher()

async def register_routers():
    dp.include_router(user_router)

async def load_modules(directories, ignore_files = ["__init__.py"]):
    for directory in directories:
        for filename in os.listdir(directory):
            if str(filename).endswith(".py") and filename not in ignore_files:
                module_name = os.path.splitext(filename)[0]
                spec = importlib.util.spec_from_file_location(module_name, os.path.join(directory, filename))
                module = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(module)

async def main():
    print('\033[32mБот запущен!\033[39m')
    bot = Bot(TOKEN, parse_mode=ParseMode.MARKDOWN)
    await register_routers()
    dirs = ["./bot/user/handlers/commands", "./bot/user/handlers/messages", "./bot/user/handlers/callbacks"]  
    await load_modules(dirs) 
    await dp.start_polling(bot)
    
if __name__ == "__main__":
    logger = Logger()
    asyncio.run(main())