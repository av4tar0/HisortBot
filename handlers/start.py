from aiogram import Dispatcher
from aiogram.types import Message
from aiogram.filters import Command
import logging

async def start(message : Message):
    await message.answer(f"<b>Привет, {message.from_user.username}!</b>" + "\n" + \
                         "Просто скинь свой нерабочий код, и я постараюсь дать тебе подсказки!", parse_mode="HTML")

def register_start_handlers(dp : Dispatcher):
    dp.message.register(start, Command("start"))
