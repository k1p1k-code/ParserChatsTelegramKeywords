from core.loader_bot import dp
from aiogram import types, F
from aiogram.filters import CommandStart


@dp.message()
async def cmd_start(message):
    await message.answer('12')
