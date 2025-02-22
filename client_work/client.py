from pyrogram import Client
from pyrogram import types
from core.loader_bot import get_client, get_me, chats, words
from pyrogram.enums import ChatType
from config import chats

class client_parse():
    def __init__(self, session, api_id, api_hash):
        self.__client=Client("session/session", api_id=api_id, api_hash=api_hash, device_model='Parsing', system_version='0.19', lang_code='ru')


    def runner(self):
        @self.__client.on_message()
        async def my_handler(client, message: types.Message):
            if str(message.chat.id) in chats:
                for i in words:
                    for t in message.text.split(' '):
                        print(t)
                        print(i)
                        if i in t:
                            if message.chat.type in [ChatType.GROUP, ChatType.SUPERGROUP]:
                                chat=await self.__client.get_chat(message.chat.id)
                                await get_client(message, chat)
                                break
            


        self.__client.run()
