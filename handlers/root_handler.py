# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
from aiogram import Router
import json
from aiogram import Bot, types
from aiogram.filters import Command, Text
from aiogram.fsm.context import FSMContext
from aiogram.exceptions import TelegramBadRequest as BadRequest
from aiogram import Router
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
import dic.dictionary as dic

from aiogram import Router
import json
from aiogram import Bot, types
from aiogram.filters import Command, Text
from aiogram.fsm.context import FSMContext

from handlers.count_messages import group_data


router = Router()

with open("group_data.json", "r", encoding='utf-8') as f:
    message_counts = json.load(f)

@router.message(Command(commands=["start"]))
async def cmd_start(msg: Message, state: FSMContext):
    await state.clear()
    await msg.answer(dic.greet_msg)

@router.message(Command(commands=["help"]))
async def cmd_start(msg: Message, state: FSMContext):
    await state.clear()
    await msg.answer(dic.help_msg)
    
@router.message(Command(commands=['start']))
async def welcome(message: types.Message):
    chat_id = message.chat.id
    if chat_id not in group_data:
        group_data[chat_id] = {}
        with open("group_data.json", "w", encoding="utf-8") as f:
            json.dump(group_data, f, ensure_ascii=False)
        await message.reply("Welcome to the chat!")
    else:
        await message.reply("Welcome back to the chat!")

@router.message(Command(commands=['group_stats']))
async def group_stats(message: types.Message):
    group_id = message.chat.id
    user_id = message.from_user.id
    if group_id in group_data:
        data = []
        for user_id, stats in group_data[group_id].items():
            user_name = stats["user_name"]
            message_count = stats["message_count"]
            data.append(f"{user_name}: {message_count} messages")
        if data:
            await message.answer("\n".join(data), parse_mode='HTML')
        else:
            await message.answer("No message data for this group yet.")
    else:
        await message.answer("No message data for this group yet.")

@router.message(Command(commands=['my_stats']))
async def my_stats(message: types.Message):
    group_id = message.chat.id
    user_id = message.from_user.id
    if group_id in group_data and user_id in group_data[group_id]:
        user_name = group_data[group_id][user_id]["user_name"]
        message_count = group_data[group_id][user_id]["message_count"]
        await message.answer(f"You wrote {message_count} messages in this group chat, {user_name}.")
    else:
        await message.answer("No message data for you in this group yet.")
