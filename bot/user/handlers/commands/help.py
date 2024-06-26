from aiogram import types
from aiogram.filters import Command
from main import user_router

@user_router.message(Command('help'))
async def help_command(message: types.Message):

    await message.answer("Вот список доступных команд:\n"
                         "/start - начать работу с ботом\n"
                         "/help - получить справку о доступных командах")