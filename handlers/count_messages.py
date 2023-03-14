# -*- coding: utf-8 -*-
from aiogram import Router
import json
from aiogram import Bot, types
from aiogram.filters import Command, Text
from aiogram.fsm.context import FSMContext
from aiogram.exceptions import TelegramBadRequest as BadRequest



router = Router()

# initialize an empty dictionary to store the message counts

group_data = {}

with open("message_counts.json", "r", encoding='utf-8') as f:
    message_counts = json.load(f)
    
message_counts = {}
for group_id, user_data in group_data.items():
    message_counts[group_id] = {}
    for user_id, messages in user_data.items():
        message_counts[group_id][int(user_id)] = messages

# handler for counting messages
@router.message()
async def count_messages(message: types.Message, state: FSMContext):
    # Get the current user's ID and the chat ID
    user_id = message.from_user.id
    chat_id = message.chat.id

    # Get the current message count from the user's state
    user_data = await state.get_data()
    message_count = user_data.get("message_count", 0)

    # Increment the message count and update the user's state
    message_count += 1
    await state.set_data({"message_count": message_count})

    # Load the group data from the file
    with open("group_data.json", "r") as f:
        group_data = json.load(f)

    # Update the group data with the new message count
    if str(chat_id) not in group_data:
        group_data[str(chat_id)] = {}

    if str(user_id) not in group_data[str(chat_id)]:
        group_data[str(chat_id)][str(user_id)] = {
            "first_name": message.from_user.first_name,
            "message_count": 1
        }
    else:
        group_data[str(chat_id)][str(user_id)]["message_count"] += 1

    # Save the updated group data back to the file
    with open("group_data.json", "w") as f:
        json.dump(group_data, f, ensure_ascii=False)














# async def count_messages(message: types.Message):
    # user_id = message.from_user.id
    
    # with open("message_counts.json", "r+") as f:
    #     message_counts = json.load(f)
        
    #     if str(user_id) not in message_counts:
    #         message_counts[str(user_id)] = 1
    #     else:
    #         message_counts[str(user_id)] += 1
            
    #     f.seek(0)
    #     json.dump(message_counts, f)
    #     f.truncate()
# async def count_messages(message: types.Message):
#     user_id = message.from_user.id
#     group_id = message.chat.id
#     user_name = message.from_user.first_name

#     # Create a new dictionary for the group if it doesn't exist
#     if group_id not in message_counts:
#         message_counts[group_id] = {}
#     # Create a new dictionary for the user if it doesn't exist
#     if user_id not in message_counts[group_id]:
#         message_counts[group_id][user_id] = {"name": user_name, "count": 1}
#     else:
#         message_counts[group_id][user_id]["count"] += 1

#     with open("message_counts.json", "w", encoding='utf-8') as f:
#         json.dump(message_counts, f, ensure_ascii=False, indent=4)
    
