from aiogram                    import Bot, Dispatcher
from aiogram.types              import Message
from aiogram.fsm.storage.memory import MemoryStorage
import asyncio
import logging

from config import TOKEN
from handlers import register_all_handlers

logging.basicConfig(level=logging.INFO)
bot = Bot(token=TOKEN)
dp = Dispatcher(storage=MemoryStorage())

async def main():
    register_all_handlers(dp)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())