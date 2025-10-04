from aiogram import Dispatcher
from .start import register_start_handlers
from .send_code import register_send_code_handlers

def register_all_handlers(dp: Dispatcher):
    register_start_handlers(dp)
    register_send_code_handlers(dp)
