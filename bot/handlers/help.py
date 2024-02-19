# Обработчики команды /help
from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from config.settings import ASK_START_TEXT

async def help_command(message: types.Message):
    # Обработчик команды /help
    await message.answer(f"<b>Здраствуй, {message.from_user.first_name}</b>"
                         "Вот список доступных команд:\n"
                         "<i>/start</i> - начать работу с ботом\n"
                         "<i>/help</i> - получить справку о доступных командах")


# Регистрация обработчика команды /help
__all__ = ['help_command']
