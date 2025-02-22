from aiogram import Dispatcher, Bot
from aiogram.client.default import DefaultBotProperties
from aiogram.fsm.storage.memory import MemoryStorage
from config import token, chats, words, chat_send
from pyrogram.types import Message
from pyrogram.types import Chat

async def get_me():
    username=await bot.me()
    username=username.username
    return username

bot=Bot(token, default=DefaultBotProperties(parse_mode="HTML"))
dp=Dispatcher(storage=MemoryStorage())

async def get_client(message: Message, chat: Chat):
    await bot.send_message(chat_send, text=
                           f'🧔Клиент: [{message.from_user.first_name}](tg://openmessage?user_id={message.from_user.id})\n'
                           f'📄 Чат: [{chat.title}]({chat.invite_link})\n'
                           f'💬 Сообщение: {message.text}'
                           , parse_mode="MARKDOWN")
    