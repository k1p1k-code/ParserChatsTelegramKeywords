from core.loader_bot import bot
from handlers import dp
from core.loader_client import client_parse
import asyncio


async def start_bot(dp, bot):
    event_loop.create_task(dp.start_polling(bot))

if __name__ == '__main__':  
    event_loop = asyncio.new_event_loop()
    event_loop.create_task(client_parse.runner())
    event_loop.run_until_complete(start_bot(dp, bot))
    event_loop.run_forever()
    