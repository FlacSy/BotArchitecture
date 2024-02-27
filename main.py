import asyncio
from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode

from config.config_manager import ConfigManager
from utils.logger import Logger

from bot.user.handlers.commands.help import help_router
from bot.user.handlers.commands.start import start_router

config_manager = ConfigManager() 
TOKEN = config_manager.get_config_value('Bot', 'BotToken')

dp = Dispatcher()

async def register_routers():
    dp.include_router(start_router)
    dp.include_router(help_router)

async def main():
    print('\033[32mБот запущен!\033[39m')
    bot = Bot(TOKEN, parse_mode=ParseMode.MARKDOWN)
    await register_routers()
    await dp.start_polling(bot)
    
if __name__ == "__main__":
    logger = Logger()
    asyncio.run(main())