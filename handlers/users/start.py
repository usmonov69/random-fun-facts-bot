from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from loader import dp
from keyboards.inline.engUzKey import engUz

@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f"Assalomu Alaykum👋, {message.from_user.full_name}! tilni tanlang",
    		reply_markup=engUz)
