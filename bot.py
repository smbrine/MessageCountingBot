from aiogram import Bot, Dispatcher
import logging
from config_reader import config
import handlers.root_handler as root_handler
import handlers.count_messages as count_messages
import asyncio
from aiogram.fsm.storage.memory import MemoryStorage

logging.basicConfig(level=logging.INFO)

async def main():
    bot = Bot(token=config.bot_token.get_secret_value())
    storage = MemoryStorage()
    dp = Dispatcher(storage=storage)
    dp.include_router(root_handler.router)
    dp.include_router(count_messages.router)
    
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
    
    




