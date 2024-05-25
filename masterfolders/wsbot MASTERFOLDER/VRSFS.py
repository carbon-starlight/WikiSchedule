# VK regular schedule forward setup

# Send the VK bot a message with the following text: "!srsf <table_id>" to schedule a regular forward

getpage_language = 'russian'

import asyncio
from vkbottle import Keyboard, KeyboardButtonColor, Text
import os
# from vkbottle import API

import json
import timeit
import time
import vkbottle
from vkbottle.bot import Bot, Message

import tracemalloc
tracemalloc.start(100)
# TODO: remove
from vkbottle import DocMessagesUploader

from vkbottle import PhotoMessageUploader
from vkbottle.bot import Bot
from vkbottle import VKAPIError

import schedule

import sys
# print(sys.path)
import io
import rich
from rich.traceback import install
install(show_locals=True)

import os
# os.chdir('C:/Users/qwert/wsbot foulder')

# sys.path.append('C:/Users/qwert/wsbot foulder')
# allows to execute functions from wsbot in this directory
# TODO: move to a more convinient, obvious for end user to specify own place

# import C:/Users/qwert/wsbot foulder/mainArray.json
# from wsbot import today_command, getCurrentTemporalInfo, getWeekCalendarBoundaries, getWeekArray, get_room_number_weekArray
# import wsbot

import re

data_file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'config.json'))

# Open the config.json file
with open(data_file_path) as file:
    data = json.load(file)

token = data['vk_bot_token']
# print('Token:', token)

# token = ""
bot = Bot(token=token)
photo_uploader = PhotoMessageUploader(bot.api)

@bot.on.message(text="!srsf <table_id>")
@bot.on.message(text="<handle> !srsf <table_id>")
async def srsf(message: Message):
    """Start regular schedule forward"""
    # print('MSGv')
    # print(message)
    # print(Message)
    # print("^M|VALSv")
    # print(id)
    # print(handle)

    words_list = message.text.split()

    # Retrieve the last word using negative indexing
    table_id = words_list[-1]

    # print('TID', table_id)

    # print(message.peer_id, 'pppiii')
    # ^ message peer id to later send message to the group

    # await bot.api.messages.send(peer_id=339422353, message="srsf^!^", random_id=0)

    append_to_forwardClientList_json(message.peer_id, table_id)

    await message.answer(f'srsf set successfully: {message.peer_id} -- {table_id}')


def append_to_forwardClientList_json(peer_id, table_id, filename='forward_group-table_dictionary.json'):
    """Append a key-value pair to a JSON dictionary of forward dictionary with peer_id/table_id pairs.

    Args:
    peer_id (str): Key to be added -- to what group send regular data.
    table_id (str): Value associated with the key -- from what table to harvest the regular data.
    filename (str, optional): Name of the JSON file to be used. Defaults to 'forward_group-table_dictionary.json'.
    """

    #  in case if I will try to implement multiple tables for 1 row
    # if table_id contains '^&&^':

    # Try to read the existing JSON file
    try:
        with open(filename, 'r') as file:
            data = json.load(file)
    except FileNotFoundError:
        # If the file does not exist, create a new dictionary
        data = {}

    # Append the key-value pair
    data[peer_id] = table_id

    # Write the updated dictionary back to the file
    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)
        print('file {} updated'.format(filename))


def remove_from_forwardClientList_json(peer_id, filename='forward_group-table_dictionary.json'):
    """Codeium suggested this function as a whole when I was going for the function to schedule.

    I decided to accept, bun I don't think I'll ever use it.
    
    Remove a key-value pair from a JSON dictionary of forward dictionary with peer_id/table_id pairs.

    Args:
    peer_id (str): Key to be removed -- from what group send regular data.
    filename (str, optional): Name of the JSON file to be used. Defaults to 'forward_group-table_dictionary.json'.
    """
    # Try to read the existing JSON file
    try:
        with open(filename, 'r') as file:
            data = json.load(file)
    except FileNotFoundError:
        # If the file does not exist, do nothing
        return

    # Remove the key-value pair
    if peer_id in data:
        del data[peer_id]

    # Write the updated dictionary back to the file
    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)
        print('file {} updated'.format(filename))


bot.run_forever()