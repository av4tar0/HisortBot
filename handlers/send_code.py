from aiogram import Dispatcher, types, F
from aiogram.types import Message
from aiogram.filters import Command

from ai.analysis import analyze_code

import logging
import asyncio

async def send_code(message : Message):
    logging.info("Поступил запрос на пояснение кода.")
    code_snippet = message.text.strip()
    
    if not code_snippet or len(code_snippet) < 10:
        await message.answer("Пожалуйста, отправьте код для анализа.", parse_mode="HTML")
        return
    
    await message.answer("<i>Ваша заявка поступила в очередь, ожидайте...</i>", parse_mode="HTML")
    
    async def process_code():
        answer_ai = await analyze_code(code_snippet)    
        await message.answer(f"{answer_ai}", parse_mode="HTML")
    
    asyncio.create_task(process_code())

def register_send_code_handlers(dp : Dispatcher):
    dp.message.register(send_code, F.text & ~F.text.startswith('/'))
