import logging
import asyncio
import json
from collections import defaultdict
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor

# Set up logging
logging.basicConfig(level=logging.INFO)

# Replace <TOKEN> with your actual bot token
TOKEN = "<TOKEN>"
bot = Bot(TOKEN)
dp = Dispatcher(bot)

# Initialize message count dictionary
message_counts = defaultdict(int)

# Load message counts from file if it exists
try:
    with open('message_counts.json', 'r') as f:
        message_counts = defaultdict(int, json.load(f))
except FileNotFoundError:
    pass

# Handle incoming messages
@dp.message_handler()
async def count_messages(message: types.Message):
    if message.chat.type == types.ChatType.GROUP or message.chat.type == types.ChatType.SUPERGROUP:
        message_counts[message.from_user.id] += 1
        await bot.send_message(message.chat.id, f"Message count for user {message.from_user.id}: {message_counts[message.from_user.id]}")
        # Save message counts to file
        with open('message_counts.json', 'w') as f:
            json.dump(dict(message_counts), f)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)