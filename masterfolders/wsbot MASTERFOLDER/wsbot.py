
# FINISH:
#
#   getToLesFromCurrent():
#   subgroup level
#   go to line print('User {username} is allowed in table {subarray[4]} according to {subarray}') and check the functional
#   today
#   start_command has some ti testing, remove
#   make mv command move distant homework, update documentation
#

from __future__ import annotations
import datetime
from datetime import datetime
from datetime import timedelta
import time
import pickle
#import numpy as np
import json
import random
import itertools
import string
import sqlite3
import asyncio
import textwrap
# from tabulate import tabulate
# import tabulate_cell_merger.tabulate_cell_merger
from sqlite3 import Error
from typing import Final
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo
from telegram.ext import Updater, CallbackContext, CallbackQueryHandler, ConversationHandler
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Application, CallbackQueryHandler, CommandHandler, ContextTypes
from typing import Annotated
from telegram.ext import CallbackQueryHandler, Updater
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import CallbackContext, CallbackQueryHandler, Updater
# import aiogram
# # from aiogram import Bot, Dispatcher, executor, types
# from aiogram.utils import executor
# from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Application, CallbackQueryHandler, CommandHandler, ContextTypes
from telegram import Update, ReplyKeyboardMarkup
import sys
import traceback
import tracemalloc
# tracemalloc.start()
# ↑ REMOVE IN PRODUCTION
# import schedule
import time
import gettext
_ = gettext.gettext
fileMA = None
user_id = None
"""Should be declared as update.message.chat.id in every function prior to calling getUserInfo()"""
# Should be declared as update.message.chat.id in every function prior to calling getUserInfo()
#user_id = Annotated[int, "Should be declared as update.message.chat.id in every function prior to calling getUserInfo()"]
# print(user_id)


import os
import json

from rich import traceback
traceback.install(show_locals=True)
traceback_mode_is_rich = True

from rich.console import Console
console = Console()
from rich.text import Text
from io import StringIO


def extract_configuration_data_dictionary_from_config_json():
    """extracts given data from config.json"""
    # Navigate to the directory containing config.json
    data_file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'config.json'))

    # Open the config.json file
    with open(data_file_path) as file:
        config_data_dictionary = json.load(file)
    
    # print(config_data_dictionary)
    return config_data_dictionary

# Navigate to the directory containing config.json
data_file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'config.json'))

# Open the config.json file
with open(data_file_path) as file:
    data = json.load(file)

bot_username = data['telegram_bot_username']
print('Bot username:', bot_username)

# Access the value of the telegram_token key
telegram_bot_token = data['telegram_bot_token']
# print('Telegram token:', telegram_bot_token)

DEVELOPER_CHAT_ID = data['developer_telegram_chat_id']
print('DEVELOPER_CHAT_ID:', DEVELOPER_CHAT_ID)

TOKEN: Final = telegram_bot_token
BOT_USERNAME: Final = bot_username


# aiogram part
# bot = Bot(token=TOKEN)
# dp = Dispatcher(bot)


async def getCurrentTemporalInfo():
    """Get current_week_utc (int, UTC), current_day_utc (in week, 1-7), current_week_utz (int, user time zone), current_day_utz (in week, 1-7) current_lesson_num_utz and current_lesson_id_utz
    
    current_week_utc, current_day_utc, current_week_utz, current_day_utz, [IN DEVELOPMENT] current_lesson_num_utz, current_lesson_id_utz

    Call after getUserInfo(), needs global utz"""
    print('EXECUTING GETCURRENTTEMPORALINFO')
    start_gcti_exec_timestamp = time.time()
    # 1688947200 is Monday, 10 July 2023 г., 0:00:00 UTC
    global current_week_utc
    global current_day_utc
    global current_week_utz
    global current_day_utz
    global adding_from_week
    current_lesson_num_utz, current_lesson_id_utz = None, None
    current_week_utc = (time.time() - 1688947200) // 604800
    current_day_utc = (time.time() - 1688947200) % 604800 // 86400 + 1
    current_week_utz = (time.time() + utz - 1688947200) // 604800
    current_day_utz = (time.time() + utz - 1688947200) % 604800 // 86400 + 1
    #current_lesson_num_utz = 
    #current_lesson_id_utz = 
    # print(current_week_utc)
    # print(current_day_utc)
    # print(current_week_utz)
    # print(current_day_utz)
    print('END OF GETCURRENTTEMPORALINFO EXECUTION IN', time.time() - start_gcti_exec_timestamp)
    return current_week_utc, current_day_utc, current_week_utz, current_day_utz, current_lesson_num_utz, current_lesson_id_utz


utz = +14400
table_user_in = None
# asyncio.run(getCurrentTemporalInfo()) # breaks everything, likely not needed
current_week_utc = None
current_day_utc = None
current_week_utz = None
current_day_utz = None
weekArray = []
"""all lessons in a week, don't forget to clear"""
mainArray = []
adding_from_week = current_week_utz
semigraphic_mode_on = True


def isinteger(string):
    try:
        int(string)
        return True
    except ValueError:
        return False
    

async def getUserInfo(user_id, username = None):
    """Get what table the user is in, it's tz (as utz), their semigraphic_mode_on and where they are allowed as an admin or a contributor"""
    print('EXECUTING GETUSERINFO')
    start_gui_exec_timestamp = time.time()
    global utz
    global table_user_in
    global tables_user_admin_in
    global tables_user_allowed_in
    global semigraphic_mode_on
    tables_user_admin_in = []
    tables_user_allowed_in = []
    #user_id = update.message.chat.id
    semigraphic_mode_on = True

    with open('mainArray.json', 'r') as fileMA:
        mainArray = json.load(fileMA)
        

    for subarray in mainArray:
        if (
                #?(subarray[2] == user_id or subarray[2] == str(user_id) or subarray[2] == int(user_id))
                subarray[2] == user_id
                and subarray[3] == 'lg'
                and subarray[10] == 0
            ):
                table_user_in = (subarray[4])
                utz = subarray[9]
                
    for subarray in reversed(mainArray):
        if (
                subarray[2] == user_id
                and subarray[3] == 'cs'
                and subarray[10] == 0
            ):
                tables_user_admin_in.append(subarray[4])

    for subarray in reversed(mainArray):
        if (
                (subarray[8] == str(user_id)
                or (subarray[8] == username and username != None))
                and subarray[3] == 'au'
                and subarray[10] == 0
        ):
                tables_user_allowed_in.append(subarray[4])
                # print(f'User {username} is allowed in table {subarray[4]} according to {subarray}')


    with open('sg_toggle_logs.json', 'r') as stf:
        stfA = json.load(stf)

    for subarray in stfA:
        if (
                subarray[2] == user_id
                and subarray[3] == 'ts'
                and subarray[10] == 0
            ):
                semigraphic_mode_on = subarray[8]
                # print("semigr mode set to " + str(semigraphic_mode_on))

    # print('in func getUserInfo: ', mainArray)
    # print('in func getUserInfo: table_user_in:', table_user_in)
    print('END OF GETUSERINFO EXECUTION IN', time.time() - start_gui_exec_timestamp)

    return semigraphic_mode_on, tables_user_admin_in, tables_user_allowed_in, table_user_in, utz

def getTableTemporalInfoFromMainArray(table_id):
    """Returnes an array with every lesson start/end times"""
    with open('mainArray.json', 'r') as fileMA:
        mainArray = json.load(fileMA)

    # res0|   time    |contrib_id| type  |table| w |d |l |cntnt|utz |vl|rg|ex|rn|r6
    #   0, 1689546503, 5725753364, 'cs', '1-HAL', 0, 0, 0, 't', utz, 0, 0, 0, 0, 0],
    #   0      1            2        3      4     5  6  7   8    9   10 11 12 13 14

    # TODO: isn't "reverse" required?
    for subarray in mainArray:
        if (
                subarray[3] == 'set_temporal'
                and subarray[4] == table_id
                and subarray[10] == 0
        ):
            return subarray[8]
    
    ti = []
    for i in range(160):
        ti.append(" N/A ")


async def getToLesFromCurrent(user_id):
    """Get an "add to" week_number, day_of_week and lesson_number based on an ongoing lesson"""
    print('EXECUTING GETTOLESFROMCURRENT')
    start_gtlfc_timestamp = time.time()
    await getUserInfo(user_id)
    await getCurrentTemporalInfo()
    await getWeekArray(table_user_in, current_week_utz)
    daily_week_array = []  # array for a day
    start_index: int = int((current_day_utz - 1) * 10)
    end_index: int = int(start_index + 10)
    # print(start_index, end_index)
    # for i in range(start_index, end_index):
    #     daily_week_array.append(weekArray[i])
    # #     print('appending')
    # filename = f"{table_user_in}_temporal_info.json"
    # with open(filename, 'r') as fileTI:
    #     ti = json.load(fileTI)
    ti = getTableTemporalInfoFromMainArray(table_user_in)
    if current_day_utz == 1:
        day_lesson_t_starts = [ti[20], ti[22], ti[24], ti[26], ti[28], ti[30], ti[32], ti[34], ti[36], ti[38]]
    if current_day_utz == 2:
        day_lesson_t_starts = [ti[40], ti[42], ti[44], ti[46], ti[48], ti[50], ti[52], ti[54], ti[56], ti[58]]
    if current_day_utz == 3:
        day_lesson_t_starts = [ti[60], ti[62], ti[64], ti[66], ti[68], ti[70], ti[72], ti[74], ti[76], ti[78]]
    if current_day_utz == 4:
        day_lesson_t_starts = [ti[80], ti[82], ti[84], ti[86], ti[88], ti[90], ti[92], ti[94], ti[96], ti[98]]
    if current_day_utz == 5:
        day_lesson_t_starts = [ti[100], ti[102], ti[104], ti[106], ti[108], ti[110], ti[112], ti[114], ti[116], ti[118]]
    if current_day_utz == 6:
        day_lesson_t_starts = [ti[120], ti[122], ti[124], ti[126], ti[128], ti[130], ti[132], ti[134], ti[136], ti[138]]
    if current_day_utz == 7:
        day_lesson_t_starts = [ti[140], ti[142], ti[144], ti[146], ti[148], ti[150], ti[152], ti[154], ti[156], ti[158]]
    
    epoch_t_starts = []
    for i in range(0, len(day_lesson_t_starts)):
        epoch_t_starts.append((int((str(day_lesson_t_starts[i]))[0:2]))*60*60 + (int((str(day_lesson_t_starts[i]))[3:5]))*60)
        # print(epoch_t_starts)

        # current_week_utc = (time.time() - 1688947200) // 604800
        # current_day_utc = (time.time() - 1688947200) % 604800 // 86400 + 1
        # current_week_utz = (time.time() + utz - 1688947200) // 604800
        # current_day_utz = (time.time() + utz - 1688947200) % 604800 // 86400 + 1

    for el in epoch_t_starts:
        el = el + 1688947200 + current_week_utz * 604800 + current_day_utz * 86400 + utz

    # print(epoch_t_starts)

    for i in range(1, 11):
        if epoch_t_starts[i-1] < time.time() + utz:
            current_lesson = i
            """int, 1-10"""
            break

    curLesNumInWA = int((current_day_utz - 1) * 10 + (current_lesson - 1))

    current_lesson_id = weekArray[curLesNumInWA]

    current_week_utz__to_edit = current_week_utz

    for i in range(1, 11):
        if epoch_t_starts[i-1] > time.time() + utz:
            current_lesson = i
    
    next_of_kind_lesson = None
    """num in all weekArray"""
    iteration__les_num = 0

    while next_of_kind_lesson == None and current_week_utz__to_edit < (current_week_utz + 10000):
        for les in weekArray:
            if les == current_lesson_id:
                next_of_kind_lesson = iteration__les_num
                next_of_kind_lesson_week = current_week_utz__to_edit
                # print(les)
                break
            iteration__les_num += 1
        getWeekArray(table_user_in, current_week_utz__to_edit := current_week_utz__to_edit + 1)
        iteration__les_num = 0

    next_of_kind_lesson_in_day = next_of_kind_lesson % 10 + 1
    """number of lesson in day, 1-10"""
    next_of_kind_lesson_day_in_week = next_of_kind_lesson // 10 + 1
    """number in week, 1-7"""

    print('END OF GETTOLESFROMCURRENT EXECUTION IN', time.time() - start_gtlfc_timestamp)

    return next_of_kind_lesson_week, next_of_kind_lesson_day_in_week, next_of_kind_lesson_in_day, current_lesson

'''
# creating a json array
# res0 / time_epoch / contributor_id / type / table / week / day / lesson / content / utz / validity (0 is good) / level (register) / exclusiveness of lesson addition (one-time event? 0. Keep until cancelation? 1.) / room_number / res6 (15)
mainArray = [
  #res0|   time    |contrib_id| type  |table| w |d |l |cntnt|utz |vl|rg|ex|rn|r6
    [0, 1689546503, 5725753364, 'cs', '1-HAL', 0, 0, 0, 't', utz, 0, 0, 0, 0, 0],
]
#    0      1            2        3      4     5  6  7   8    9   10 11 12 13 14
with open('mainArray.json', 'w') as fileMA:
        json.dump(mainArray, fileMA)
'''

new_data = None
"""
res0 / time_epoch / contributor_id / type / table / week / day / lesson / content / utz / validity (0 is good) / level (register) / exclusiveness of lesson addition (one-time event? 0. Keep until cancelation? 1.) / room_number / res6 (15)
```
mainArray = [
   res0|   time    |contrib_id| type  |table| w |d |l |cntnt|utz |vl|rg|ex|rn|r6
    [0, 1689546503, 5725753364, 'cs', '1-HAL', 0, 0, 0, 't', utz, 0, 0, 0, 0, 0],
]
     0      1            2        3      4     5  6  7   8    9   10 11 12 13 14
```
     """


# async def add_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     keyboard = [[InlineKeyboardButton("Fill Form", web_app=WebAppInfo(url="https://127.0.0.1:5000/form"))]]
#     reply_markup = InlineKeyboardMarkup(keyboard)
#     await update.message.reply_text('Please fill this form:', reply_markup=reply_markup)


async def getWeekArray(table_user_in, adding_from_week):
    """
    Get the array of lessons for the entire week.
    
    Returns:
        list: A list containing all the lessons 1-10 starting from 0 in a week.
    """
    print('EXECUTING GETWEEKARRAY')
    start_gwa_timestamp = time.time()
    weekArray.clear()
    # print('in func getWeekArray (beginning): adding_from_week: ', adding_from_week)
    await getCurrentTemporalInfo()
    # print('in func getWeekArray (after getCurrentTemporalInfo): adding_from_week: ', adding_from_week)
    # Decode the JSON array to Python object
    with open('mainArray.json', 'r') as fileMA:
        mainArray = json.load(fileMA)

    # print('in func getWeekArray: ', mainArray)
    adding_from_day = 1
    for adding_from_day in range(1, 8):
        for adding_from_lesson in range(1, 11):
            # Iterate through the array in reverse order
            found = False  # Flag to track if a valid subarray is found
            for subarray in reversed(mainArray):
                # default adding_from_week = current_week_utz
                if (
                    subarray[3] == 'al'
                    and subarray[4] == table_user_in
                    and subarray[5] == adding_from_week
                    and subarray[6] == adding_from_day
                    and subarray[7] == adding_from_lesson
                    and subarray[10] == 0
                ):
                    weekArray.append(subarray[8])
                    found = True  # if matching criteria found found = True
                    break
            if not found:
                adding_from_week_for_iteration = adding_from_week
                while found == False and adding_from_week_for_iteration > 0:
                    adding_from_week_for_iteration -= 1
                    for subarray in reversed(mainArray):
                    # default adding_from_week = current_week_utz
                        if (
                            subarray[3] == 'al'
                            and subarray[4] == table_user_in
                            and subarray[5] == adding_from_week_for_iteration
                            and subarray[6] == adding_from_day
                            and subarray[7] == adding_from_lesson
                            and subarray[10] == 0
                            and subarray[12] == 1
                            and found == False
                        ):
                            weekArray.append(subarray[8])
                            found = True
                if found == False:
                    weekArray.append(None)
    # print('in func getWeekArray (end): adding_from_week: ', adding_from_week)
    print('END OF GETWEEKARRAY EXECUTION IN: ', time.time() - start_gwa_timestamp)
    return weekArray


async def getWeekArray_HW(table_user_in, adding_from_week):
    """
    Get the array of hw for the entire week.
    
    Returns:
        weekArray_HW: A list containing all the hw 1-10 starting from 0 in a week.
    """
    print('EXECUTING GETWEEKARRAY_HW')
    start_gwahw_timestamp = time.time()
    await getCurrentTemporalInfo()
    # Decode the JSON array to Python object
    with open('mainArray.json', 'r') as fileMA:
        mainArray = json.load(fileMA)

    # print('in func getWeekArray_HW: ', mainArray)
    weekArray_HW = []
    adding_from_day = 1
    upd_found = True
    """To pass a false state of found down the code to toggle after reassignment"""
    for adding_from_day in range(1, 8):
        for adding_from_lesson in range(1, 11):
            # Iterate through the array in reverse order
            found = False  # Flag to track if a valid subarray is found
            for subarray in mainArray:
                # default adding_from_week = current_week_utz
                if (
                    subarray[3] == 'ah'
                    and subarray[4] == table_user_in
                    and subarray[5] == adding_from_week
                    and subarray[6] == adding_from_day
                    and subarray[7] == adding_from_lesson
                    and subarray[10] == 0
                ):
                    if found == False:  # if data for this lesson isn't here yet
                        weekArray_HW.append(subarray[8])
                    if found == True:  # if we already have something in the allocated cell
                        if subarray[8] != '\empty':
                            if weekArray_HW[-1] != None:
                                weekArray_HW[-1] += "; " + str(subarray[8])
                            else:
                                weekArray_HW[-1] = str(subarray[8])
                        else:
                            weekArray_HW[-1] = None
                            found = False
                            upd_found = False
                    found = True  # if matching criteria found found = True
                    # if upd_found == False:
                        # found = False
            if not found:  # If no valid subarray was found, we append None
                weekArray_HW.append(None)
    # print('in func getWeekArray_HW (end): adding_from_week: ', adding_from_week)
    print('END OF GETWEEKARRAY_HW EXECUTION IN: ', time.time() - start_gwahw_timestamp)
    return weekArray_HW


async def get_room_number_weekArray(table_user_in, adding_from_week):
    """"""
    global room_number_weekArray
    print('EXECUTING GET_ROOM_NUMBER_WEEKARRAY')
    start_grnwA_timestamp = time.time()
    with open('mainArray.json', 'r') as fileMA:
        mainArray = json.load(fileMA)

    room_number_weekArray = []
    adding_from_day = 1
    for adding_from_day in range(1, 8):
        for adding_from_lesson in range(1, 11):
            # Iterate through the array in reverse order
            found = False  # Flag to track if a valid subarray is found
            for subarray in reversed(mainArray):
                # default adding_from_week = current_week_utz
                if (
                    subarray[3] == 'al'
                    # mark done
                    and subarray[4] == table_user_in
                    and subarray[5] == adding_from_week
                    and subarray[6] == adding_from_day
                    and subarray[7] == adding_from_lesson
                    and subarray[10] == 0
                    # and subarray[13] != 0
                ):
                    if found == False: # if data for this lesson isn't here yet
                        room_number = subarray[13]
                        if subarray[13] == 0:
                            room_number = None
                        room_number_weekArray.append(room_number)
                    if found == True: # if we already have something in the allocated cell
                        pass
                    found = True  # if matching criteria found found = True
            if not found:  # If no valid subarray was found, we append None
                adding_from_week_for_iteration = adding_from_week
                while found == False and adding_from_week_for_iteration > 0:
                    adding_from_week_for_iteration -= 1
                    for subarray in reversed(mainArray):
                    # default adding_from_week = current_week_utz
                        if (
                            subarray[3] == 'al'
                            and subarray[4] == table_user_in
                            and subarray[5] == adding_from_week_for_iteration
                            and subarray[6] == adding_from_day
                            and subarray[7] == adding_from_lesson
                            and subarray[10] == 0
                            and subarray[12] == 1
                            # and subarray[13] != 0
                            and found == False
                        ):
                            room_number = subarray[13]
                            if subarray[13] == 0:
                                room_number = None
                            room_number_weekArray.append(room_number)
                            #log()
                            found = True
                if found == False:
                    room_number_weekArray.append(None)
    print('END OF GET_ROOM_NUMBER_WEEKARRAY EXECUTION IN: ', time.time() - start_grnwA_timestamp)
    return room_number_weekArray


async def get_done_hw_weekArray(table_user_in, adding_from_week, user_id):
    """"""
    global done_hw_weekArray
    print('EXECUTING GET_DONE_HW_WEEKARRAY')
    start_gdhwA_timestamp = time.time()
    with open('mainArray.json', 'r') as fileMA:
        mainArray = json.load(fileMA)

    done_hw_weekArray = []
    adding_from_day = 1
    for adding_from_day in range(1, 8):
        for adding_from_lesson in range(1, 11):
            # Iterate through the array in reverse order
            found = False  # Flag to track if a valid subarray is found
            for subarray in reversed(mainArray):
                # default adding_from_week = current_week_utz
                if (
                    subarray[3] == 'md'
                    # mark done
                    and subarray[4] == table_user_in
                    and subarray[5] == adding_from_week
                    and subarray[6] == adding_from_day
                    and subarray[7] == adding_from_lesson
                    and subarray[10] == 0
                ):
                    if found == False: # if data for this lesson isn't here yet
                        done_hw_weekArray.append(subarray[8])
                    if found == True: # if we already have something in the allocated cell
                        pass
                    found = True  # if matching criteria found found = True
            if not found:  # If no valid subarray was found, we append None
                done_hw_weekArray.append(' ')
    # print('formed done_hw_weekArray: ', done_hw_weekArray)
    print('END OF GET_DONE_HW_WEEKARRAY EXECUTION IN: ', time.time() - start_gdhwA_timestamp)
    return done_hw_weekArray
    

async def getWeekArray_N(table_user_in, adding_from_week):
    """
    Get the array of notes for the entire week.
    
    Returns:
        weekArray_N: A list containing all the notes 1-10 starting from 0 in a week.
    """
    print('EXECUTING GETWEEKARRAY_N')
    start_gwn_timestamp = time.time()
    await getCurrentTemporalInfo()
    # Decode the JSON array to Python object
    with open('mainArray.json', 'r') as fileMA:
        mainArray = json.load(fileMA)

    # print('in func getWeekArray_N: ', mainArray)
    weekArray_N = []
    adding_from_day = 1
    upd_found = True
    """To pass a false state of found down the code to toggle after reassignment"""
    for adding_from_day in range(1, 8):
        for adding_from_lesson in range(1, 11):
            # Iterate through the array in reverse order
            found = False  # Flag to track if a valid subarray is found
            for subarray in mainArray:
                # default adding_from_week = current_week_utz
                if (
                    subarray[3] == 'an'
                    and subarray[4] == table_user_in
                    and subarray[5] == adding_from_week
                    and subarray[6] == adding_from_day
                    and subarray[7] == adding_from_lesson
                    and subarray[10] == 0
                ):
                    if found == False: # if data for this lesson isn't here yet
                        weekArray_N.append(subarray[8])
                    if found == True: # if we already have something in the allocated cell
                        if subarray[8] != '\empty':
                            if weekArray_N[-1] != None:
                                weekArray_N[-1] += "; " + str(subarray[8])
                            else:
                                weekArray_N[-1] = str(subarray[8])
                        else:
                            weekArray_N[-1] = None
                            found = False
                            upd_found = False
                    found = True  # if matching criteria found found = True
                    # if upd_found == False:
                    #     found = False
            if not found:  # If no valid subarray was found, we append None
                weekArray_N.append(None)
    # print('in func getWeekArray_N (end): adding_from_week: ', adding_from_week)
    print('END OF GETWEEKARRAY_N EXECUTION IN: ', time.time() - start_gwn_timestamp)
    return weekArray_N
# async def log(user_id, type, table_user_in, week_number, day_of_week, lesson_number, content, utz, subgroup_level):


async def log(new_data):
    """Creates a log as a subarray in JSON mainArray. Pass new_data as a 1D list in format: [res0 / time_epoch / contributor_id / type / table / week / day / lesson / content / utz / validity (0 is good) / level (register) / exclusiveness of lesson addition (one-time event? 0. Keep until cancelation? 1.) / room_number / res6]
```   
  #res0|   time    |contrib_id| type  |table| w |d |l |cntnt|utz |vl|rg|ex|rn|r6
    [0, 1689546503, 5725753364, 'cs', '1-HAL', 0, 0, 0, 't', utz, 0, 0, 0, 0, 0],
]
#    0      1            2        3      4     5  6  7   8    9   10 11 12 13 14```"""

    print('EXECUTING LOG FUNCTION')
    start_log_timestamp = time.time()
    # First, load the data already in the fileMA
    with open('mainArray.json', 'r') as fileMA:
        mainArray = json.load(fileMA)

    # Now append the new_data to your data
    mainArray.append(new_data)

    # Now write the data back to the fileMA
    with open('mainArray.json', 'w') as fileMA:
        json.dump(mainArray, fileMA)
    print('END OF LOG FUNCTION EXECUTION IN: ', time.time() - start_log_timestamp)


async def getWeekCalendarBoundaries(adding_from_week):
    '''get the adding_from_week calendar boundaries as week_calendar_boundaries'''
    print('EXECUTING GETWEEKCALENDARBOUNDARIES')
    start_gwcb_timestamp = time.time()
    
    await getCurrentTemporalInfo()

    week_start_epoch = adding_from_week * 604800 + 1688947200 + utz
    '''seconds from epoch to start of week (utz)'''
    # Convert the epoch value to a datetime object
    start_date = datetime.fromtimestamp(week_start_epoch)

    # Calculate the end of the week by adding 6 days and 23 hours, 59 minutes, and 59 seconds
    # end_date = start_date + datetime.datetime.timedelta(days=6, hours=23, minutes=59, seconds=59)
    end_date = start_date + timedelta(days=6, hours=23, minutes=59, seconds=59)

    # Format the beginning and end dates in the desired format
    formatted_dates = f"({start_date.strftime('%d.%m')} - {end_date.strftime('%d.%m')})"
    
    # print(formatted_dates)
    week_calendar_boundaries = formatted_dates
    # yield week_calendar_boundaries

    # in function getCurrentTemporalInfo:
    # current_week_utc = (time.time() - 1688947200) // 604800
    # current_day_utc = (time.time() - 1688947200) % 604800 // 86400 + 1
    # current_week_utz = (time.time() + utz - 1688947200) // 604800
    # current_day_utz = (time.time() + utz - 1688947200) % 604800 // 86400 + 1

    print('END OF GETWEEKCALENDARBOUNDARIES EXECUTION IN: ', time.time() - start_gwcb_timestamp)
    return week_calendar_boundaries

def get_weekday_names(language_code):
    weekday_names_by_language = {
        'ru': ['ПОНЕДЕЛЬНИК', 'ВТОРНИК', 'СРЕДА', 'ЧЕТВЕРГ', 'ПЯТНИЦА', 'СУББОТА', 'ВОСКРЕСЕНЬЕ'],
        'es': ['LUNES', 'MARTES', 'MIÉRCOLES', 'JUEVES', 'VIERNES', 'SÁBADO', 'DOMINGO'],
        'fr': ['LUNDI', 'MARDI', 'MERCREDI', 'JEUDI', 'VENDREDI', 'SAMEDI', 'DIMANCHE'],
        'de': ['MONTAG', 'DIENSTAG', 'MITTWOCH', 'DONNERSTAG', 'FREITAG', 'SAMSTAG', 'SONNTAG'],
        'it': ['LUNEDÌ', 'MARTEDÌ', 'MERCOLEDÌ', 'GIOVEDÌ', 'VENERDÌ', 'SABATO', 'DOMENICA'],
        'pt': ['SEGUNDA-FEIRA', 'TERÇA-FEIRA', 'QUARTA-FEIRA', 'QUINTA-FEIRA', 'SEXTA-FEIRA', 'SÁBADO', 'DOMINGO'],
        'nl': ['MAANDAG', 'DINSDAG', 'WOENSDAG', 'DONDERDAG', 'VRIJDAG', 'ZATERDAG', 'ZONDAG'],
        'sv': ['MÅNDAG', 'TISDAG', 'ONSDAG', 'TORSDAG', 'FREDAG', 'LÖRDAG', 'SÖNDAG'],
        'da': ['MANDAG', 'TIRSDAG', 'ONSDAG', 'TORSDAG', 'FREDAG', 'LØRDAG', 'SØNDAG'],
        'no': ['MANDAG', 'TIRSDAG', 'ONSDAG', 'TORSDAG', 'FREDAG', 'LØRDAG', 'SØNDAG'],
        'fi': ['MAANANTAI', 'TIISTAI', 'KESKIVIIKKO', 'TORSTAI', 'PERJANTAI', 'LAUANTAI', 'SUNNUNTAI'],
        'tr': ['PAZARTESI', 'SALI', 'ÇARŞAMBA', 'PERŞEMBE', 'CUMA', 'CUMARTESI', 'PAZAR'],
        'pl': ['PONIEDZIAŁEK', 'WTOREK', 'ŚRODA', 'CZWARTEK', 'PIĄTEK', 'SOBOTA', 'NIEDZIELA'],
        'hu': ['HÉTFŐ', 'KEDD', 'SZERDA', 'CSÜTÖRTÖK', 'PÉNTEK', 'SZOMBAT', 'VASÁRNAP'],
        'zh': ['星期一', '星期二', '星期三', '星期四', '星期五', '星期六', '星期天'],
        'ja': ['月曜日', '火曜日', '水曜日', '木曜日', '金曜日', '土曜日', '日曜日'],
        'eo': ['LUNDO', 'MARDO', 'MERKREDO', 'ĴAŬDO', 'VENDREDO', 'SABATO', 'DIMANĈO'],
        'uk': ['ПОНЕДІЛОК', 'ВІВТОРОК', 'СЕРЕДА', 'ЧЕТВЕР', 'П’ЯТНИЦЯ', 'СУБОТА', 'НЕДІЛЯ'],
        'ko': ['월요일', '화요일', '수요일', '목요일', '금요일', '토요일', '일요일'],
        'ar': ['الاثنين', 'الثلاثاء', 'الأربعاء', 'الخميس', 'الجمعة', 'السبت', 'الأحد'],
        'cs': ['PONDĚLÍ', 'ÚTERÝ', 'STŘEDA', 'ČTVRTEK', 'PÁTEK', 'SOBOTA', 'NEDĚLE'],
        'el': ['ΔΕΥΤΈΡΑ', 'ΤΡΊΤΗ', 'ΤΕΤΆΡΤΗ', 'ΠΈΜΠΤΗ', 'ΠΑΡΑΣΚΕΥΉ', 'ΣΆΒΒΑΤΟ', 'ΚΥΡΙΑΚΉ'],
        'th': ['วันจันทร์', 'วันอังคาร', 'วันพุธ', 'วันพฤหัสบดี', 'วันศุกร์', 'วันเสาร์', 'วันอาทิตย์'],
        'he': ['יום שני', 'יום שלישי', 'יום רביעי', 'יום חמישי', 'יום שישי', 'שבת', 'יום ראשון'],
        'bg': ['ПОНЕДЕЛНИК', 'ВТОРНИК', 'СРЯДА', 'ЧЕТВЪРТЪК', 'ПЕТЪК', 'СЪБОТА', 'НЕДЕЛЯ'],
    }

    return weekday_names_by_language.get(
        language_code.lower(),
        ['MONDAY', 'TUESDAY', 'WEDNESDAY', 'THURSDAY', 'FRIDAY', 'SATURDAY', 'SUNDAY']
    )

async def today_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """List schedule for today"""
    print('EXECUTING TODAY_COMMAND')
    start_tc_timestamp = time.time()
    # print(str(Update))
    # print(Update.message.photo)
    user_id = update.message.chat.id
    username = update.message.chat.username
    await getUserInfo(user_id, username)
    await getCurrentTemporalInfo()
    week_calendar_boundaries = await getWeekCalendarBoundaries(current_week_utz)
    adding_from_week = current_week_utz
    weekArray = await getWeekArray(table_user_in, adding_from_week)
    # print('cvxmxa weekArray: ', weekArray)
    room_number_weekArray = await get_room_number_weekArray(table_user_in, adding_from_week)
    # filename = f"{table_user_in}_temporal_info.json"
    # with open(filename, 'r') as fileTI:
    #     ti = json.load(fileTI)
    ti = getTableTemporalInfoFromMainArray(table_user_in)    
    for i in range(0, 200):
        try:
            if ti[i] == None:
                ti[i] = ' N/A '
        except TypeError:
            if ti == None:
                ti = []
                for i in range(0, 200):
                    ti.append(' N/A ')
            ti[i] = ' N/A '
    if current_day_utz == 1:
        wd_n = 0
    elif current_day_utz == 2:
        wd_n = 1
    elif current_day_utz == 3:
        wd_n = 2
    elif current_day_utz == 4:
        wd_n = 3
    elif current_day_utz == 5:
        wd_n = 4
    elif current_day_utz == 6:
        wd_n = 5
    elif current_day_utz == 7:
        wd_n = 6

    ti_nums = [
        [ti[20], ti[21], ti[22], ti[23], ti[24], ti[25], ti[26], ti[27], ti[28], ti[29], ti[30], ti[31], ti[32], ti[33], ti[34], ti[35], ti[36], ti[37], ti[38], ti[39]],  # monday
        [ti[40], ti[41], ti[42], ti[43], ti[44], ti[45], ti[46], ti[47], ti[48], ti[49], ti[50], ti[51], ti[52], ti[53], ti[54], ti[55], ti[56], ti[57], ti[58], ti[59]],
        [ti[60], ti[61], ti[62], ti[63], ti[64], ti[65], ti[66], ti[67], ti[68], ti[69], ti[70], ti[71], ti[72], ti[73], ti[74], ti[75], ti[76], ti[77], ti[78], ti[79]],
        [ti[80], ti[81], ti[82], ti[83], ti[84], ti[85], ti[86], ti[87], ti[88], ti[89], ti[90], ti[91], ti[92], ti[93], ti[94], ti[95], ti[96], ti[97], ti[98], ti[99]],
        [ti[100], ti[101], ti[102], ti[103], ti[104], ti[105], ti[106], ti[107], ti[108], ti[109], ti[110], ti[111], ti[112], ti[113], ti[114], ti[115], ti[116], ti[117], ti[118], ti[119]],
        [ti[120], ti[121], ti[122], ti[123], ti[124], ti[125], ti[126], ti[127], ti[128], ti[129], ti[130], ti[131], ti[132], ti[133], ti[134], ti[135], ti[136], ti[137], ti[138], ti[139]],
        [ti[140], ti[141], ti[142], ti[143], ti[144], ti[145], ti[146], ti[147], ti[148], ti[149], ti[150], ti[151], ti[152], ti[153], ti[154], ti[155], ti[156], ti[157], ti[158], ti[159]],  # sunday
    ]

    # print('in td wA: ', weekArray)
    wA_nums = [
        [weekArray[0], weekArray[1], weekArray[2], weekArray[3], weekArray[4], weekArray[5], weekArray[6], weekArray[7], weekArray[8], weekArray[9]],
        [weekArray[10], weekArray[11], weekArray[12], weekArray[13], weekArray[14], weekArray[15], weekArray[16], weekArray[17], weekArray[18], weekArray[19]],
        [weekArray[20], weekArray[21], weekArray[22], weekArray[23], weekArray[24], weekArray[25], weekArray[26], weekArray[27], weekArray[28], weekArray[29]],
        [weekArray[30], weekArray[31], weekArray[32], weekArray[33], weekArray[34], weekArray[35], weekArray[36], weekArray[37], weekArray[38], weekArray[39]],
        [weekArray[40], weekArray[41], weekArray[42], weekArray[43], weekArray[44], weekArray[45], weekArray[46], weekArray[47], weekArray[48], weekArray[49]],
        [weekArray[50], weekArray[51], weekArray[52], weekArray[53], weekArray[54], weekArray[55], weekArray[56], weekArray[57], weekArray[58], weekArray[59]],
        [weekArray[60], weekArray[61], weekArray[62], weekArray[63], weekArray[64], weekArray[65], weekArray[66], weekArray[67], weekArray[68], weekArray[69]],  # sunday
    ]

    # print(wA_nums)


    # s_table = [
    # ["WEEK"],
    # ["MONDAY","t","q"]
    # ]


    # print(tabulate(s_table, headers="firstrow", tablefmt="fancy_grid"))

    # colspan = {(0, 0): 2}
    # rowspan = {(0, 1): 2}

    # s_table = tabulate(s_table, colspan=colspan, rowspan=rowspan, tablefmt="simple_grid")


    # s_table = '<pre>' + s_table + '</pre>'


    # table = [
    # ["", "WEEK", "d"],
    # ["", "MONDAY", "t"]
    # ]

    # headers = ['Title']

    # formatted_table = tabulate(table, headers=headers, tablefmt="simple_grid")
    # print(formatted_table)


    wd_names = get_weekday_names(update.message.from_user.language_code.lower())


    # if update.message.from_user.language_code == 'ru':
    #     wd_names = ['ПОНЕДЕЛЬНИК', 'ВТОРНИК', 'СРЕДА', 'ЧЕТВЕРГ', 'ПЯТНИЦА', 'СУББОТА', 'ВОСКРЕСЕНЬЕ']
    # else:
    #     wd_names = ['MONDAY', 'TUESDAY', 'WEDNESDAY', 'THURSDAY', 'FRIDAY', 'SATURDAY', 'SUNDAY']



    for i, element in enumerate(room_number_weekArray):
        if element is None:
            room_number_weekArray[i] = ' '

    for i, element in enumerate(room_number_weekArray):
        if len(str(element)) != 5:
            room_number_weekArray[i] = ' '*(5-len(str(element))) + str(element)
    
    # print(int(wd_n*10+1))
    # print(wd_n)
    # print(room_number_weekArray)

    s_table = (f"""<pre>┌──────────────────────────┐
│WEEK {str(int(adding_from_week))} {str(week_calendar_boundaries)}{' '*(20-(len(str(int(adding_from_week)))+len(str(week_calendar_boundaries))))}│
├──────────────────────────┤
│{wd_names[wd_n] + ' '*(26-len(wd_names[wd_n]))}│
├─┬─────┬─────┬─────┬──────┤
│1│{ti_nums[wd_n][0]}│{ti_nums[wd_n][1]}│{room_number_weekArray[wd_n*10+0]}│{str(wA_nums[wd_n][0]) + ' '*(6-len(str(wA_nums[wd_n][0]))) if wA_nums[wd_n][0] != None else '      '}│
├─┼─────┼─────┼─────┼──────┤
│2│{ti_nums[wd_n][2]}│{ti_nums[wd_n][3]}│{room_number_weekArray[wd_n*10+1]}│{str(wA_nums[wd_n][1]) + ' '*(6-len(str(wA_nums[wd_n][1]))) if wA_nums[wd_n][1] != None else '      '}│
├─┼─────┼─────┼─────┼──────┤
│3│{ti_nums[wd_n][4]}│{ti_nums[wd_n][5]}│{room_number_weekArray[wd_n*10+2]}│{str(wA_nums[wd_n][2]) + ' '*(6-len(str(wA_nums[wd_n][2]))) if wA_nums[wd_n][2] != None else '      '}│
├─┼─────┼─────┼─────┼──────┤
│4│{ti_nums[wd_n][6]}│{ti_nums[wd_n][7]}│{room_number_weekArray[wd_n*10+3]}│{str(wA_nums[wd_n][3]) + ' '*(6-len(str(wA_nums[wd_n][3]))) if wA_nums[wd_n][3] != None else '      '}│
├─┼─────┼─────┼─────┼──────┤
│5│{ti_nums[wd_n][8]}│{ti_nums[wd_n][9]}│{room_number_weekArray[wd_n*10+4]}│{str(wA_nums[wd_n][4]) + ' '*(6-len(str(wA_nums[wd_n][4]))) if wA_nums[wd_n][4] != None else '      '}│
├─┼─────┼─────┼─────┼──────┤
│6│{ti_nums[wd_n][10]}│{ti_nums[wd_n][11]}│{room_number_weekArray[wd_n*10+5]}│{str(wA_nums[wd_n][5]) + ' '*(6-len(str(wA_nums[wd_n][5]))) if wA_nums[wd_n][5] != None else '      '}│
├─┴─────┴─────┴─────┴──────┤
│TABLE ID: {table_user_in + ' '*(16-len(table_user_in))}│
└──────────────────────────┘</pre>""")
    await update.message.reply_text(s_table, parse_mode='HTML')
    print('END OF TODAY_COMMAND EXECUTION IN', time.time() - start_tc_timestamp)
    return weekArray

#     s_table = (f"""<pre>{wd_n, current_day_utz, current_day_utc}
# ┌──────────────────────────┐
# │WEEK {str(int(adding_from_week))} {str(week_calendar_boundaries)}{' '*(20-(len(str(int(adding_from_week)))+len(str(week_calendar_boundaries))))}│
# ├──────────────────────────┤
# │{wd_names[wd_n] + ' '*(26-len(wd_names[wd_n]))}│
# ├─┬─────┬─────┬────────────┤
# │1│{ti_nums[wd_n][0]}│{ti_nums[wd_n][1]}│{str(wA_nums[wd_n][0]) + ' '*(12-len(str(wA_nums[wd_n][0]))) if wA_nums[wd_n][0] != None else '            '}│
# ├─┼─────┼─────┼────────────┤
# │2│{ti_nums[wd_n][2]}│{ti_nums[wd_n][3]}│{str(wA_nums[wd_n][1]) + ' '*(12-len(str(wA_nums[wd_n][1]))) if wA_nums[wd_n][1] != None else '            '}│
# ├─┼─────┼─────┼────────────┤
# │3│{ti_nums[wd_n][4]}│{ti_nums[wd_n][5]}│{str(wA_nums[wd_n][2]) + ' '*(12-len(str(wA_nums[wd_n][2]))) if wA_nums[wd_n][2] != None else '            '}│
# ├─┼─────┼─────┼────────────┤
# │4│{ti_nums[wd_n][6]}│{ti_nums[wd_n][7]}│{str(wA_nums[wd_n][3]) + ' '*(12-len(str(wA_nums[wd_n][3]))) if wA_nums[wd_n][3] != None else '            '}│
# ├─┼─────┼─────┼────────────┤
# │5│{ti_nums[wd_n][8]}│{ti_nums[wd_n][9]}│{str(wA_nums[wd_n][4]) + ' '*(12-len(str(wA_nums[wd_n][4]))) if wA_nums[wd_n][4] != None else '            '}│
# ├─┼─────┼─────┼────────────┤
# │6│{ti_nums[wd_n][10]}│{ti_nums[wd_n][11]}│{str(wA_nums[wd_n][5]) + ' '*(12-len(str(wA_nums[wd_n][5]))) if wA_nums[wd_n][5] != None else '            '}│
# └─┴─────┴─────┴────────────┘
# </pre>""")



async def formSemigraphicTable(adding_from_week, user_id, table_type, weekArray, weekArray_HW = [], weekArray_N = [], done_hw_weekArray = [], roomNpos = 'no', update = None):
    """Creates a semigraphic table. Pass table_type as 'lessons_only' or 'hw' or 'notes'"""
    print('EXECUTING FORMSEMIGRAPHICTABLE')
    start_fst_timestamp = time.time()
    global s_table
    await getUserInfo(user_id)
    week_calendar_boundaries = await getWeekCalendarBoundaries(adding_from_week)
    room_number_weekArray = await get_room_number_weekArray(table_user_in, adding_from_week)
    # filename = f"{table_user_in}_temporal_info.json"
    try:
        # with open(filename, 'r') as fileTI:
        #     ti = json.load(fileTI)
        ti = getTableTemporalInfoFromMainArray(table_user_in)
    except:
        print('Something went wrong. Try setting time with /set_temporal first.')
        await update.message.reply_text('Something went wrong. Try setting /set_temporal first.')

    for i in range(0, 200):
        try:
            if ti[i] == None:
                ti[i] = ' N/A '
        except TypeError:
            if ti == None:
                ti = []
                for i in range(0, 200):
                    ti.append(' N/A ')
            ti[i] = ' N/A '

    if ti[20] == None:
        for i in range(20, 150):
            ti[i] = " N/A "

    done_hw_weekArray = await get_done_hw_weekArray(table_user_in, adding_from_week, user_id)

    if update.message.from_user.language_code == 'ru':
        wd_names = ['ПОНЕДЕЛЬНИК', 'ВТОРНИК', 'СРЕДА', 'ЧЕТВЕРГ', 'ПЯТНИЦА', 'СУББОТА', 'ВОСКРЕСЕНЬЕ']
    else:
        wd_names = ['MONDAY', 'TUESDAY', 'WEDNESDAY', 'THURSDAY', 'FRIDAY', 'SATURDAY', 'SUNDAY']

    if table_type == 'lessons_only':
        # without room numbers table
        s_table = f"""<pre>
┌──────────────────────────┐
│WEEK {str(int(adding_from_week))} {str(week_calendar_boundaries)}{' '*(20-(len(str(int(adding_from_week)))+len(str(week_calendar_boundaries))))}│
├──────────────────────────┤
│{wd_names[0] + ' '*(26-len(wd_names[0]))}│
├─┬─────┬─────┬────────────┤
│1│{ti[20]}│{ti[21]}│{str(weekArray[0]) + ' '*(12-len(str(weekArray[0]))) if weekArray[0] != None else '            '}│
├─┼─────┼─────┼────────────┤
│2│{ti[22]}│{ti[23]}│{str(weekArray[1]) + ' '*(12-len(str(weekArray[1]))) if weekArray[1] != None else '            '}│
├─┼─────┼─────┼────────────┤
│3│{ti[24]}│{ti[25]}│{str(weekArray[2]) + ' '*(12-len(str(weekArray[2]))) if weekArray[2] != None else '            '}│
├─┼─────┼─────┼────────────┤
│4│{ti[26]}│{ti[27]}│{str(weekArray[3]) + ' '*(12-len(str(weekArray[3]))) if weekArray[3] != None else '            '}│
├─┼─────┼─────┼────────────┤
│5│{ti[28]}│{ti[29]}│{str(weekArray[4]) + ' '*(12-len(str(weekArray[4]))) if weekArray[4] != None else '            '}│
├─┼─────┼─────┼────────────┤
│6│{ti[30]}│{ti[31]}│{str(weekArray[5]) + ' '*(12-len(str(weekArray[5]))) if weekArray[5] != None else '            '}│
├─┴─────┴─────┴────────────┤
│{wd_names[1] + ' '*(26-len(wd_names[1]))}│
├─┬─────┬─────┬────────────┤
│1│{ti[40]}│{ti[41]}│{str(weekArray[10]) + ' '*(12-len(str(weekArray[10]))) if weekArray[10] != None else '            '}│
├─┼─────┼─────┼────────────┤
│2│{ti[42]}│{ti[43]}│{str(weekArray[11]) + ' '*(12-len(str(weekArray[11]))) if weekArray[11] != None else '            '}│
├─┼─────┼─────┼────────────┤
│3│{ti[44]}│{ti[45]}│{str(weekArray[12]) + ' '*(12-len(str(weekArray[12]))) if weekArray[12] != None else '            '}│
├─┼─────┼─────┼────────────┤
│4│{ti[46]}│{ti[47]}│{str(weekArray[13]) + ' '*(12-len(str(weekArray[13]))) if weekArray[13] != None else '            '}│
├─┼─────┼─────┼────────────┤
│5│{ti[48]}│{ti[49]}│{str(weekArray[14]) + ' '*(12-len(str(weekArray[14]))) if weekArray[14] != None else '            '}│
├─┼─────┼─────┼────────────┤
│6│{ti[50]}│{ti[51]}│{str(weekArray[15]) + ' '*(12-len(str(weekArray[15]))) if weekArray[15] != None else '            '}│
├─┴─────┴─────┴────────────┤
│{wd_names[2] + ' '*(26-len(wd_names[2]))}│
├─┬─────┬─────┬────────────┤
│1│{ti[60]}│{ti[61]}│{str(weekArray[20]) + ' '*(12-len(str(weekArray[20]))) if weekArray[20] != None else '            '}│
├─┼─────┼─────┼────────────┤
│2│{ti[62]}│{ti[63]}│{str(weekArray[21]) + ' '*(12-len(str(weekArray[21]))) if weekArray[21] != None else '            '}│
├─┼─────┼─────┼────────────┤
│3│{ti[64]}│{ti[65]}│{str(weekArray[22]) + ' '*(12-len(str(weekArray[22]))) if weekArray[22] != None else '            '}│
├─┼─────┼─────┼────────────┤
│4│{ti[66]}│{ti[67]}│{str(weekArray[23]) + ' '*(12-len(str(weekArray[23]))) if weekArray[23] != None else '            '}│
├─┼─────┼─────┼────────────┤
│5│{ti[68]}│{ti[69]}│{str(weekArray[24]) + ' '*(12-len(str(weekArray[24]))) if weekArray[24] != None else '            '}│
├─┼─────┼─────┼────────────┤
│6│{ti[70]}│{ti[71]}│{str(weekArray[25]) + ' '*(12-len(str(weekArray[25]))) if weekArray[25] != None else '            '}│
├─┴─────┴─────┴────────────┤
│{wd_names[3] + ' '*(26-len(wd_names[3]))}│
├─┬─────┬─────┬────────────┤
│1│{ti[80]}│{ti[81]}│{str(weekArray[30]) + ' '*(12-len(str(weekArray[30]))) if weekArray[30] != None else '            '}│
├─┼─────┼─────┼────────────┤
│2│{ti[82]}│{ti[83]}│{str(weekArray[31]) + ' '*(12-len(str(weekArray[31]))) if weekArray[31] != None else '            '}│
├─┼─────┼─────┼────────────┤
│3│{ti[84]}│{ti[85]}│{str(weekArray[32]) + ' '*(12-len(str(weekArray[32]))) if weekArray[32] != None else '            '}│
├─┼─────┼─────┼────────────┤
│4│{ti[86]}│{ti[87]}│{str(weekArray[33]) + ' '*(12-len(str(weekArray[33]))) if weekArray[33] != None else '            '}│
├─┼─────┼─────┼────────────┤
│5│{ti[88]}│{ti[89]}│{str(weekArray[34]) + ' '*(12-len(str(weekArray[34]))) if weekArray[34] != None else '            '}│
├─┼─────┼─────┼────────────┤
│6│{ti[90]}│{ti[91]}│{str(weekArray[35]) + ' '*(12-len(str(weekArray[35]))) if weekArray[35] != None else '            '}│
├─┴─────┴─────┴────────────┤
│{wd_names[4] + ' '*(26-len(wd_names[4]))}│
├─┬─────┬─────┬────────────┤
│1│{ti[100]}│{ti[101]}│{str(weekArray[40]) + ' '*(12-len(str(weekArray[40]))) if weekArray[40] != None else '            '}│
├─┼─────┼─────┼────────────┤
│2│{ti[102]}│{ti[103]}│{str(weekArray[41]) + ' '*(12-len(str(weekArray[41]))) if weekArray[41] != None else '            '}│
├─┼─────┼─────┼────────────┤
│3│{ti[104]}│{ti[105]}│{str(weekArray[42]) + ' '*(12-len(str(weekArray[42]))) if weekArray[42] != None else '            '}│
├─┼─────┼─────┼────────────┤
│4│{ti[106]}│{ti[107]}│{str(weekArray[43]) + ' '*(12-len(str(weekArray[43]))) if weekArray[43] != None else '            '}│
├─┼─────┼─────┼────────────┤
│5│{ti[108]}│{ti[109]}│{str(weekArray[44]) + ' '*(12-len(str(weekArray[44]))) if weekArray[44] != None else '            '}│
├─┼─────┼─────┼────────────┤
│6│{ti[110]}│{ti[111]}│{str(weekArray[45]) + ' '*(12-len(str(weekArray[45]))) if weekArray[45] != None else '            '}│
├─┴─────┴─────┴────────────┤
│{wd_names[5] + ' '*(26-len(wd_names[5]))}│
├─┬─────┬─────┬────────────┤
│1│{ti[120]}│{ti[121]}│{str(weekArray[50]) + ' '*(12-len(str(weekArray[50]))) if weekArray[50] != None else '            '}│
├─┼─────┼─────┼────────────┤
│2│{ti[122]}│{ti[123]}│{str(weekArray[51]) + ' '*(12-len(str(weekArray[51]))) if weekArray[51] != None else '            '}│
├─┼─────┼─────┼────────────┤
│3│{ti[124]}│{ti[125]}│{str(weekArray[52]) + ' '*(12-len(str(weekArray[52]))) if weekArray[52] != None else '            '}│
├─┼─────┼─────┼────────────┤
│4│{ti[126]}│{ti[127]}│{str(weekArray[53]) + ' '*(12-len(str(weekArray[53]))) if weekArray[53] != None else '            '}│
├─┼─────┼─────┼────────────┤
│5│{ti[128]}│{ti[129]}│{str(weekArray[54]) + ' '*(12-len(str(weekArray[54]))) if weekArray[54] != None else '            '}│
├─┼─────┼─────┼────────────┤
│6│{ti[130]}│{ti[131]}│{str(weekArray[55]) + ' '*(12-len(str(weekArray[55]))) if weekArray[55] != None else '            '}│
├─┴─────┴─────┴────────────┤
│TABLE ID: {table_user_in + ' '*(16-len(table_user_in))}│
└──────────────────────────┘

</pre>
"""
# ├─┴─────┴─────┴────────────┤
# │SUNDAY                    │26+2
# ├─┬─────┬─────┬────────────┤
# │1│{ti[0]}│{ti[1]}│{str(weekArray[60]) + ' '*(12-len(str(weekArray[60]))) if weekArray[60] != None else '            '}│
# ├─┼─────┼─────┼────────────┤
# │2│{ti[2]}│{ti[3]}│{str(weekArray[61]) + ' '*(12-len(str(weekArray[61]))) if weekArray[61] != None else '            '}│
# ├─┼─────┼─────┼────────────┤
# │3│{ti[4]}│{ti[5]}│{str(weekArray[62]) + ' '*(12-len(str(weekArray[62]))) if weekArray[62] != None else '            '}│
# ├─┼─────┼─────┼────────────┤
# │4│{ti[6]}│{ti[7]}│{str(weekArray[63]) + ' '*(12-len(str(weekArray[63]))) if weekArray[63] != None else '            '}│
# ├─┼─────┼─────┼────────────┤
# │5│{ti[8]}│{ti[9]}│{str(weekArray[64]) + ' '*(12-len(str(weekArray[64]))) if weekArray[64] != None else '            '}│
# ├─┼─────┼─────┼────────────┤
# │6│{ti[10]}│{ti[11]}│{str(weekArray[65]) + ' '*(12-len(str(weekArray[65]))) if weekArray[65] != None else '            '}│
# └─┴─────┴─────┴────────────┘

#     elif table_type == 'generative_lessons_only':
#     # an experimental attempt to generate the table with loops without repetative code
#         wd = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
#         table_text = f"""┌──────────────────────────┐
# │WEEK {str(int(adding_from_week))} {str(week_calendar_boundaries)}{' '*(20-(len(str(int(adding_from_week)))+len(str(week_calendar_boundaries))))}│
# ├──────────────────────────┤
# """
#         for day in range (0, 7):
#             table_text += f"""│wd[day]+(' '*(26-len(str(wd[day]))))│
#     """
#             for lesson in range (0, 6):
#                 table_text += f"""│{str(weekArray[7]) + ' '*(12-len(str(weekArray[7]))) if weekArray[7] != None else '            '}│
#                 """

        
        room_number_weekArray = [None, 123, None, 456, None, 789]

        room_number_weekArray = ['    ' if val is None else val for val in room_number_weekArray]




#         s_table = f"""<pre>
# ┌──────────────────────────┐
# │WEEK {str(int(adding_from_week))} {str(week_calendar_boundaries)}{' '*(20-(len(str(int(adding_from_week)))+len(str(week_calendar_boundaries))))}│
# ├──────────────────────────┤
# │MONDAY                    │
# ├─┬─────┬─────┬────────────┤
# │1│{ti[20]}│{ti[21]}│{str(weekArray[0]) + ' '*(7-len(str(weekArray[0]))) if weekArray[0] != None else '            '}┊{str(room_number_weekArray[0])}│
# ├─┼─────┼─────┼────────────┤
# │2│{ti[22]}│{ti[23]}│{str(weekArray[1]) + ' '*(12-len(str(weekArray[1]))) if weekArray[1] != None else '            '}│
# ├─┼─────┼─────┼────────────┤
# │3│{ti[24]}│{ti[25]}│{str(weekArray[2]) + ' '*(12-len(str(weekArray[2]))) if weekArray[2] != None else '            '}│
# ├─┼─────┼─────┼────────────┤
# │4│{ti[26]}│{ti[27]}│{str(weekArray[3]) + ' '*(12-len(str(weekArray[3]))) if weekArray[3] != None else '            '}│
# ├─┼─────┼─────┼────────────┤
# │5│{ti[28]}│{ti[29]}│{str(weekArray[4]) + ' '*(12-len(str(weekArray[4]))) if weekArray[4] != None else '            '}│
# ├─┼─────┼─────┼────────────┤
# │6│{ti[30]}│{ti[31]}│{str(weekArray[5]) + ' '*(12-len(str(weekArray[5]))) if weekArray[5] != None else '            '}│
# ├─┴─────┴─────┴────────────┤
# │TUESDAY                   │
# ├─┬─────┬─────┬────────────┤
# │1│{ti[40]}│{ti[41]}│{str(weekArray[10]) + ' '*(12-len(str(weekArray[10]))) if weekArray[10] != None else '            '}│
# ├─┼─────┼─────┼────────────┤
# │2│{ti[42]}│{ti[43]}│{str(weekArray[11]) + ' '*(12-len(str(weekArray[11]))) if weekArray[11] != None else '            '}│
# ├─┼─────┼─────┼────────────┤
# │3│{ti[44]}│{ti[45]}│{str(weekArray[12]) + ' '*(12-len(str(weekArray[12]))) if weekArray[12] != None else '            '}│
# ├─┼─────┼─────┼────────────┤
# │4│{ti[46]}│{ti[47]}│{str(weekArray[13]) + ' '*(12-len(str(weekArray[13]))) if weekArray[13] != None else '            '}│
# ├─┼─────┼─────┼────────────┤
# │5│{ti[48]}│{ti[49]}│{str(weekArray[14]) + ' '*(12-len(str(weekArray[14]))) if weekArray[14] != None else '            '}│
# ├─┼─────┼─────┼────────────┤
# │6│{ti[50]}│{ti[51]}│{str(weekArray[15]) + ' '*(12-len(str(weekArray[15]))) if weekArray[15] != None else '            '}│
# ├─┴─────┴─────┴────────────┤
# │WEDNESDAY                 │
# ├─┬─────┬─────┬────────────┤
# │1│{ti[60]}│{ti[61]}│{str(weekArray[20]) + ' '*(12-len(str(weekArray[20]))) if weekArray[20] != None else '            '}│
# ├─┼─────┼─────┼────────────┤
# │2│{ti[62]}│{ti[63]}│{str(weekArray[21]) + ' '*(12-len(str(weekArray[21]))) if weekArray[21] != None else '            '}│
# ├─┼─────┼─────┼────────────┤
# │3│{ti[64]}│{ti[65]}│{str(weekArray[22]) + ' '*(12-len(str(weekArray[22]))) if weekArray[22] != None else '            '}│
# ├─┼─────┼─────┼────────────┤
# │4│{ti[66]}│{ti[67]}│{str(weekArray[23]) + ' '*(12-len(str(weekArray[23]))) if weekArray[23] != None else '            '}│
# ├─┼─────┼─────┼────────────┤
# │5│{ti[68]}│{ti[69]}│{str(weekArray[24]) + ' '*(12-len(str(weekArray[24]))) if weekArray[24] != None else '            '}│
# ├─┼─────┼─────┼────────────┤
# │6│{ti[70]}│{ti[71]}│{str(weekArray[25]) + ' '*(12-len(str(weekArray[25]))) if weekArray[25] != None else '            '}│
# ├─┴─────┴─────┴────────────┤
# │THURSDAY                  │
# ├─┬─────┬─────┬────────────┤
# │1│{ti[80]}│{ti[81]}│{str(weekArray[30]) + ' '*(12-len(str(weekArray[30]))) if weekArray[30] != None else '            '}│
# ├─┼─────┼─────┼────────────┤
# │2│{ti[82]}│{ti[83]}│{str(weekArray[31]) + ' '*(12-len(str(weekArray[31]))) if weekArray[31] != None else '            '}│
# ├─┼─────┼─────┼────────────┤
# │3│{ti[84]}│{ti[85]}│{str(weekArray[32]) + ' '*(12-len(str(weekArray[32]))) if weekArray[32] != None else '            '}│
# ├─┼─────┼─────┼────────────┤
# │4│{ti[86]}│{ti[87]}│{str(weekArray[33]) + ' '*(12-len(str(weekArray[33]))) if weekArray[33] != None else '            '}│
# ├─┼─────┼─────┼────────────┤
# │5│{ti[88]}│{ti[89]}│{str(weekArray[34]) + ' '*(12-len(str(weekArray[34]))) if weekArray[34] != None else '            '}│
# ├─┼─────┼─────┼────────────┤
# │6│{ti[90]}│{ti[91]}│{str(weekArray[35]) + ' '*(12-len(str(weekArray[35]))) if weekArray[35] != None else '            '}│
# ├─┴─────┴─────┴────────────┤
# │FRIDAY                    │
# ├─┬─────┬─────┬────────────┤
# │1│{ti[100]}│{ti[101]}│{str(weekArray[40]) + ' '*(12-len(str(weekArray[40]))) if weekArray[40] != None else '            '}│
# ├─┼─────┼─────┼────────────┤
# │2│{ti[102]}│{ti[103]}│{str(weekArray[41]) + ' '*(12-len(str(weekArray[41]))) if weekArray[41] != None else '            '}│
# ├─┼─────┼─────┼────────────┤
# │3│{ti[104]}│{ti[105]}│{str(weekArray[42]) + ' '*(12-len(str(weekArray[42]))) if weekArray[42] != None else '            '}│
# ├─┼─────┼─────┼────────────┤
# │4│{ti[106]}│{ti[107]}│{str(weekArray[43]) + ' '*(12-len(str(weekArray[43]))) if weekArray[43] != None else '            '}│
# ├─┼─────┼─────┼────────────┤
# │5│{ti[108]}│{ti[109]}│{str(weekArray[44]) + ' '*(12-len(str(weekArray[44]))) if weekArray[44] != None else '            '}│
# ├─┼─────┼─────┼────────────┤
# │6│{ti[110]}│{ti[111]}│{str(weekArray[45]) + ' '*(12-len(str(weekArray[45]))) if weekArray[45] != None else '            '}│
# ├─┴─────┴─────┴────────────┤
# │SATURDAY                  │
# ├─┬─────┬─────┬────────────┤
# │1│{ti[120]}│{ti[121]}│{str(weekArray[50]) + ' '*(12-len(str(weekArray[50]))) if weekArray[50] != None else '            '}│
# ├─┼─────┼─────┼────────────┤
# │2│{ti[122]}│{ti[123]}│{str(weekArray[51]) + ' '*(12-len(str(weekArray[51]))) if weekArray[51] != None else '            '}│
# ├─┼─────┼─────┼────────────┤
# │3│{ti[124]}│{ti[125]}│{str(weekArray[52]) + ' '*(12-len(str(weekArray[52]))) if weekArray[52] != None else '            '}│
# ├─┼─────┼─────┼────────────┤
# │4│{ti[126]}│{ti[127]}│{str(weekArray[53]) + ' '*(12-len(str(weekArray[53]))) if weekArray[53] != None else '            '}│
# ├─┼─────┼─────┼────────────┤
# │5│{ti[128]}│{ti[129]}│{str(weekArray[54]) + ' '*(12-len(str(weekArray[54]))) if weekArray[54] != None else '            '}│
# ├─┼─────┼─────┼────────────┤
# │6│{ti[130]}│{ti[131]}│{str(weekArray[55]) + ' '*(12-len(str(weekArray[55]))) if weekArray[55] != None else '            '}│
# ├─┴─────┴─────┴────────────┤
# │TABLE ID: {table_user_in + ' '*(16-len(table_user_in))}│
# └──────────────────────────┘

# </pre>
# """




    elif table_type == 'hw':
        # print('weekArray_HW at start: ', weekArray_HW)
        lined_hw_array = []
        
        for i in range(len(weekArray_HW)):
            if weekArray_HW[i] is not None:
                weekArray_HW[i] = weekArray_HW[i].replace("\n", " ")

        for string in weekArray_HW:
            if string is None:
                lined_hw_array.append(['                        ', '                        ', '                          ', '                          ', '                          ', '                          ', '                          ', '                          ', '                          ', '                          ', '                          ', '                          ', '                          ', '                          ', '                          ', '                          '])
                # Adds 16 blank placeholders
                continue
            element_1 = string[:24]
            element_1 = element_1 + ' ' * (24 - len(element_1))
            element_2 = string[24:48]
            element_2 = element_2 + ' ' * (24 - len(element_2))
            element_3 = string[48:74]
            element_3 = element_3 + ' ' * (26 - len(element_3))
            element_4 = string[74:100]
            element_4 = element_4 + ' ' * (26 - len(element_4))
            element_5 = string[100:126]
            element_5 = element_5 + ' ' * (26 - len(element_5))
            element_6 = string[126:152]
            element_6 = element_6 + ' ' * (26 - len(element_6))
            element_7 = string[152:178]
            element_7 = element_7 + ' ' * (26 - len(element_7))
            element_8 = string[178:]
            element_8 = element_8 + ' ' * (26 - len(element_8))
            if element_1 != '                        ' and element_2 == '                        ':
                element_2 = '                        '
                # adds a non-space character to make the table display the line
            temp_subarray = [element_1, element_2, element_3, element_4, element_5, element_6, element_7, element_8]
            lined_hw_array.append(temp_subarray)
        # print("weekArray_HW: ", weekArray_HW)
        # print("lined_hw_array: ", lined_hw_array)
        eol = '\n'
        # the following one is reassigned later
        s_table = f"""<pre>
┌──────────────────────────┐
│WEEK {str(int(adding_from_week))} {str(week_calendar_boundaries)}{' '*(20-(len(str(int(adding_from_week)))+len(str(week_calendar_boundaries))))}│
├──────────────────────────┤
│MONDAY                    │
├─┬─────┬─────┬────────────┤
│1│{ti[20]}│{ti[21]}│{str(weekArray[0]) + ' '*(12-len(str(weekArray[0]))) if weekArray[0] != None else '            '}│
├─┴─────┴─────┴──────────┬─┤
│{lined_hw_array[0][0]}│V│
│{lined_hw_array[0][1]}└─┤
│{lined_hw_array[0][2]}│{eol + '│' + lined_hw_array[0][3] + '│' if lined_hw_array[0][3] != '                          ' else ''}
├─┬─────┬─────┬────────────┤
│2│{ti[22]}│{ti[23]}│{str(weekArray[1]) + ' '*(12-len(str(weekArray[1]))) if weekArray[1] != None else '            '}│
├─┴─────┴─────┴──────────┬─┤
│{lined_hw_array[1][0]}│V│
│{lined_hw_array[1][1]}└─┤
│{lined_hw_array[1][2]}│{eol + '│' + lined_hw_array[1][3] + '│' if lined_hw_array[1][3] != '                          ' else ''}
├─┬─────┬─────┬────────────┤
│3│{ti[24]}│{ti[25]}│{str(weekArray[2]) + ' '*(12-len(str(weekArray[2]))) if weekArray[2] != None else '            '}│
├─┴─────┴─────┴──────────┬─┤
│{lined_hw_array[2][0]}│V│
│{lined_hw_array[2][1]}└─┤
│{lined_hw_array[2][2]}│{eol + '│' + lined_hw_array[2][3] + '│' if lined_hw_array[2][3] != '                          ' else ''}
├─┬─────┬─────┬────────────┤
│4│{ti[26]}│{ti[27]}│{str(weekArray[3]) + ' '*(12-len(str(weekArray[3]))) if weekArray[3] != None else '            '}│
├─┴─────┴─────┴──────────┬─┤
│{lined_hw_array[3][0]}│V│
│{lined_hw_array[3][1]}└─┤
│{lined_hw_array[3][2]}│{eol + '│' + lined_hw_array[3][3] + '│' if lined_hw_array[3][3] != '                          ' else ''}
├─┬─────┬─────┬────────────┤
│5│{ti[28]}│{ti[29]}│{str(weekArray[4]) + ' '*(12-len(str(weekArray[4]))) if weekArray[4] != None else '            '}│
├─┴─────┴─────┴──────────┬─┤
│{lined_hw_array[4][0]}│V│
│{lined_hw_array[4][1]}└─┤
│{lined_hw_array[4][2]}│{eol + '│' + lined_hw_array[4][3] + '│' if lined_hw_array[4][3] != '                          ' else ''}
├─┬─────┬─────┬────────────┤
│6│{ti[30]}│{ti[31]}│{str(weekArray[5]) + ' '*(12-len(str(weekArray[5]))) if weekArray[5] != None else '            '}│
├─┴─────┴─────┴──────────┬─┤
│{lined_hw_array[5][0]}│V│
│{lined_hw_array[5][1]}└─┤
│{lined_hw_array[5][2]}│{eol + '│' + lined_hw_array[5][3] + '│' if lined_hw_array[5][3] != '                          ' else ''}
├──────────────────────────┤
│TUESDAY                   │
├─┬─────┬─────┬────────────┤
│1│{ti[40]}│{ti[41]}│{str(weekArray[10]) + ' '*(12-len(str(weekArray[10]))) if weekArray[10] != None else '            '}│
├─┴─────┴─────┴──────────┬─┤
│{lined_hw_array[10][0]}│V│
│{lined_hw_array[10][1]}└─┤
│{lined_hw_array[10][2]}│{eol + '│' + lined_hw_array[10][3] + '│' if lined_hw_array[10][3] != '                          ' else ''}
├─┬─────┬─────┬────────────┤
│2│{ti[42]}│{ti[43]}│{str(weekArray[11]) + ' '*(12-len(str(weekArray[11]))) if weekArray[11] != None else '            '}│
├─┴─────┴─────┴──────────┬─┤
│{lined_hw_array[11][0]}│V│
│{lined_hw_array[11][1]}└─┤
│{lined_hw_array[11][2]}│{eol + '│' + lined_hw_array[11][3] + '│' if lined_hw_array[11][3] != '                          ' else ''}
├─┬─────┬─────┬────────────┤
│3│{ti[44]}│{ti[45]}│{str(weekArray[12]) + ' '*(12-len(str(weekArray[12]))) if weekArray[12] != None else '            '}│
├─┴─────┴─────┴──────────┬─┤
│{lined_hw_array[12][0]}│V│
│{lined_hw_array[12][1]}└─┤
│{lined_hw_array[12][2]}│{eol + '│' + lined_hw_array[12][3] + '│' if lined_hw_array[12][3] != '                          ' else ''}
├─┬─────┬─────┬────────────┤
│4│{ti[46]}│{ti[47]}│{str(weekArray[13]) + ' '*(12-len(str(weekArray[13]))) if weekArray[13] != None else '            '}│
├─┴─────┴─────┴──────────┬─┤
│{lined_hw_array[13][0]}│V│
│{lined_hw_array[13][1]}└─┤
│{lined_hw_array[13][2]}│{eol + '│' + lined_hw_array[13][3] + '│' if lined_hw_array[13][3] != '                          ' else ''}
├─┬─────┬─────┬────────────┤
│5│{ti[48]}│{ti[49]}│{str(weekArray[14]) + ' '*(12-len(str(weekArray[14]))) if weekArray[14] != None else '            '}│
├─┴─────┴─────┴──────────┬─┤
│{lined_hw_array[14][0]}│V│
│{lined_hw_array[14][1]}└─┤
│{lined_hw_array[14][2]}│{eol + '│' + lined_hw_array[14][3] + '│' if lined_hw_array[14][3] != '                          ' else ''}
├─┬─────┬─────┬────────────┤
│6│{ti[50]}│{ti[51]}│{str(weekArray[15]) + ' '*(12-len(str(weekArray[15]))) if weekArray[15] != None else '            '}│
├─┴─────┴─────┴─────━────┬─┤
│{lined_hw_array[15][0]}│V│
│{lined_hw_array[15][1]}└─┤
│{lined_hw_array[15][2]}│{eol + '│' + lined_hw_array[15][3] + '│' if lined_hw_array[15][3] != '                          ' else ''}{eol + '│' + lined_hw_array[15][4] + '│' if lined_hw_array[15][4] != '                          ' else ''}
├──────────────────────────┤
│WEDNESDAY                 │
├─┬─────┬─────┬────────────┤
│1│{ti[40]}│{ti[41]}│{str(weekArray[10]) + ' '*(12-len(str(weekArray[10]))) if weekArray[10] != None else '            '}│
├─┴─────┴─────┴──────────┬─┤{eol + '│' + lined_hw_array[20][0] + '│V│' if lined_hw_array[20][0] != '                          ' else ''}{eol + '│' + lined_hw_array[20][1] + '└─┤' if lined_hw_array[20][1] != '                          ' else ''}{eol + '│' + lined_hw_array[20][2] + '│' if lined_hw_array[20][2] != '                          ' else ''}{eol + '│' + lined_hw_array[20][3] + '│' if lined_hw_array[20][3] != '                          ' else ''}{eol + '│' + lined_hw_array[20][4] + '│' if lined_hw_array[20][4] != '                          ' else ''}{eol + '│' + lined_hw_array[20][5] + '│' if lined_hw_array[20][5] != '                          ' else ''}{eol + '│' + lined_hw_array[20][6] + '│' if lined_hw_array[20][6] != '                          ' else ''}{eol + '│' + lined_hw_array[20][7] + '│' if lined_hw_array[20][7] != '                          ' else ''}
q
</pre>"""


# lined_hw_array[0][0]
#                ^  ^
#               les li
#               son ne


        eol = '\n'


        s_table = f"""
├─┬─────┬─────┬────────────┤
│1│{ti[40]}│{ti[41]}│{str(weekArray[10]) + ' '*(12-len(str(weekArray[10]))) if weekArray[10] != None else '            '}│
{'├─┼─────┼─────┼────────────┤' if lined_hw_array[20][1] == '                        ' else '├─┴─────┴─────┴──────────┬─┤'}{eol + '│' + lined_hw_array[20][0] + '│V│' if lined_hw_array[20][0] != '                        ' else ''}{eol + '│' + lined_hw_array[20][1] + '└─┤' if lined_hw_array[20][1] != '                        ' else ''}{eol + '│' + lined_hw_array[20][2] + '│' if lined_hw_array[20][2] != '                          ' else ''}{eol + '│' + lined_hw_array[20][3] + '│' if lined_hw_array[20][3] != '                          ' else ''}{eol + '│' + lined_hw_array[20][4] + '│' if lined_hw_array[20][4] != '                          ' else ''}{eol + '│' + lined_hw_array[20][5] + '│' if lined_hw_array[20][5] != '                          ' else ''}{eol + '│' + lined_hw_array[20][6] + '│' if lined_hw_array[20][6] != '                          ' else ''}{eol + '│' + lined_hw_array[20][7] + '│' if lined_hw_array[20][7] != '                          ' else ''}{eol + '├─┬─────┬─────┬────────────┤' if lined_hw_array[20][1] != '                        ' else ''} 
│2│{ti[22]}│{ti[23]}│{str(weekArray[1]) + ' '*(12-len(str(weekArray[1]))) if weekArray[1] != None else '            '}│



├─┴─────┴─────┴──────────┬─┤{eol + '│' + lined_hw_array[21][0] + '│V│' if lined_hw_array[21][0] != '                        ' else ''}{eol + '│' + lined_hw_array[21][1] + '└─┤' if lined_hw_array[21][1] != '                        ' else ''}{eol + '│' + lined_hw_array[21][2] + '│' if lined_hw_array[21][2] != '                          ' else ''}{eol + '│' + lined_hw_array[21][3] + '│' if lined_hw_array[21][3] != '                          ' else ''}{eol + '│' + lined_hw_array[21][4] + '│' if lined_hw_array[21][4] != '                          ' else ''}{eol + '│' + lined_hw_array[21][5] + '│' if lined_hw_array[21][5] != '                          ' else ''}{eol + '│' + lined_hw_array[21][6] + '│' if lined_hw_array[21][6] != '                          ' else ''}{eol + '│' + lined_hw_array[21][7] + '│' if lined_hw_array[21][7] != '                          ' else ''}

        """



        # print("right before error: done_hw_weekArray = ", done_hw_weekArray)

        # for a draft for 10-lesson table refer to 10-lesson_hw_sg_table_draft.txt

        s_table = f"""<pre>
┌──────────────────────────┐
│WEEK {str(int(adding_from_week))} {str(week_calendar_boundaries)}{' '*(20-(len(str(int(adding_from_week)))+len(str(week_calendar_boundaries))))}│
├──────────────────────────┤
│{wd_names[0] + ' '*(26-len(wd_names[0]))}│
├─┬─────┬─────┬────────────┤        
│1│{ti[20]}│{ti[21]}│{str(weekArray[0]) + ' '*(12-len(str(weekArray[0]))) if weekArray[0] != None else '            '}│
{'├─┼─────┼─────┼────────────┤' if lined_hw_array[0][0] == '                        ' else '├─┴─────┴─────┴──────────┬─┤'}{eol + '│' + lined_hw_array[0][0] + '│' + done_hw_weekArray[0] + '│' if lined_hw_array[0][0] != '                        ' else ''}{eol + '│' + lined_hw_array[0][1] + '└─┤' if lined_hw_array[0][1] != '                        ' else ''}{eol + '│' + lined_hw_array[0][2] + '│' if lined_hw_array[0][2] != '                          ' else ''}{eol + '│' + lined_hw_array[0][3] + '│' if lined_hw_array[0][3] != '                          ' else ''}{eol + '│' + lined_hw_array[0][4] + '│' if lined_hw_array[0][4] != '                          ' else ''}{eol + '│' + lined_hw_array[0][5] + '│' if lined_hw_array[0][5] != '                          ' else ''}{eol + '│' + lined_hw_array[0][6] + '│' if lined_hw_array[0][6] != '                          ' else ''}{eol + '│' + lined_hw_array[0][7] + '│' if lined_hw_array[0][7] != '                          ' else ''}{eol + '├─┬─────┬─────┬────────────┤' if lined_hw_array[0][1] != '                        ' else ''}
│2│{ti[22]}│{ti[23]}│{str(weekArray[1]) + ' '*(12-len(str(weekArray[1]))) if weekArray[1] != None else '            '}│
{'├─┼─────┼─────┼────────────┤' if lined_hw_array[1][0] == '                        ' else '├─┴─────┴─────┴──────────┬─┤'}{eol + '│' + lined_hw_array[1][0] + '│' + done_hw_weekArray[1] + '│' if lined_hw_array[1][0] != '                        ' else ''}{eol + '│' + lined_hw_array[1][1] + '└─┤' if lined_hw_array[1][1] != '                        ' else ''}{eol + '│' + lined_hw_array[1][2] + '│' if lined_hw_array[1][2] != '                          ' else ''}{eol + '│' + lined_hw_array[1][3] + '│' if lined_hw_array[1][3] != '                          ' else ''}{eol + '│' + lined_hw_array[1][4] + '│' if lined_hw_array[1][4] != '                          ' else ''}{eol + '│' + lined_hw_array[1][5] + '│' if lined_hw_array[1][5] != '                          ' else ''}{eol + '│' + lined_hw_array[1][6] + '│' if lined_hw_array[1][6] != '                          ' else ''}{eol + '│' + lined_hw_array[1][7] + '│' if lined_hw_array[1][7] != '                          ' else ''}{eol + '├─┬─────┬─────┬────────────┤' if lined_hw_array[1][1] != '                        ' else ''}
│3│{ti[24]}│{ti[25]}│{str(weekArray[2]) + ' '*(12-len(str(weekArray[2]))) if weekArray[2] != None else '            '}│
{'├─┼─────┼─────┼────────────┤' if lined_hw_array[2][0] == '                        ' else '├─┴─────┴─────┴──────────┬─┤'}{eol + '│' + lined_hw_array[2][0] + '│' + done_hw_weekArray[2] + '│' if lined_hw_array[2][0] != '                        ' else ''}{eol + '│' + lined_hw_array[2][1] + '└─┤' if lined_hw_array[2][1] != '                        ' else ''}{eol + '│' + lined_hw_array[2][2] + '│' if lined_hw_array[2][2] != '                          ' else ''}{eol + '│' + lined_hw_array[2][3] + '│' if lined_hw_array[2][3] != '                          ' else ''}{eol + '│' + lined_hw_array[2][4] + '│' if lined_hw_array[2][4] != '                          ' else ''}{eol + '│' + lined_hw_array[2][5] + '│' if lined_hw_array[2][5] != '                          ' else ''}{eol + '│' + lined_hw_array[2][6] + '│' if lined_hw_array[2][6] != '                          ' else ''}{eol + '│' + lined_hw_array[2][7] + '│' if lined_hw_array[2][7] != '                          ' else ''}{eol + '├─┬─────┬─────┬────────────┤' if lined_hw_array[2][1] != '                        ' else ''}
│4│{ti[26]}│{ti[27]}│{str(weekArray[3]) + ' '*(12-len(str(weekArray[3]))) if weekArray[3] != None else '            '}│
{'├─┼─────┼─────┼────────────┤' if lined_hw_array[3][0] == '                        ' else '├─┴─────┴─────┴──────────┬─┤'}{eol + '│' + lined_hw_array[3][0] + '│' + done_hw_weekArray[3] + '│' if lined_hw_array[3][0] != '                        ' else ''}{eol + '│' + lined_hw_array[3][1] + '└─┤' if lined_hw_array[3][1] != '                        ' else ''}{eol + '│' + lined_hw_array[3][2] + '│' if lined_hw_array[3][2] != '                          ' else ''}{eol + '│' + lined_hw_array[3][3] + '│' if lined_hw_array[3][3] != '                          ' else ''}{eol + '│' + lined_hw_array[3][4] + '│' if lined_hw_array[3][4] != '                          ' else ''}{eol + '│' + lined_hw_array[3][5] + '│' if lined_hw_array[3][5] != '                          ' else ''}{eol + '│' + lined_hw_array[3][6] + '│' if lined_hw_array[3][6] != '                          ' else ''}{eol + '│' + lined_hw_array[3][7] + '│' if lined_hw_array[3][7] != '                          ' else ''}{eol + '├─┬─────┬─────┬────────────┤' if lined_hw_array[3][1] != '                        ' else ''}
│5│{ti[28]}│{ti[29]}│{str(weekArray[4]) + ' '*(12-len(str(weekArray[4]))) if weekArray[4] != None else '            '}│
{'├─┼─────┼─────┼────────────┤' if lined_hw_array[4][0] == '                        ' else '├─┴─────┴─────┴──────────┬─┤'}{eol + '│' + lined_hw_array[4][0] + '│' + done_hw_weekArray[4] + '│' if lined_hw_array[4][0] != '                        ' else ''}{eol + '│' + lined_hw_array[4][1] + '└─┤' if lined_hw_array[4][1] != '                        ' else ''}{eol + '│' + lined_hw_array[4][2] + '│' if lined_hw_array[4][2] != '                          ' else ''}{eol + '│' + lined_hw_array[4][3] + '│' if lined_hw_array[4][3] != '                          ' else ''}{eol + '│' + lined_hw_array[4][4] + '│' if lined_hw_array[4][4] != '                          ' else ''}{eol + '│' + lined_hw_array[4][5] + '│' if lined_hw_array[4][5] != '                          ' else ''}{eol + '│' + lined_hw_array[4][6] + '│' if lined_hw_array[4][6] != '                          ' else ''}{eol + '│' + lined_hw_array[4][7] + '│' if lined_hw_array[4][7] != '                          ' else ''}{eol + '├─┬─────┬─────┬────────────┤' if lined_hw_array[4][1] != '                        ' else ''}
│6│{ti[30]}│{ti[31]}│{str(weekArray[5]) + ' '*(12-len(str(weekArray[5]))) if weekArray[5] != None else '            '}│
{'├─┴─────┴─────┴────────────┤' if lined_hw_array[5][0] == '                        ' else '├─┴─────┴─────┴──────────┬─┤'}{eol + '│' + lined_hw_array[5][0] + '│' + done_hw_weekArray[5] + '│' if lined_hw_array[5][0] != '                        ' else ''}{eol + '│' + lined_hw_array[5][1] + '└─┤' if lined_hw_array[5][1] != '                        ' else ''}{eol + '│' + lined_hw_array[5][2] + '│' if lined_hw_array[5][2] != '                          ' else ''}{eol + '│' + lined_hw_array[5][3] + '│' if lined_hw_array[5][3] != '                          ' else ''}{eol + '│' + lined_hw_array[5][4] + '│' if lined_hw_array[5][4] != '                          ' else ''}{eol + '│' + lined_hw_array[5][5] + '│' if lined_hw_array[5][5] != '                          ' else ''}{eol + '│' + lined_hw_array[5][6] + '│' if lined_hw_array[5][6] != '                          ' else ''}{eol + '│' + lined_hw_array[5][7] + '│' if lined_hw_array[5][7] != '                          ' else ''}{eol + '├─┬─────┬─────┬────────────┤' if lined_hw_array[5][1] != '                        ' else ''}
│{wd_names[1] + ' '*(26-len(wd_names[1]))}│
├─┬─────┬─────┬────────────┤
│1│{ti[40]}│{ti[41]}│{str(weekArray[10]) + ' '*(12-len(str(weekArray[10]))) if weekArray[10] != None else '            '}│
{'├─┼─────┼─────┼────────────┤' if lined_hw_array[10][0] == '                        ' else '├─┴─────┴─────┴──────────┬─┤'}{eol + '│' + lined_hw_array[10][0] + '│' + done_hw_weekArray[10] + '│' if lined_hw_array[10][0] != '                        ' else ''}{eol + '│' + lined_hw_array[10][1] + '└─┤' if lined_hw_array[10][1] != '                        ' else ''}{eol + '│' + lined_hw_array[10][2] + '│' if lined_hw_array[10][2] != '                          ' else ''}{eol + '│' + lined_hw_array[10][3] + '│' if lined_hw_array[10][3] != '                          ' else ''}{eol + '│' + lined_hw_array[10][4] + '│' if lined_hw_array[10][4] != '                          ' else ''}{eol + '│' + lined_hw_array[10][5] + '│' if lined_hw_array[10][5] != '                          ' else ''}{eol + '│' + lined_hw_array[10][6] + '│' if lined_hw_array[10][6] != '                          ' else ''}{eol + '│' + lined_hw_array[10][7] + '│' if lined_hw_array[10][7] != '                          ' else ''}{eol + '├─┬─────┬─────┬────────────┤' if lined_hw_array[10][1] != '                        ' else ''}
│2│{ti[42]}│{ti[43]}│{str(weekArray[11]) + ' '*(12-len(str(weekArray[11]))) if weekArray[11] != None else '            '}│
{'├─┼─────┼─────┼────────────┤' if lined_hw_array[11][0] == '                        ' else '├─┴─────┴─────┴──────────┬─┤'}{eol + '│' + lined_hw_array[11][0] + '│' + done_hw_weekArray[11] + '│' if lined_hw_array[11][0] != '                        ' else ''}{eol + '│' + lined_hw_array[11][1] + '└─┤' if lined_hw_array[11][1] != '                        ' else ''}{eol + '│' + lined_hw_array[11][2] + '│' if lined_hw_array[11][2] != '                          ' else ''}{eol + '│' + lined_hw_array[11][3] + '│' if lined_hw_array[11][3] != '                          ' else ''}{eol + '│' + lined_hw_array[11][4] + '│' if lined_hw_array[11][4] != '                          ' else ''}{eol + '│' + lined_hw_array[11][5] + '│' if lined_hw_array[11][5] != '                          ' else ''}{eol + '│' + lined_hw_array[11][6] + '│' if lined_hw_array[11][6] != '                          ' else ''}{eol + '│' + lined_hw_array[11][7] + '│' if lined_hw_array[11][7] != '                          ' else ''}{eol + '├─┬─────┬─────┬────────────┤' if lined_hw_array[11][1] != '                        ' else ''}
│3│{ti[44]}│{ti[45]}│{str(weekArray[12]) + ' '*(12-len(str(weekArray[12]))) if weekArray[12] != None else '            '}│
{'├─┼─────┼─────┼────────────┤' if lined_hw_array[12][0] == '                        ' else '├─┴─────┴─────┴──────────┬─┤'}{eol + '│' + lined_hw_array[12][0] + '│' + done_hw_weekArray[12] + '│' if lined_hw_array[12][0] != '                        ' else ''}{eol + '│' + lined_hw_array[12][1] + '└─┤' if lined_hw_array[12][1] != '                        ' else ''}{eol + '│' + lined_hw_array[12][2] + '│' if lined_hw_array[12][2] != '                          ' else ''}{eol + '│' + lined_hw_array[12][3] + '│' if lined_hw_array[12][3] != '                          ' else ''}{eol + '│' + lined_hw_array[12][4] + '│' if lined_hw_array[12][4] != '                          ' else ''}{eol + '│' + lined_hw_array[12][5] + '│' if lined_hw_array[12][5] != '                          ' else ''}{eol + '│' + lined_hw_array[12][6] + '│' if lined_hw_array[12][6] != '                          ' else ''}{eol + '│' + lined_hw_array[12][7] + '│' if lined_hw_array[12][7] != '                          ' else ''}{eol + '├─┬─────┬─────┬────────────┤' if lined_hw_array[12][1] != '                        ' else ''}
│4│{ti[46]}│{ti[47]}│{str(weekArray[13]) + ' '*(12-len(str(weekArray[13]))) if weekArray[13] != None else '            '}│
{'├─┼─────┼─────┼────────────┤' if lined_hw_array[13][0] == '                        ' else '├─┴─────┴─────┴──────────┬─┤'}{eol + '│' + lined_hw_array[13][0] + '│' + done_hw_weekArray[13] + '│' if lined_hw_array[13][0] != '                        ' else ''}{eol + '│' + lined_hw_array[13][1] + '└─┤' if lined_hw_array[13][1] != '                        ' else ''}{eol + '│' + lined_hw_array[13][2] + '│' if lined_hw_array[13][2] != '                          ' else ''}{eol + '│' + lined_hw_array[13][3] + '│' if lined_hw_array[13][3] != '                          ' else ''}{eol + '│' + lined_hw_array[13][4] + '│' if lined_hw_array[13][4] != '                          ' else ''}{eol + '│' + lined_hw_array[13][5] + '│' if lined_hw_array[13][5] != '                          ' else ''}{eol + '│' + lined_hw_array[13][6] + '│' if lined_hw_array[13][6] != '                          ' else ''}{eol + '│' + lined_hw_array[13][7] + '│' if lined_hw_array[13][7] != '                          ' else ''}{eol + '├─┬─────┬─────┬────────────┤' if lined_hw_array[13][1] != '                        ' else ''}
│5│{ti[48]}│{ti[49]}│{str(weekArray[14]) + ' '*(12-len(str(weekArray[14]))) if weekArray[14] != None else '            '}│
{'├─┼─────┼─────┼────────────┤' if lined_hw_array[14][0] == '                        ' else '├─┴─────┴─────┴──────────┬─┤'}{eol + '│' + lined_hw_array[14][0] + '│' + done_hw_weekArray[14] + '│' if lined_hw_array[14][0] != '                        ' else ''}{eol + '│' + lined_hw_array[14][1] + '└─┤' if lined_hw_array[14][1] != '                        ' else ''}{eol + '│' + lined_hw_array[14][2] + '│' if lined_hw_array[14][2] != '                          ' else ''}{eol + '│' + lined_hw_array[14][3] + '│' if lined_hw_array[14][3] != '                          ' else ''}{eol + '│' + lined_hw_array[14][4] + '│' if lined_hw_array[14][4] != '                          ' else ''}{eol + '│' + lined_hw_array[14][5] + '│' if lined_hw_array[14][5] != '                          ' else ''}{eol + '│' + lined_hw_array[14][6] + '│' if lined_hw_array[14][6] != '                          ' else ''}{eol + '│' + lined_hw_array[14][7] + '│' if lined_hw_array[14][7] != '                          ' else ''}{eol + '├─┬─────┬─────┬────────────┤' if lined_hw_array[14][1] != '                        ' else ''}
│6│{ti[50]}│{ti[51]}│{str(weekArray[15]) + ' '*(12-len(str(weekArray[15]))) if weekArray[15] != None else '            '}│
{'├─┴─────┴─────┴────────────┤' if lined_hw_array[15][0] == '                        ' else '├─┴─────┴─────┴──────────┬─┤'}{eol + '│' + lined_hw_array[15][0] + '│' + done_hw_weekArray[15] + '│' if lined_hw_array[15][0] != '                        ' else ''}{eol + '│' + lined_hw_array[15][1] + '└─┤' if lined_hw_array[15][1] != '                        ' else ''}{eol + '│' + lined_hw_array[15][2] + '│' if lined_hw_array[15][2] != '                          ' else ''}{eol + '│' + lined_hw_array[15][3] + '│' if lined_hw_array[15][3] != '                          ' else ''}{eol + '│' + lined_hw_array[15][4] + '│' if lined_hw_array[15][4] != '                          ' else ''}{eol + '│' + lined_hw_array[15][5] + '│' if lined_hw_array[15][5] != '                          ' else ''}{eol + '│' + lined_hw_array[15][6] + '│' if lined_hw_array[15][6] != '                          ' else ''}{eol + '│' + lined_hw_array[15][7] + '│' if lined_hw_array[15][7] != '                          ' else ''}{eol + '├─┬─────┬─────┬────────────┤' if lined_hw_array[15][1] != '                        ' else ''}
│{wd_names[2] + ' '*(26-len(wd_names[2]))}│
├─┬─────┬─────┬────────────┤
│1│{ti[60]}│{ti[61]}│{str(weekArray[20]) + ' '*(12-len(str(weekArray[20]))) if weekArray[20] != None else '            '}│
{'├─┼─────┼─────┼────────────┤' if lined_hw_array[20][0] == '                        ' else '├─┴─────┴─────┴──────────┬─┤'}{eol + '│' + lined_hw_array[20][0] + '│' + done_hw_weekArray[20] + '│' if lined_hw_array[20][0] != '                        ' else ''}{eol + '│' + lined_hw_array[20][1] + '└─┤' if lined_hw_array[20][1] != '                        ' else ''}{eol + '│' + lined_hw_array[20][2] + '│' if lined_hw_array[20][2] != '                          ' else ''}{eol + '│' + lined_hw_array[20][3] + '│' if lined_hw_array[20][3] != '                          ' else ''}{eol + '│' + lined_hw_array[20][4] + '│' if lined_hw_array[20][4] != '                          ' else ''}{eol + '│' + lined_hw_array[20][5] + '│' if lined_hw_array[20][5] != '                          ' else ''}{eol + '│' + lined_hw_array[20][6] + '│' if lined_hw_array[20][6] != '                          ' else ''}{eol + '│' + lined_hw_array[20][7] + '│' if lined_hw_array[20][7] != '                          ' else ''}{eol + '├─┬─────┬─────┬────────────┤' if lined_hw_array[20][1] != '                        ' else ''}
│2│{ti[62]}│{ti[63]}│{str(weekArray[21]) + ' '*(12-len(str(weekArray[21]))) if weekArray[21] != None else '            '}│
{'├─┼─────┼─────┼────────────┤' if lined_hw_array[21][0] == '                        ' else '├─┴─────┴─────┴──────────┬─┤'}{eol + '│' + lined_hw_array[21][0] + '│' + done_hw_weekArray[21] + '│' if lined_hw_array[21][0] != '                        ' else ''}{eol + '│' + lined_hw_array[21][1] + '└─┤' if lined_hw_array[21][1] != '                        ' else ''}{eol + '│' + lined_hw_array[21][2] + '│' if lined_hw_array[21][2] != '                          ' else ''}{eol + '│' + lined_hw_array[21][3] + '│' if lined_hw_array[21][3] != '                          ' else ''}{eol + '│' + lined_hw_array[21][4] + '│' if lined_hw_array[21][4] != '                          ' else ''}{eol + '│' + lined_hw_array[21][5] + '│' if lined_hw_array[21][5] != '                          ' else ''}{eol + '│' + lined_hw_array[21][6] + '│' if lined_hw_array[21][6] != '                          ' else ''}{eol + '│' + lined_hw_array[21][7] + '│' if lined_hw_array[21][7] != '                          ' else ''}{eol + '├─┬─────┬─────┬────────────┤' if lined_hw_array[21][1] != '                        ' else ''}
│3│{ti[64]}│{ti[65]}│{str(weekArray[22]) + ' '*(12-len(str(weekArray[22]))) if weekArray[22] != None else '            '}│
{'├─┼─────┼─────┼────────────┤' if lined_hw_array[22][0] == '                        ' else '├─┴─────┴─────┴──────────┬─┤'}{eol + '│' + lined_hw_array[22][0] + '│' + done_hw_weekArray[22] + '│' if lined_hw_array[22][0] != '                        ' else ''}{eol + '│' + lined_hw_array[22][1] + '└─┤' if lined_hw_array[22][1] != '                        ' else ''}{eol + '│' + lined_hw_array[22][2] + '│' if lined_hw_array[22][2] != '                          ' else ''}{eol + '│' + lined_hw_array[22][3] + '│' if lined_hw_array[22][3] != '                          ' else ''}{eol + '│' + lined_hw_array[22][4] + '│' if lined_hw_array[22][4] != '                          ' else ''}{eol + '│' + lined_hw_array[22][5] + '│' if lined_hw_array[22][5] != '                          ' else ''}{eol + '│' + lined_hw_array[22][6] + '│' if lined_hw_array[22][6] != '                          ' else ''}{eol + '│' + lined_hw_array[22][7] + '│' if lined_hw_array[22][7] != '                          ' else ''}{eol + '├─┬─────┬─────┬────────────┤' if lined_hw_array[22][1] != '                        ' else ''}
│4│{ti[66]}│{ti[67]}│{str(weekArray[23]) + ' '*(12-len(str(weekArray[23]))) if weekArray[23] != None else '            '}│
{'├─┼─────┼─────┼────────────┤' if lined_hw_array[23][0] == '                        ' else '├─┴─────┴─────┴──────────┬─┤'}{eol + '│' + lined_hw_array[23][0] + '│' + done_hw_weekArray[23] + '│' if lined_hw_array[23][0] != '                        ' else ''}{eol + '│' + lined_hw_array[23][1] + '└─┤' if lined_hw_array[23][1] != '                        ' else ''}{eol + '│' + lined_hw_array[23][2] + '│' if lined_hw_array[23][2] != '                          ' else ''}{eol + '│' + lined_hw_array[23][3] + '│' if lined_hw_array[23][3] != '                          ' else ''}{eol + '│' + lined_hw_array[23][4] + '│' if lined_hw_array[23][4] != '                          ' else ''}{eol + '│' + lined_hw_array[23][5] + '│' if lined_hw_array[23][5] != '                          ' else ''}{eol + '│' + lined_hw_array[23][6] + '│' if lined_hw_array[23][6] != '                          ' else ''}{eol + '│' + lined_hw_array[23][7] + '│' if lined_hw_array[23][7] != '                          ' else ''}{eol + '├─┬─────┬─────┬────────────┤' if lined_hw_array[23][1] != '                        ' else ''}
│5│{ti[68]}│{ti[69]}│{str(weekArray[24]) + ' '*(12-len(str(weekArray[24]))) if weekArray[24] != None else '            '}│
{'├─┼─────┼─────┼────────────┤' if lined_hw_array[24][0] == '                        ' else '├─┴─────┴─────┴──────────┬─┤'}{eol + '│' + lined_hw_array[24][0] + '│' + done_hw_weekArray[24] + '│' if lined_hw_array[24][0] != '                        ' else ''}{eol + '│' + lined_hw_array[24][1] + '└─┤' if lined_hw_array[24][1] != '                        ' else ''}{eol + '│' + lined_hw_array[24][2] + '│' if lined_hw_array[24][2] != '                          ' else ''}{eol + '│' + lined_hw_array[24][3] + '│' if lined_hw_array[24][3] != '                          ' else ''}{eol + '│' + lined_hw_array[24][4] + '│' if lined_hw_array[24][4] != '                          ' else ''}{eol + '│' + lined_hw_array[24][5] + '│' if lined_hw_array[24][5] != '                          ' else ''}{eol + '│' + lined_hw_array[24][6] + '│' if lined_hw_array[24][6] != '                          ' else ''}{eol + '│' + lined_hw_array[24][7] + '│' if lined_hw_array[24][7] != '                          ' else ''}{eol + '├─┬─────┬─────┬────────────┤' if lined_hw_array[24][1] != '                        ' else ''}
│6│{ti[70]}│{ti[71]}│{str(weekArray[25]) + ' '*(12-len(str(weekArray[25]))) if weekArray[25] != None else '            '}│
{'├─┴─────┴─────┴────────────┤' if lined_hw_array[25][0] == '                        ' else '├─┴─────┴─────┴──────────┬─┤'}{eol + '│' + lined_hw_array[25][0] + '│' + done_hw_weekArray[25] + '│' if lined_hw_array[25][0] != '                        ' else ''}{eol + '│' + lined_hw_array[25][1] + '└─┤' if lined_hw_array[25][1] != '                        ' else ''}{eol + '│' + lined_hw_array[25][2] + '│' if lined_hw_array[25][2] != '                          ' else ''}{eol + '│' + lined_hw_array[25][3] + '│' if lined_hw_array[25][3] != '                          ' else ''}{eol + '│' + lined_hw_array[25][4] + '│' if lined_hw_array[25][4] != '                          ' else ''}{eol + '│' + lined_hw_array[25][5] + '│' if lined_hw_array[25][5] != '                          ' else ''}{eol + '│' + lined_hw_array[25][6] + '│' if lined_hw_array[25][6] != '                          ' else ''}{eol + '│' + lined_hw_array[25][7] + '│' if lined_hw_array[25][7] != '                          ' else ''}{eol + '├─┬─────┬─────┬────────────┤' if lined_hw_array[25][1] != '                        ' else ''}
│{wd_names[3] + ' '*(26-len(wd_names[3]))}│
├─┬─────┬─────┬────────────┤
│1│{ti[80]}│{ti[81]}│{str(weekArray[30]) + ' '*(12-len(str(weekArray[30]))) if weekArray[30] != None else '            '}│
{'├─┼─────┼─────┼────────────┤' if lined_hw_array[30][0] == '                        ' else '├─┴─────┴─────┴──────────┬─┤'}{eol + '│' + lined_hw_array[30][0] + '│' + done_hw_weekArray[30] + '│' if lined_hw_array[30][0] != '                        ' else ''}{eol + '│' + lined_hw_array[30][1] + '└─┤' if lined_hw_array[30][1] != '                        ' else ''}{eol + '│' + lined_hw_array[30][2] + '│' if lined_hw_array[30][2] != '                          ' else ''}{eol + '│' + lined_hw_array[30][3] + '│' if lined_hw_array[30][3] != '                          ' else ''}{eol + '│' + lined_hw_array[30][4] + '│' if lined_hw_array[30][4] != '                          ' else ''}{eol + '│' + lined_hw_array[30][5] + '│' if lined_hw_array[30][5] != '                          ' else ''}{eol + '│' + lined_hw_array[30][6] + '│' if lined_hw_array[30][6] != '                          ' else ''}{eol + '│' + lined_hw_array[30][7] + '│' if lined_hw_array[30][7] != '                          ' else ''}{eol + '├─┬─────┬─────┬────────────┤' if lined_hw_array[30][1] != '                        ' else ''}
│2│{ti[82]}│{ti[83]}│{str(weekArray[31]) + ' '*(12-len(str(weekArray[31]))) if weekArray[31] != None else '            '}│
{'├─┼─────┼─────┼────────────┤' if lined_hw_array[31][0] == '                        ' else '├─┴─────┴─────┴──────────┬─┤'}{eol + '│' + lined_hw_array[31][0] + '│' + done_hw_weekArray[31] + '│' if lined_hw_array[31][0] != '                        ' else ''}{eol + '│' + lined_hw_array[31][1] + '└─┤' if lined_hw_array[31][1] != '                        ' else ''}{eol + '│' + lined_hw_array[31][2] + '│' if lined_hw_array[31][2] != '                          ' else ''}{eol + '│' + lined_hw_array[31][3] + '│' if lined_hw_array[31][3] != '                          ' else ''}{eol + '│' + lined_hw_array[31][4] + '│' if lined_hw_array[31][4] != '                          ' else ''}{eol + '│' + lined_hw_array[31][5] + '│' if lined_hw_array[31][5] != '                          ' else ''}{eol + '│' + lined_hw_array[31][6] + '│' if lined_hw_array[31][6] != '                          ' else ''}{eol + '│' + lined_hw_array[31][7] + '│' if lined_hw_array[31][7] != '                          ' else ''}{eol + '├─┬─────┬─────┬────────────┤' if lined_hw_array[31][1] != '                        ' else ''}
│3│{ti[84]}│{ti[85]}│{str(weekArray[32]) + ' '*(12-len(str(weekArray[32]))) if weekArray[32] != None else '            '}│
{'├─┼─────┼─────┼────────────┤' if lined_hw_array[32][0] == '                        ' else '├─┴─────┴─────┴──────────┬─┤'}{eol + '│' + lined_hw_array[32][0] + '│' + done_hw_weekArray[32] + '│' if lined_hw_array[32][0] != '                        ' else ''}{eol + '│' + lined_hw_array[32][1] + '└─┤' if lined_hw_array[32][1] != '                        ' else ''}{eol + '│' + lined_hw_array[32][2] + '│' if lined_hw_array[32][2] != '                          ' else ''}{eol + '│' + lined_hw_array[32][3] + '│' if lined_hw_array[32][3] != '                          ' else ''}{eol + '│' + lined_hw_array[32][4] + '│' if lined_hw_array[32][4] != '                          ' else ''}{eol + '│' + lined_hw_array[32][5] + '│' if lined_hw_array[32][5] != '                          ' else ''}{eol + '│' + lined_hw_array[32][6] + '│' if lined_hw_array[32][6] != '                          ' else ''}{eol + '│' + lined_hw_array[32][7] + '│' if lined_hw_array[32][7] != '                          ' else ''}{eol + '├─┬─────┬─────┬────────────┤' if lined_hw_array[32][1] != '                        ' else ''}
│4│{ti[86]}│{ti[87]}│{str(weekArray[33]) + ' '*(12-len(str(weekArray[33]))) if weekArray[33] != None else '            '}│
{'├─┼─────┼─────┼────────────┤' if lined_hw_array[33][0] == '                        ' else '├─┴─────┴─────┴──────────┬─┤'}{eol + '│' + lined_hw_array[33][0] + '│' + done_hw_weekArray[33] + '│' if lined_hw_array[33][0] != '                        ' else ''}{eol + '│' + lined_hw_array[33][1] + '└─┤' if lined_hw_array[33][1] != '                        ' else ''}{eol + '│' + lined_hw_array[33][2] + '│' if lined_hw_array[33][2] != '                          ' else ''}{eol + '│' + lined_hw_array[33][3] + '│' if lined_hw_array[33][3] != '                          ' else ''}{eol + '│' + lined_hw_array[33][4] + '│' if lined_hw_array[33][4] != '                          ' else ''}{eol + '│' + lined_hw_array[33][5] + '│' if lined_hw_array[33][5] != '                          ' else ''}{eol + '│' + lined_hw_array[33][6] + '│' if lined_hw_array[33][6] != '                          ' else ''}{eol + '│' + lined_hw_array[33][7] + '│' if lined_hw_array[33][7] != '                          ' else ''}{eol + '├─┬─────┬─────┬────────────┤' if lined_hw_array[33][1] != '                        ' else ''}
│5│{ti[88]}│{ti[89]}│{str(weekArray[34]) + ' '*(12-len(str(weekArray[34]))) if weekArray[34] != None else '            '}│
{'├─┼─────┼─────┼────────────┤' if lined_hw_array[34][0] == '                        ' else '├─┴─────┴─────┴──────────┬─┤'}{eol + '│' + lined_hw_array[34][0] + '│' + done_hw_weekArray[34] + '│' if lined_hw_array[34][0] != '                        ' else ''}{eol + '│' + lined_hw_array[34][1] + '└─┤' if lined_hw_array[34][1] != '                        ' else ''}{eol + '│' + lined_hw_array[34][2] + '│' if lined_hw_array[34][2] != '                          ' else ''}{eol + '│' + lined_hw_array[34][3] + '│' if lined_hw_array[34][3] != '                          ' else ''}{eol + '│' + lined_hw_array[34][4] + '│' if lined_hw_array[34][4] != '                          ' else ''}{eol + '│' + lined_hw_array[34][5] + '│' if lined_hw_array[34][5] != '                          ' else ''}{eol + '│' + lined_hw_array[34][6] + '│' if lined_hw_array[34][6] != '                          ' else ''}{eol + '│' + lined_hw_array[34][7] + '│' if lined_hw_array[34][7] != '                          ' else ''}{eol + '├─┬─────┬─────┬────────────┤' if lined_hw_array[34][1] != '                        ' else ''}
│6│{ti[90]}│{ti[91]}│{str(weekArray[35]) + ' '*(12-len(str(weekArray[35]))) if weekArray[35] != None else '            '}│
{'├─┴─────┴─────┴────────────┤' if lined_hw_array[35][0] == '                        ' else '├─┴─────┴─────┴──────────┬─┤'}{eol + '│' + lined_hw_array[35][0] + '│' + done_hw_weekArray[35] + '│' if lined_hw_array[35][0] != '                        ' else ''}{eol + '│' + lined_hw_array[35][1] + '└─┤' if lined_hw_array[35][1] != '                        ' else ''}{eol + '│' + lined_hw_array[35][2] + '│' if lined_hw_array[35][2] != '                          ' else ''}{eol + '│' + lined_hw_array[35][3] + '│' if lined_hw_array[35][3] != '                          ' else ''}{eol + '│' + lined_hw_array[35][4] + '│' if lined_hw_array[35][4] != '                          ' else ''}{eol + '│' + lined_hw_array[35][5] + '│' if lined_hw_array[35][5] != '                          ' else ''}{eol + '│' + lined_hw_array[35][6] + '│' if lined_hw_array[35][6] != '                          ' else ''}{eol + '│' + lined_hw_array[35][7] + '│' if lined_hw_array[35][7] != '                          ' else ''}{eol + '├─┬─────┬─────┬────────────┤' if lined_hw_array[35][1] != '                        ' else ''}
│{wd_names[4] + ' '*(26-len(wd_names[4]))}│
├─┬─────┬─────┬────────────┤
│1│{ti[100]}│{ti[101]}│{str(weekArray[40]) + ' '*(12-len(str(weekArray[40]))) if weekArray[40] != None else '            '}│
{'├─┼─────┼─────┼────────────┤' if lined_hw_array[40][0] == '                        ' else '├─┴─────┴─────┴──────────┬─┤'}{eol + '│' + lined_hw_array[40][0] + '│' + done_hw_weekArray[40] + '│' if lined_hw_array[40][0] != '                        ' else ''}{eol + '│' + lined_hw_array[40][1] + '└─┤' if lined_hw_array[40][1] != '                        ' else ''}{eol + '│' + lined_hw_array[40][2] + '│' if lined_hw_array[40][2] != '                          ' else ''}{eol + '│' + lined_hw_array[40][3] + '│' if lined_hw_array[40][3] != '                          ' else ''}{eol + '│' + lined_hw_array[40][4] + '│' if lined_hw_array[40][4] != '                          ' else ''}{eol + '│' + lined_hw_array[40][5] + '│' if lined_hw_array[40][5] != '                          ' else ''}{eol + '│' + lined_hw_array[40][6] + '│' if lined_hw_array[40][6] != '                          ' else ''}{eol + '│' + lined_hw_array[40][7] + '│' if lined_hw_array[40][7] != '                          ' else ''}{eol + '├─┬─────┬─────┬────────────┤' if lined_hw_array[40][1] != '                        ' else ''}
│2│{ti[102]}│{ti[103]}│{str(weekArray[41]) + ' '*(12-len(str(weekArray[41]))) if weekArray[41] != None else '            '}│
{'├─┼─────┼─────┼────────────┤' if lined_hw_array[41][0] == '                        ' else '├─┴─────┴─────┴──────────┬─┤'}{eol + '│' + lined_hw_array[41][0] + '│' + done_hw_weekArray[41] + '│' if lined_hw_array[41][0] != '                        ' else ''}{eol + '│' + lined_hw_array[41][1] + '└─┤' if lined_hw_array[41][1] != '                        ' else ''}{eol + '│' + lined_hw_array[41][2] + '│' if lined_hw_array[41][2] != '                          ' else ''}{eol + '│' + lined_hw_array[41][3] + '│' if lined_hw_array[41][3] != '                          ' else ''}{eol + '│' + lined_hw_array[41][4] + '│' if lined_hw_array[41][4] != '                          ' else ''}{eol + '│' + lined_hw_array[41][5] + '│' if lined_hw_array[41][5] != '                          ' else ''}{eol + '│' + lined_hw_array[41][6] + '│' if lined_hw_array[41][6] != '                          ' else ''}{eol + '│' + lined_hw_array[41][7] + '│' if lined_hw_array[41][7] != '                          ' else ''}{eol + '├─┬─────┬─────┬────────────┤' if lined_hw_array[41][1] != '                        ' else ''}
│3│{ti[104]}│{ti[105]}│{str(weekArray[42]) + ' '*(12-len(str(weekArray[42]))) if weekArray[42] != None else '            '}│
{'├─┼─────┼─────┼────────────┤' if lined_hw_array[42][0] == '                        ' else '├─┴─────┴─────┴──────────┬─┤'}{eol + '│' + lined_hw_array[42][0] + '│' + done_hw_weekArray[42] + '│' if lined_hw_array[42][0] != '                        ' else ''}{eol + '│' + lined_hw_array[42][1] + '└─┤' if lined_hw_array[42][1] != '                        ' else ''}{eol + '│' + lined_hw_array[42][2] + '│' if lined_hw_array[42][2] != '                          ' else ''}{eol + '│' + lined_hw_array[42][3] + '│' if lined_hw_array[42][3] != '                          ' else ''}{eol + '│' + lined_hw_array[42][4] + '│' if lined_hw_array[42][4] != '                          ' else ''}{eol + '│' + lined_hw_array[42][5] + '│' if lined_hw_array[42][5] != '                          ' else ''}{eol + '│' + lined_hw_array[42][6] + '│' if lined_hw_array[42][6] != '                          ' else ''}{eol + '│' + lined_hw_array[42][7] + '│' if lined_hw_array[42][7] != '                          ' else ''}{eol + '├─┬─────┬─────┬────────────┤' if lined_hw_array[42][1] != '                        ' else ''}
│4│{ti[106]}│{ti[107]}│{str(weekArray[43]) + ' '*(12-len(str(weekArray[43]))) if weekArray[43] != None else '            '}│
{'├─┼─────┼─────┼────────────┤' if lined_hw_array[43][0] == '                        ' else '├─┴─────┴─────┴──────────┬─┤'}{eol + '│' + lined_hw_array[43][0] + '│' + done_hw_weekArray[43] + '│' if lined_hw_array[43][0] != '                        ' else ''}{eol + '│' + lined_hw_array[43][1] + '└─┤' if lined_hw_array[43][1] != '                        ' else ''}{eol + '│' + lined_hw_array[43][2] + '│' if lined_hw_array[43][2] != '                          ' else ''}{eol + '│' + lined_hw_array[43][3] + '│' if lined_hw_array[43][3] != '                          ' else ''}{eol + '│' + lined_hw_array[43][4] + '│' if lined_hw_array[43][4] != '                          ' else ''}{eol + '│' + lined_hw_array[43][5] + '│' if lined_hw_array[43][5] != '                          ' else ''}{eol + '│' + lined_hw_array[43][6] + '│' if lined_hw_array[43][6] != '                          ' else ''}{eol + '│' + lined_hw_array[43][7] + '│' if lined_hw_array[43][7] != '                          ' else ''}{eol + '├─┬─────┬─────┬────────────┤' if lined_hw_array[43][1] != '                        ' else ''}
│5│{ti[108]}│{ti[109]}│{str(weekArray[44]) + ' '*(12-len(str(weekArray[44]))) if weekArray[44] != None else '            '}│
{'├─┼─────┼─────┼────────────┤' if lined_hw_array[44][0] == '                        ' else '├─┴─────┴─────┴──────────┬─┤'}{eol + '│' + lined_hw_array[44][0] + '│' + done_hw_weekArray[44] + '│' if lined_hw_array[44][0] != '                        ' else ''}{eol + '│' + lined_hw_array[44][1] + '└─┤' if lined_hw_array[44][1] != '                        ' else ''}{eol + '│' + lined_hw_array[44][2] + '│' if lined_hw_array[44][2] != '                          ' else ''}{eol + '│' + lined_hw_array[44][3] + '│' if lined_hw_array[44][3] != '                          ' else ''}{eol + '│' + lined_hw_array[44][4] + '│' if lined_hw_array[44][4] != '                          ' else ''}{eol + '│' + lined_hw_array[44][5] + '│' if lined_hw_array[44][5] != '                          ' else ''}{eol + '│' + lined_hw_array[44][6] + '│' if lined_hw_array[44][6] != '                          ' else ''}{eol + '│' + lined_hw_array[44][7] + '│' if lined_hw_array[44][7] != '                          ' else ''}{eol + '├─┬─────┬─────┬────────────┤' if lined_hw_array[44][1] != '                        ' else ''}
│6│{ti[110]}│{ti[111]}│{str(weekArray[45]) + ' '*(12-len(str(weekArray[45]))) if weekArray[45] != None else '            '}│
{'├─┴─────┴─────┴────────────┤' if lined_hw_array[45][0] == '                        ' else '├─┴─────┴─────┴──────────┬─┤'}{eol + '│' + lined_hw_array[45][0] + '│' + done_hw_weekArray[45] + '│' if lined_hw_array[45][0] != '                        ' else ''}{eol + '│' + lined_hw_array[45][1] + '└─┤' if lined_hw_array[45][1] != '                        ' else ''}{eol + '│' + lined_hw_array[45][2] + '│' if lined_hw_array[45][2] != '                          ' else ''}{eol + '│' + lined_hw_array[45][3] + '│' if lined_hw_array[45][3] != '                          ' else ''}{eol + '│' + lined_hw_array[45][4] + '│' if lined_hw_array[45][4] != '                          ' else ''}{eol + '│' + lined_hw_array[45][5] + '│' if lined_hw_array[45][5] != '                          ' else ''}{eol + '│' + lined_hw_array[45][6] + '│' if lined_hw_array[45][6] != '                          ' else ''}{eol + '│' + lined_hw_array[45][7] + '│' if lined_hw_array[45][7] != '                          ' else ''}{eol + '├─┬─────┬─────┬────────────┤' if lined_hw_array[45][1] != '                        ' else ''}        
│{wd_names[5] + ' '*(26-len(wd_names[5]))}│
├─┬─────┬─────┬────────────┤
│1│{ti[120]}│{ti[121]}│{str(weekArray[50]) + ' '*(12-len(str(weekArray[50]))) if weekArray[50] != None else '            '}│
{'├─┼─────┼─────┼────────────┤' if lined_hw_array[50][0] == '                        ' else '├─┴─────┴─────┴──────────┬─┤'}{eol + '│' + lined_hw_array[50][0] + '│' + done_hw_weekArray[50] + '│' if lined_hw_array[50][0] != '                        ' else ''}{eol + '│' + lined_hw_array[50][1] + '└─┤' if lined_hw_array[50][1] != '                        ' else ''}{eol + '│' + lined_hw_array[50][2] + '│' if lined_hw_array[50][2] != '                          ' else ''}{eol + '│' + lined_hw_array[50][3] + '│' if lined_hw_array[50][3] != '                          ' else ''}{eol + '│' + lined_hw_array[50][4] + '│' if lined_hw_array[50][4] != '                          ' else ''}{eol + '│' + lined_hw_array[50][5] + '│' if lined_hw_array[50][5] != '                          ' else ''}{eol + '│' + lined_hw_array[50][6] + '│' if lined_hw_array[50][6] != '                          ' else ''}{eol + '│' + lined_hw_array[50][7] + '│' if lined_hw_array[50][7] != '                          ' else ''}{eol + '├─┬─────┬─────┬────────────┤' if lined_hw_array[50][1] != '                        ' else ''}
│2│{ti[122]}│{ti[123]}│{str(weekArray[51]) + ' '*(12-len(str(weekArray[51]))) if weekArray[51] != None else '            '}│
{'├─┼─────┼─────┼────────────┤' if lined_hw_array[51][0] == '                        ' else '├─┴─────┴─────┴──────────┬─┤'}{eol + '│' + lined_hw_array[51][0] + '│' + done_hw_weekArray[51] + '│' if lined_hw_array[51][0] != '                        ' else ''}{eol + '│' + lined_hw_array[51][1] + '└─┤' if lined_hw_array[51][1] != '                        ' else ''}{eol + '│' + lined_hw_array[51][2] + '│' if lined_hw_array[51][2] != '                          ' else ''}{eol + '│' + lined_hw_array[51][3] + '│' if lined_hw_array[51][3] != '                          ' else ''}{eol + '│' + lined_hw_array[51][4] + '│' if lined_hw_array[51][4] != '                          ' else ''}{eol + '│' + lined_hw_array[51][5] + '│' if lined_hw_array[51][5] != '                          ' else ''}{eol + '│' + lined_hw_array[51][6] + '│' if lined_hw_array[51][6] != '                          ' else ''}{eol + '│' + lined_hw_array[51][7] + '│' if lined_hw_array[51][7] != '                          ' else ''}{eol + '├─┬─────┬─────┬────────────┤' if lined_hw_array[51][1] != '                        ' else ''}
│3│{ti[124]}│{ti[125]}│{str(weekArray[52]) + ' '*(12-len(str(weekArray[52]))) if weekArray[52] != None else '            '}│
{'├─┼─────┼─────┼────────────┤' if lined_hw_array[52][0] == '                        ' else '├─┴─────┴─────┴──────────┬─┤'}{eol + '│' + lined_hw_array[52][0] + '│' + done_hw_weekArray[52] + '│' if lined_hw_array[52][0] != '                        ' else ''}{eol + '│' + lined_hw_array[52][1] + '└─┤' if lined_hw_array[52][1] != '                        ' else ''}{eol + '│' + lined_hw_array[52][2] + '│' if lined_hw_array[52][2] != '                          ' else ''}{eol + '│' + lined_hw_array[52][3] + '│' if lined_hw_array[52][3] != '                          ' else ''}{eol + '│' + lined_hw_array[52][4] + '│' if lined_hw_array[52][4] != '                          ' else ''}{eol + '│' + lined_hw_array[52][5] + '│' if lined_hw_array[52][5] != '                          ' else ''}{eol + '│' + lined_hw_array[52][6] + '│' if lined_hw_array[52][6] != '                          ' else ''}{eol + '│' + lined_hw_array[52][7] + '│' if lined_hw_array[52][7] != '                          ' else ''}{eol + '├─┬─────┬─────┬────────────┤' if lined_hw_array[52][1] != '                        ' else ''}
│4│{ti[126]}│{ti[127]}│{str(weekArray[53]) + ' '*(12-len(str(weekArray[53]))) if weekArray[53] != None else '            '}│
{'├─┼─────┼─────┼────────────┤' if lined_hw_array[53][0] == '                        ' else '├─┴─────┴─────┴──────────┬─┤'}{eol + '│' + lined_hw_array[53][0] + '│' + done_hw_weekArray[53] + '│' if lined_hw_array[53][0] != '                        ' else ''}{eol + '│' + lined_hw_array[53][1] + '└─┤' if lined_hw_array[53][1] != '                        ' else ''}{eol + '│' + lined_hw_array[53][2] + '│' if lined_hw_array[53][2] != '                          ' else ''}{eol + '│' + lined_hw_array[53][3] + '│' if lined_hw_array[53][3] != '                          ' else ''}{eol + '│' + lined_hw_array[53][4] + '│' if lined_hw_array[53][4] != '                          ' else ''}{eol + '│' + lined_hw_array[53][5] + '│' if lined_hw_array[53][5] != '                          ' else ''}{eol + '│' + lined_hw_array[53][6] + '│' if lined_hw_array[53][6] != '                          ' else ''}{eol + '│' + lined_hw_array[53][7] + '│' if lined_hw_array[53][7] != '                          ' else ''}{eol + '├─┬─────┬─────┬────────────┤' if lined_hw_array[53][1] != '                        ' else ''}
│5│{ti[128]}│{ti[129]}│{str(weekArray[54]) + ' '*(12-len(str(weekArray[54]))) if weekArray[54] != None else '            '}│
{'├─┼─────┼─────┼────────────┤' if lined_hw_array[54][0] == '                        ' else '├─┴─────┴─────┴──────────┬─┤'}{eol + '│' + lined_hw_array[54][0] + '│' + done_hw_weekArray[54] + '│' if lined_hw_array[54][0] != '                        ' else ''}{eol + '│' + lined_hw_array[54][1] + '└─┤' if lined_hw_array[54][1] != '                        ' else ''}{eol + '│' + lined_hw_array[54][2] + '│' if lined_hw_array[54][2] != '                          ' else ''}{eol + '│' + lined_hw_array[54][3] + '│' if lined_hw_array[54][3] != '                          ' else ''}{eol + '│' + lined_hw_array[54][4] + '│' if lined_hw_array[54][4] != '                          ' else ''}{eol + '│' + lined_hw_array[54][5] + '│' if lined_hw_array[54][5] != '                          ' else ''}{eol + '│' + lined_hw_array[54][6] + '│' if lined_hw_array[54][6] != '                          ' else ''}{eol + '│' + lined_hw_array[54][7] + '│' if lined_hw_array[54][7] != '                          ' else ''}{eol + '├─┬─────┬─────┬────────────┤' if lined_hw_array[54][1] != '                        ' else ''}
│6│{ti[130]}│{ti[131]}│{str(weekArray[55]) + ' '*(12-len(str(weekArray[55]))) if weekArray[55] != None else '            '}│
{'├─┴─────┴─────┴────────────┤' if lined_hw_array[55][0] == '                        ' else '├─┴─────┴─────┴──────────┬─┤'}{eol + '│' + lined_hw_array[55][0] + '│' + done_hw_weekArray[55] + '│' if lined_hw_array[55][0] != '                        ' else ''}{eol + '│' + lined_hw_array[55][1] + '└─┤' if lined_hw_array[55][1] != '                        ' else ''}{eol + '│' + lined_hw_array[55][2] + '│' if lined_hw_array[55][2] != '                          ' else ''}{eol + '│' + lined_hw_array[55][3] + '│' if lined_hw_array[55][3] != '                          ' else ''}{eol + '│' + lined_hw_array[55][4] + '│' if lined_hw_array[55][4] != '                          ' else ''}{eol + '│' + lined_hw_array[55][5] + '│' if lined_hw_array[55][5] != '                          ' else ''}{eol + '│' + lined_hw_array[55][6] + '│' if lined_hw_array[55][6] != '                          ' else ''}{eol + '│' + lined_hw_array[55][7] + '│' if lined_hw_array[55][7] != '                          ' else ''}{eol + '└─┴─────┴─────┴────────────┘' if lined_hw_array[55][1] != '                        ' else ''}                
│TABLE ID: {table_user_in + ' '*(16-len(table_user_in))}│
└──────────────────────────┘
</pre>"""
        
        # print(lined_hw_array[2][0])

        #separated_version_s_table = 




    else:
        pass





        # else:
        #     pass


    # ┌──────────────────────────┐
    # │WEEK 7: HW                │
    # ├──────────────────────────┤
    # │MONDAY                    │
    # ├─┬─────┬─────┬────────────┤
    # │1│08:20│09:55│            │
    # ├─┴─────┴─────┴──────────┬─┤
    # │Read pages 1-10 in a    │✓│
    # │textbook N.Y.A., compl. └─┤
    # │tasks 11-12 wb Kawa-II    │
    # ├─┬─────┬─────┬────────────┤
    # │2│10:05│11:40│            │
    # ├─┼─────┼─────┼────────────┤
    # │3│12:20│13:55│            │
    # ├─┼─────┼─────┼────────────┤
    # │4│14:05│15:40│            │
    # ├─┼─────┼─────┼────────────┤
    # │5│15:50│17:25│            │
    # ├─┼─────┼─────┼────────────┤
    # │6│17:35│19:10│            │
    # └─┴─────┴─────┴────────────┘

    print("END OF FORMSEMIGRAPHICTABLE EXECUTION IN: ", time.time() - start_fst_timestamp)


# Commands

async def done_command(update: Update, context: ContextTypes.DEFAULT_TYPE, overwrite_update_message=None):
    user_id = update.message.chat.id
    await getUserInfo(update.message.chat.id)
    await getCurrentTemporalInfo()
    # await getToLesFromCurrent()
    try:
        if overwrite_update_message is not None:
            text = overwrite_update_message
        else:
            # access the text in the message object(member inside update)
            text = update.message.text
        # split the text into words
        words = text.split()
        # print(text)

        # check if the command is formed correctly
        if len(words) < 3 or len(words) > 5:
            raise ValueError("ERROR 841: INVALID COMMAND")

        command = words[0]
        week_number = words[1]
        day_of_week = int(words[2])
        lesson_number = int(words[3])
        if week_number == 'c':
            week_number = current_week_utz
        elif week_number == 'n':
            week_number = current_week_utz + 1
        else:
            week_number = int(week_number)
        
            # The additional subarray
        new_data = [0, time.time(), update.message.chat.id, 'md', table_user_in, week_number, day_of_week, lesson_number, '✓', utz, 0, 0, 0, 0, 0,]

        await log(new_data)


        await update.message.reply_text(f'✓-ing lesson number {lesson_number} in week {int(week_number)}, day {day_of_week} in {table_user_in}')
    
    except ValueError as e:
        # if anything goes wrong, tell the user
        await update.message.reply_text(str(e))


async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Select a language"""

    with open('start_logs.txt', 'a') as f:
        f.write(f'{datetime.now()}: User {update.message.chat.id} {update.message.chat.username} started the bot in {(update.message.from_user.language_code)} language\n')
    
    # print(update.message.from_user.language_code)
    if update.message.from_user.language_code == 'ru':
        await update.message.reply_text("""Добро пожаловать в WikiSchedule!

Вас когда-нибудь раздражало, что каждый ученик в вашей группе должен записывать одно и то же общее расписание? Набирать общее домашнее задание в их локальном офлайн-приложении, а затем сверять его и конспекты в поисках ошибок через обычный мессенджер?

Хорошая новость — вы, вероятно, нашли решение. С помощью бота WS вы можете составить единое расписание для всей группы. Всего один вклад - вместо 15+ - для всех!
                                        
Вы используете русскую языковую версию. Она была определена на основе языковых настроек вашего устройства. English version is also available.
                                        
Ознакомьтесь с подробным руководством с помощью команды /help.""", parse_mode="HTML")

    else:
        await update.message.reply_text(f"""Welcome to WikiSchedule!

Ever found annoying that every student in your class should write down the same common schedule you all share? Type your common homework to their offline timetable app and later check it and notes out in search for misunderstandings via a regular messenger?

Good news — you've probably found the solution. With WS bot, you can have the same schedule for the whole group. Only one contribution — instead of 15+ — for everyone to use!
                                        
You are using the international language version (English). It was determined based on language settings of your device. Russian version is also available.
                                        
View a detailed tutorial with /help command.""", parse_mode="HTML")


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Sending a message with documentation"""
    # print(update.message.from_user.language_code)
    if update.message.from_user.language_code == 'ru':
        await update.message.reply_text("""Добро пожаловать в WikiSchedule!

Вы можете войти в таблицы, в которые были приглашены с помощью команды /lg. Через пробел введите id расписания.

Пример синтаксиса:

<pre>/lg 1-MIKU</pre>

Если вы получили пригласительный код, добавьте его после id таблицы через пробел.


Вы можете создать новые таблицы с помощью команды /cs ([c]reate [s]chedule). Через пробел добавьте часовой пояс в секундах (например, UTC+04:00 это +14400). После этого можно добавить желаемое название [опционально]. Если оно занято, то будет заменено сгенерированным. Создав расписание, вы станете его единственным администратором.

Пример синтаксиса:

<pre>/cs +14400</pre>


Приглашайте новых пользователей с помощью команды /au ([a]dd [u]ser). Через пробел введите id или username пользователя.

Пример синтаксиса:

<pre>/au 5725769420</pre>

Если вы отправите просто "/au", то будет сгенерирован код приглашения.
                                        

Вызовите расписание на сегодня командой /today.


Вы можете получить расписаниe на неделю с помощью команды /ls. Для просмотра домашнего задания используйте команду /ls_hw, а для просмотра конспектов и заметок — /ls_n. Чтобы увидеть информацию для конкретной недели, введите её номер после команды /ls(_hw|_n).


Добавить уроки в расписание можно с помощью команды /al. Разделяя пробелами, введите номер недели (начиная с понедельника, 10 июля 2023 года, 0:00:00 UTC, его можно получить с помощью команды /ls), день недели, номер урока и id урока (не может быть числом). Опционально можно добавить (непосредственно перед идентификатором урока) уровень подгруппы (0 - только для вас, 1 - для вашей таблицы, 2 - для взаимосвязанных таблиц) и эксклюзивность мероприятия (Разовое мероприятие? 0. Для всех следующих недель, пока не будет добавлен другой урок? 1). В конце можно добавить номер кабинета (не более 5 символов).

Пример синтаксиса:

<pre>/al 69 1 2 GLing</pre>

Будет назначено занятие по general linguistics на неделю 69, день 1, занятие 2
                                    
<pre>\empty</pre> на месте id предмета или номера кабинета освободит слот.

Максимальная длина id урока - 12 символов, хотя рекомендуется сократить это число до 6 - так он будет совместим со всеми видами семиграфических таблиц. Он должен состоять из одного слова (например, "GenLing" и "gen_ling" допустимы, "gen ling" - нет).

Разбор синтаксиса: (необязательные поля указаны в квадратных скобках):

<pre>
/al 5 2 4 [1] [1] АнгФ [A420]

 ↑  ↑ ↑ ↑  ↑   ↑   ↑     ↑
 C  W D L  L   E   L     C 
 M  E A E  V   X   E     A
 D  E Y S  L       S     B
    K   №          |
                   I
                   D
</pre>
                                        
Если указали LVL, не пропускайте EX.

LVL добавляет уровень регистра, это функция в разработке, пока не трогайте ее. Это необязательное к добавлению число будет определять добавление новых данных во взаимосвязанные таблицы.

Вместо "5" можно написать "c" для добавления к текущей неделе и "n" для добавления к следующей.

                                    
Добавить домашнее задание можно с помощью команды /ah. Синтаксис команды:

<pre>
/ah 5 2 4 [1] p46 t32 tb Utane

 ↑  ↑ ↑ ↑  ↑         ↑
 C  W D L  L         H
 M  E A E  V         W
 D  E Y S  L
    K   №
</pre>

[В РАЗРАБОТКЕ:] Если номера пропущены, то HW будет добавлено к следующему уроку с тем же id.

Отметить выполненное домашнее задание можно командой /done. Отметку увидите только вы.

Разбор синтаксиса:

<pre>
/done n 2 4

  ↑   ↑ ↑ ↑
  C   W D L
  M   E A E
  D   E Y S
      K   №
</pre>


Добавляйте конспекты с помощью команды /an ([а]dd [n]otes). Разбор синтаксиса:

<pre>
/an 5 2 4 [1] We're no strangers to love
You know the rules and so do I (do I)
A full commitment's what I'm thinking of
You wouldn't get this from any other guy

 ↑  ↑ ↑ ↑  ↑       ↑
 C  W D L  L       N
 M  E A E  V       T
 D  E Y S  L
    K   №
</pre>

[В РАЗРАБОТКЕ:] С помощью этой команды можно загрузить изображение. Количество загружаемых изображений ограничено 120 в час.""", parse_mode="HTML")
        await update.message.reply_text("""Перемещение уроков осуществляется с помощью команды /mv.

Разбор синтаксиса:
                                        
<pre>
/mv c 2 3 c 2 1

 ↑  ↑ ↑ ↑ ↑ ↑ ↑
 C  W D L W D L
 M  E A E E A E
 D  E Y S E Y S
    K   № K   №
   └────┘└─────┘
     что   куда
</pre>

Также перемещаются домашние задания и заметки, которые относятся к выбранному пункту (то есть не те, которые относятся к последующим неделям). В будущем это может измениться.

                   
Чтобы задать время начала и конца отдельных уроков, используйте команду /set_temporal.

В следующем примере текст после "#" (до следующей строки) приведён для разъяснения, не включайте его в свою команду.

Пример синтаксиса:

<pre>
/set_temporal
08:20 09:55  # нач и кон 1 урока
10:05 11:40  # нач и кон 2-ого
12:20 13:55  # и так далее
14:05 15:40
15:50 17:25
17:35 19:10
00:00 00:00
00:00 00:00  # этот блок — универсальное время
00:00 00:00  # если необходимо составить другое расписание на определенный день
00:00 00:00  # пишите "00:00 00:00", пока не достигните 10 уроков

01:01 01:02  # это особенное для понедельника время
01:03 01:04  # можно ограничиться первым блоком
01:05 01:06  # если занятия начинаются и заканчиваются в одно и то же время каждый день.
01:07 01:08
01:09 01:10
01:11 01:12
00:00 00:00
00:00 00:00
00:00 00:00
00:00 00:00  # если же нет, продолжайте до конца недели.

02:01 02:02  # вторник
02:03 02:04
...
</pre>

Время всегда должно быть в формате hh:mm, всегда 5 символов. "9:30" — недействительно, "09:30" — допустимо.


<pre>────────────────────────────</pre>

Если эта линия растянулась на 2 строки, попробуйте уменьшить размер шрифта, иначе семиграфическая таблица будет отображаться некорректно.

Если вам когда-нибудь понадобится более 6 уроков, или если таблица отображается некорректно, а менять настройки шрифта не хочется, можно включить/выключить семиграфический режим командой /tg_sg. Таблицы будут выглядеть не так красиво, зато станут более надежными. Если вам когда-нибудь потребуется использовать 8 или более уроков, не стесняйтесь, пишите мне, если это кому-то понадобится, я добавлю такую возможность.

Если у вас возникнут вопросы или предложения, пожалуйста, напишите мне: @carbon_starlight""", parse_mode = "HTML")

    else:
        await update.message.reply_text(_("""Welcome to WikiSchedule!

Ever found annoying that every student in your class should write down the same common schedule you all share? Type your common homework to their offline timetable app and later check it and notes out in search for misunderstandings via a regular messenger?

Good news — you've probably found the solution. With WS bot, you can have the same schedule for the whole group. Only one contribution — instead of 15+ — for everyone to use!


Log in to tables you are invited to with /lg command. Separated with a space, enter table id.

Syntax example:

<pre>/lg 1-MIKU</pre>

If you got an invitation code, add it after table name, separated with a space.


Create new schedules with /cs command. Separated with a space, add it's time zone in seconds (for example, UTC+04:00 is +14400). After it you can add a desired name [optional]. If taken, in will be replaced with a generated one. Upon creating a schedule, you will become it's only admin.

Syntax example:

<pre>/cs +14400</pre>


Invite new users with /au command. Separated with a space, enter user id. Please, note: not handle, id, digits only.

Syntax example:

<pre>/au 5725769420</pre>

If you will send just "/au", it will generate an invitation code.
                                          

List today lessons with /today command.


List schedule for a week with /ls command. Use /ls_hw to see homework, or /ls_n to see notes. To see info for a particular week number, enter it after /ls(_hw|_n) command.


Add lessons to schedule with /al command. Separated with spaces, enter week number (since Monday, 10 July 2023, 0:00:00 UTC, you can get it with /ls command), day of week, lesson number and lesson id (cannot be a number). Optionally you can add (right before lesson id) a subgroup level (0 — for you only, 1 — your table, 2 — for interconnected tables) and exclusiveness of event (one-time event? 0. Keep until cancelation? 1). At the end you can add cabinet number (4 characters max).

Syntax example:

<pre>/al 69 1 2 GLing</pre>

It will schedule a lesson on general linguistics to week 69, day 1, lesson 2
                                    
<pre>\empty</pre> on the place of les_id or room_number will free up a slot

Max length of lesson id is 12 characters, althrough it's highly recomended to keep this number down to 7 -- this way it will be compatable with all kinds of semigraphic tables. It should be one word (e.g. "GenLing" and "gen_ling" are acceptable, "gen ling" is not). 

Breakdown (optional fields are shown in square brackets):

<pre>
/al 5 2 4 [1] [1] АнгФ [A420]

 ↑  ↑ ↑ ↑  ↑   ↑   ↑     ↑
 C  W D L  L   E   L     C 
 M  E A E  V   X   E     A
 D  E Y S  L       S     B
    K   №          |
                   I
                   D
</pre>

LVL adds register level, it's a function in development, don't touch it yet. This optional-to-add number will determine addition of new data to interconnected tables.

Instead of "5" you can write "c" to add to the current week and "n" for the next one.

                                    
Add homework with /ah command. Syntax breakdown:

<pre>
/ah 5 2 4 [1] p46 t32 tb Utane

 ↑  ↑ ↑ ↑  ↑         ↑
 C  W D L  L         H
 M  E A E  V         W
 D  E Y S  L
    K   №
</pre>

[IN DEVELOPMENT:] If numbers skipped, HW will be added to the next lesson with the same id.

Mark done homework with /done command. Only you will see the mark.

Syntax breakdown:

<pre>
/done n 2 4

  ↑   ↑ ↑ ↑
  C   W D L
  M   E A E
  D   E Y S
      K   №
</pre>


Add notes with /an command. Syntax breakdown:

<pre>
/an 5 2 4 [1] We're no strangers to love
You know the rules and so do I (do I)
A full commitment's what I'm thinking of
You wouldn't get this from any other guy

 ↑  ↑ ↑ ↑  ↑       ↑
 C  W D L  L       N
 M  E A E  V       T
 D  E Y S  L
    K   №
</pre>

[IN DEVELOPMENT:] You can upload an image with this command. To prevent abuse, you are limited to 120 uploads per hour."""), parse_mode = 'HTML')

        await update.message.reply_text("""Move lessons with /mv command.

Syntax breakdown:
<pre>
/mv c 2 3 c 2 1

 ↑  ↑ ↑ ↑ ↑ ↑ ↑
 C  W D L W D L
 M  E A E E A E
 D  E Y S E Y S
    K   № K   №
   └────┘└─────┘
    from   to
</pre>

It also moves homework and notes that are on selected point (so not the ones that are on succeding weeks). This might change in the future.
                                        

To set information of lesson start/end, use /set_temporal command.

In the following example text after "#"s (up to new line) is for explanation, don't include it to your command.
Syntax example:

<pre>/set_temporal
08:20 09:55  # start and end of the first lesson
10:05 11:40  # start and end of second one
12:20 13:55  # and so on
14:05 15:40
15:50 17:25
17:35 19:10
00:00 00:00
00:00 00:00  # this block is universal time
00:00 00:00  # if you will need to make another timetable for a specific day
00:00 00:00  # write "00:00 00:00" until you'll reach 10 lessons

01:01 01:02  # this is time specific for monday
01:03 01:04  # you may limit yourself to the first block
01:05 01:06  # if lessons start and end at the same time every single day.
01:07 01:08
01:09 01:10
01:11 01:12
00:00 00:00
00:00 00:00
00:00 00:00
00:00 00:00  # if not, go on until the end of the week.

02:01 02:02  # tuesday
02:03 02:04
...
</pre>

Time must always be in hh:mm format, 5 symbols always. "9:30" is invalid, "09:30" is valid.


<pre>────────────────────────────</pre>

If this line is of 2 lines, try lowering your font size, or the table will not be displayed correctly.

If you will ever need more than 6 lessons, or if a table is not displayed correctly and you don't want to change your font settings, you can toggle semigraphic mode on/off with /tg_sg command. Tables will not look this nice, but will be more reliable. If you'll ever need to use 8 or more lessons, don't hesitate to write me, if someone will need it, I will make the feature.


If you will have any questions or suggestions, please, contact me: @carbon_starlight""", parse_mode = "HTML")


async def getValidInviteCodes(for_table):
    valid_invite_codes = []
    with open('mainArray.json', 'r') as fileMA:
        for subarray in json.load(fileMA):
            if subarray[3] == 'ic' and subarray[10] == 0 and subarray[4] == for_table:
                valid_invite_codes.append(subarray[8])
    return valid_invite_codes


async def lg_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.message.chat.id
    text = update.message.text
    await getUserInfo(update.message.chat.id, update.message.chat.username)
    words = text.split()
    if len(words) < 2:
        await update.message.reply_text(f"""You are administrator in {tables_user_admin_in}

You may make edits in {tables_user_allowed_in}

Current table: {table_user_in}

Type table ID after the command, separated with a space to log in.""")
        return
    valid_invite_codes = await getValidInviteCodes(words[1])
    if words[1] in tables_user_admin_in or words[1] in tables_user_allowed_in or (len(words) > 2 and words[2] in valid_invite_codes):
        new_data = [0, time.time(), update.message.chat.id, 'lg', words[1], 0, 0, 0, 0, utz, 0, 0, 0, 0, 0,]
        
        with open('mainArray.json', 'r') as fileMA:
            mainArray = json.load(fileMA)

        # Now append the new_data to your data
        mainArray.append(new_data)

        # Now write the data back to the fileMA
        with open('mainArray.json', 'w') as fileMA:
            json.dump(mainArray, fileMA)

        with open('lg_logs.txt', 'a') as f:
            f.write(f'{datetime.now()}: User {update.message.chat.id} {update.message.chat.username} logged in to table {words[1]}\n') 

        await update.message.reply_text(f'Logged in successfully')
    else:
        await update.message.reply_text(f'User not allowed or table does not exist')


async def al_command(update: Update, context: ContextTypes.DEFAULT_TYPE, overwrite_update_message=None):
    """Add lesson command"""
    user_id = update.message.chat.id
    await getUserInfo(update.message.chat.id)
    await getCurrentTemporalInfo()
    # await getToLesFromCurrent()
    try:
        if overwrite_update_message is not None:
            text = overwrite_update_message
        else:
            # access the text in the message object(member inside update)
            text = update.message.text
        # split the text into words
        words = text.split()
        # print(text)

        # check if the command is formed correctly
        if len(words) < 5 or len(words) > 8:
            raise ValueError("""ERROR 399: INVALID COMMAND

Correct syntax:
<pre>
/al 5 2 4 [1] [1] АнгФ [A420]

 ↑  ↑ ↑ ↑  ↑   ↑   ↑     ↑
 C  W D L  L   E   L     C 
 M  E A E  V   X   E     A
 D  E Y S  L       S     B
    K   №          |
                   I
                   D
</pre>""")

        room_number = 0

        command = words[0]  # '/al'
        week_number = words[1]
        day_of_week = int(words[2])
        lesson_number = int(words[3])
        if week_number == 'c':
            week_number = current_week_utz
        elif week_number == 'n':
            week_number = current_week_utz + 1
        else:
            week_number = int(week_number)
        if len(words) == 5:  # /al 1 2 3 les
            subgroup_level = 1  # default value
            exclusiveness = 1
            lesson_id = words[4]
        elif len(words) == 6:  # /al 1 2 3 les 006
            subgroup_level = 1  # default value
            exclusiveness = 1
            lesson_id = words[4]
            room_number = words[5]
        elif len(words) == 7:  # /al 1 2 3 1 1 les
            subgroup_level = int(words[4])
            exclusiveness = int(words[5])
            lesson_id = words[6]
        else:  # /al 1 2 3 1 1 les 006 || len == 8
            subgroup_level = int(words[4])
            exclusiveness = int(words[5])
            lesson_id = words[6]
            room_number = words[7]

            # vars
    #        /al 1 2 3 les
    #        /al 1 2 3 les 006
    #        /al 1 2 3 1   1   les
    #        /al 1 2 3 1   1   les 006
    #   ind   0  1 2 3 4   5    6   7
    #   len   1  2 3 4 5   6    7   8


        if len(lesson_id) > 12:
            raise ValueError("ERROR 1102: INVALID ID\n\nThe length of the ID must be less than 12 symbols.")
        
        if lesson_id.isdigit():
            raise ValueError("ERROR 1105: INVALID ID\n\nThe ID must not be a number.")
        
        if lesson_id == '\\empty':
            lesson_id = None

        if room_number == '\\empty':
            room_number = None

            # The additional subarray
        new_data = [0, time.time(), update.message.chat.id, 'al', table_user_in, week_number, day_of_week, lesson_number, lesson_id, utz, 0, subgroup_level, exclusiveness, room_number, 0,]

        #await log(new_data)

        # First, load the data already in the fileMA
        with open('mainArray.json', 'r') as fileMA:
            mainArray = json.load(fileMA)

        # Now append the new_data to your data
        mainArray.append(new_data)

        # Now write the data back to the fileMA
        with open('mainArray.json', 'w') as fileMA:
            json.dump(mainArray, fileMA)


        if  update.message.from_user.language_code == 'ru':
            await update.message.reply_text(f'Добавление урока {lesson_id} {"как части регулярного расписания" if exclusiveness == 1 else "как единовременное исключение"} к неделе {int(week_number)}, день {day_of_week}, номер {lesson_number} для регистра {subgroup_level} к таблице {table_user_in}. Номер кабинета: {room_number}')
        else:
            await update.message.reply_text(f'Adding lesson {lesson_id} {"as part of the regular schedule" if exclusiveness == 1 else "as an exception"} to week {int(week_number)}, day {day_of_week}, lesson number {lesson_number} for register {subgroup_level} to {table_user_in} table. Room number: {room_number}')

        await save_data_for_interchange(table_user_in)
    
    except ValueError as e:
        # if anything goes wrong, tell the user
        await update.message.reply_text("<pre>" + str(e) + "</pre>", parse_mode = 'HTML')



async def ah_command(update: Update, context: ContextTypes.DEFAULT_TYPE, overwrite_update_message=None):
    print('EXECUTING AH COMMAND')
    start_ac_timestamp = time.time()
    user_id = update.message.chat.id
    await getCurrentTemporalInfo()
    await getUserInfo(user_id)
    if overwrite_update_message is not None:
        text = overwrite_update_message
    else:
        text = update.message.text
    words = text.split()
    # print(len(words))

    if len(words) == 1:
        await update.message.reply_text("""<pre>ERR1777: INVALID COMMAND

Correct syntax:

/ah 5 2 4 [1] p46 t32 tb Utane

 ↑  ↑ ↑ ↑  ↑         ↑
 C  W D L  L         H
 M  E A E  V         W
 D  E Y S  L
    K   №</pre>""", parse_mode = 'HTML')

    if isinteger(words[1]) or (words[1] == 'c') or (words[1] == 'n'): 
        try:
            # print('1205818478')
            # access the text in the message object(member inside update)
            # split the text into words
            words = text.split()

            # check if the command is formed correctly
            if len(words) < 5:
                raise ValueError("ERR453: INVALID COMMAND")

            command = words[0]  #
            week_number = words[1]
            day_of_week = int(words[2])
            lesson_number = int(words[3])
            if week_number == 'c':
                week_number = current_week_utz
            elif week_number == 'n':
                week_number = current_week_utz + 1
            else:
                week_number = int(week_number)

            if isinteger(words[4]):
                subgroup_level = int(words[4])
            else:
                subgroup_level = 1  # default value

            split_command = text.split(" ")
            hw = " ".join(split_command[4:])
    
            # print('hw:',hw)

            new_data = [0, time.time(), update.message.chat.id, 'ah', table_user_in, week_number, day_of_week, lesson_number, hw, utz, 0, subgroup_level, 0, 0, 0, 0,]
            await log(new_data)

            if update.message.from_user.language_code == 'ru':
                await update.message.reply_text(f'Добавление домашнего задания "{hw}" к неделе {int(week_number)}, день {day_of_week}, номер {lesson_number} для регистра {subgroup_level}')
            else:
                await update.message.reply_text(f'Adding homework "{hw}" to week {int(week_number)}, day {day_of_week}, lesson number {lesson_number} for register {subgroup_level}')
            await save_data_for_interchange(table_user_in)
            
        except ValueError as e:
            # if anything goes wrong, tell the user
            await update.message.reply_text("<pre>" + str(e) + "</pre>", parse_mode = 'HTML')
    else:
        next_of_kind_lesson_week, next_of_kind_lesson_day_in_week, next_of_kind_lesson_in_day, current_lesson = await getToLesFromCurrent(update.message.chat.id)
        split_command = text.split(" ")
        hw = " ".join(split_command[1:])
        new_data = [0, time.time(), update.message.chat.id, 'ah', table_user_in, next_of_kind_lesson_week, next_of_kind_lesson_day_in_week, next_of_kind_lesson_in_day, hw, utz, 0, 1, 0, 0, 0,]
        await log(new_data)

        # Now, you should connect to your database and add these values
        # please replace this with your actual db operation
        # db_operation(week_num, day_of_week, lesson_num, subgroup_level, lesson_id)

        await update.message.reply_text(f'Adding hw in auto mode for {hw}, to week {next_of_kind_lesson_week}, day {next_of_kind_lesson_day_in_week}, lesson number {next_of_kind_lesson_in_day} for register 1')
        await save_data_for_interchange(table_user_in)
        print('END OF AH COMMAND EXECUTION IN ', time.time() - start_ac_timestamp)


async def an_command(update: Update, context: ContextTypes.DEFAULT_TYPE, overwrite_update_message = None):
    """Add notes command"""
    user_id = update.message.chat.id
    if overwrite_update_message is not None:
        text = overwrite_update_message
    else:
        text = update.message.text
    words = text.split()

    if len(words) == 1:
        await update.message.reply_text("""<pre>ERR506: INVALID COMMAND
        
Correct syntax:

/an 5 2 4 [1] Aoi kaze ga ima mune no doa wo tataitemo,
Watashi dake wo tada mitsumete
Hohoenderu Anata
Sotto Fureru mono

 ↑  ↑ ↑ ↑  ↑       ↑
 C  W D L  L       N
 M  E A E  V       T
 D  E Y S  L
    K   №
</pre>""", parse_mode = 'HTML')

    if isinteger(words[1]) or (words[1] == 'c') or (words[1] == 'n'): 
        try:
            await getUserInfo(user_id)
            await getCurrentTemporalInfo()
            # access the text in the message object(member inside update)
            # split the text into words
            words = text.split()

            # check if the command is formed correctly
            if len(words) < 5:
                raise ValueError("ERR506: INVALID COMMAND")

            command = words[0]
            week_number = words[1]
            day_of_week = int(words[2])
            lesson_number = int(words[3])
            if week_number == 'c':
                week_number = current_week_utz
            elif week_number == 'n':
                week_number = current_week_utz + 1
            else:
                week_number = int(week_number)

            if isinteger(words[4]):
                subgroup_level = int(words[4])
            else:
                subgroup_level = 1  # default value

            split_command = text.split(" ")
            n = " ".join(split_command[4:])
    
            new_data = [0, time.time(), update.message.chat.id, 'an', table_user_in, week_number, day_of_week, lesson_number, n, utz, 0, subgroup_level, 0, 0, 0, 0,]
            await log(new_data)

            if update.message.from_user.language_code == 'ru':
                await update.message.reply_text(f'Добавление заметок/конспекта к неделе {int(week_number)}, день {day_of_week}, номер урока {lesson_number} для регистра {subgroup_level}')
            else:
                await update.message.reply_text(f'Adding notes to week {int(week_number)}, day {day_of_week}, lesson number {lesson_number} for register {subgroup_level}')
            await save_data_for_interchange(table_user_in)


        except ValueError as e:
            if traceback_mode_is_rich:
                # With rich's traceback:
                print(str(e))
            else:
            # With standard traceback:
                # Get the line number of the last executed line
                _, _, tb = sys.exc_info()
                line_number = traceback.extract_tb(tb)[-1][1]

                # Create the error message including the line number
                error_message = f"Error occurred on line {line_number}: {str(e)}"

                # Print or display the error message
                print(error_message)
                await update.message.reply_text(error_message)
    else:
        next_of_kind_lesson_week, next_of_kind_lesson_day_in_week, next_of_kind_lesson_in_day, current_lesson = await getToLesFromCurrent(update.message.chat.id)
        split_command = text.split(" ")
        n = " ".join(split_command[1:])

        new_data = [0, time.time(), update.message.chat.id, 'an', table_user_in, current_week_utz, current_day_utz, current_lesson, n, utz, 0, 1, 0, 0, 0,]
        await log(new_data)

        await update.message.reply_text(f'Adding notes in auto mode to week {current_week_utz}, day {current_day_utz}, lesson number {current_lesson} for register 1 (your table)')


async def mv_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """move lesson with homework and notes to another place"""
    """/mv c 2 3 c 3 4"""
    """ c  w d l w d l"""
    """ 0  1 2 3 4 5 6"""
    print("EXECUTING MV_COMMAND")
    start_mc_timestamp = time.time()
    await getUserInfo(update.message.chat.id)
    # print(utz)
    await getCurrentTemporalInfo()
    # print('cool')
    # print(current_week_utz)

    text = update.message.text
    words = text.split()
    # print(words)
    if words[1] == 'c':
        words[1] = current_week_utz
    if words[1] == 'n':
        words[1] = current_week_utz + 1
    if words[4] == 'c':
        words[4] = current_week_utz
    if words[4] == 'n':
        words[4] = current_week_utz + 1

    # print(words)

    getWeekArray(table_user_in, words[1])

    with open('mainArray.json', 'r') as fileMA:
        mainArray = json.load(fileMA)
    # print(words[1:7])

    words[1:6] = [int(word) for word in words[1:6]]

    for subarray in reversed(mainArray):
        if (
        # subarray[5] == words[1]  # week
        # subarray[6] == words[2]  # day
        subarray[7] == words[3]  # lesson
        ):
            print('point 1')
        else:
            print('Debug:', type(subarray[7]), type(words[3]))


    async def get_weekArray_index(w: int, d: int, l: int):
        index = 0 + (d - 1)*10 + (l - 1)
        return index

    for subarray in reversed(mainArray):
        if (
        subarray[5] == words[1]  # week
        and subarray[6] == words[2]  # day
        and subarray[7] == words[3]  # lesson
        and subarray[4] == table_user_in
        and subarray[10] == 0
        and subarray[3] == 'al'
        ):
            # print('found les')
            new_data = [subarray[0], time.time(), update.message.chat.id, 'al', table_user_in, words[4], words[5], int(words[6]), subarray[8], subarray[9], subarray[10], subarray[11], subarray[12], subarray[13], subarray[14]]
            await log(new_data)
            # print(new_data)
            new_data = [subarray[0], time.time(), update.message.chat.id, 'al', table_user_in, subarray[5], subarray[6], subarray[7], None, subarray[9], subarray[10], subarray[11], subarray[12], None, subarray[14]]
            await log(new_data)
            # print(new_data)
            break
            
    for subarray in mainArray:
        if (
        subarray[5] == words[1]
        and subarray[6] == words[2]
        and subarray[7] == words[3]
        and subarray[4] == table_user_in
        and subarray[10] == 0
        and subarray[3] == 'ah'
        ):
            new_data = [subarray[0], time.time(), update.message.chat.id, 'ah', table_user_in, words[4], words[5], int(words[6]), subarray[8], subarray[9], subarray[10], subarray[11], subarray[12], subarray[13], subarray[14]]
            await log(new_data)
            new_data = [subarray[0], time.time(), update.message.chat.id, 'ah', table_user_in, subarray[5], subarray[6], subarray[7], '\empty', subarray[9], subarray[10], subarray[11], subarray[12], 0, subarray[14]]
            await log(new_data)
            break

    for subarray in mainArray:
        if (
        subarray[5] == words[1]
        and subarray[6] == words[2]
        and subarray[7] == words[3]
        and subarray[4] == table_user_in
        and subarray[10] == 0
        and subarray[3] == 'an'
        ):
            new_data = [subarray[0], time.time(), update.message.chat.id, 'an', table_user_in, words[4], words[5], int(words[6]), subarray[8], subarray[9], subarray[10], subarray[11], subarray[12], subarray[13], subarray[14]]
            await log(new_data)
            new_data = [subarray[0], time.time(), update.message.chat.id, 'an', table_user_in, subarray[5], subarray[6], subarray[7], '\empty', subarray[9], subarray[10], subarray[11], subarray[12], 0, subarray[14]]
            await log(new_data)
            try: print('sARRAY IN Q' + str(new_data))
            finally: pass
            
            #              res0     |   time    |      contrib_id        | type  |   table   |     w    |      d   |      l      |   cntnt   |   utz      |     vl       |          rg|          ex|         rn   |        r6
            #              res0     |   time    |      contrib_id        | type  |   table   |     w      |      d     |      l     | cntnt |  utz      |     vl|          rg|          ex|         rn|        r6
    
            break
    
    await update.message.reply_text(f"Lesson {words[3]} of week {words[1]} day {words[2]} moved to week {words[4]}, day {words[5]} lesson {words[6]} with notes and homework")

    print ("END OF MV_COMMAND EXECUTION IN ", time.time() - start_mc_timestamp)
            
    
  #res0|   time    |contrib_id| type  |table| w |d |l |cntnt|utz |vl|rg|ex|rn|r6
  # [0, 1689546503, 5725753364, 'cs', '1-HAL', 0, 0, 0, 't', utz, 0, 0, 0, 0, 0],
#]
#    0      1            2        3      4     5  6  7   8    9   10 11 12 13 14```







# Each category corresponds to a specific menu step
# Define conversation states
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes, ConversationHandler

# Constants for states
TYPE, WEEK, DAY, LESSON_NUMBER, EVENT_TYPE_IF_REGULAR, ADD_FOR, CONTENT, ROOM = range(8)

# Command handler functions
async def add_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    print("func add_command")
    if update.message.from_user.language_code == 'ru':
        reply_keyboard = [['‎Урок / Лекцию'], ['‎‎Домашнее задание'], ['‎‎‎Пометить Д/З как завершённое'], ['‎‎‎‎Конспект']]
    else:
        reply_keyboard = [['‎Lesson'], ['‎‎Homework'], ['‎‎‎Homework mark'], ['‎‎‎‎Note']]
    
    if update.message.from_user.language_code == 'ru':
        msg = "Что вы хотите добавить?"
    else:
        msg = "What would you like to add?"
    
    await update.message.reply_text(
        msg,
        reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)
    )
    return TYPE

async def type_sel(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    print("func type_sel")
    print("adding to context.user_data['type']:", update.message.text)
    context.user_data['type'] = update.message.text

    # reply_keyboard = [['‎Current', '‎‎Next', '‎‎‎Other']]
    if update.message.from_user.language_code == 'ru':
        reply_keyboard = [['‎Текущий', '‎‎Следующий']]
    else:
        reply_keyboard = [['‎Current', '‎‎Next']]

    if update.message.from_user.language_code == 'ru':
        msg = "В какую неделю добавить?"
    else:
        msg = "Please, specify the week"

    await update.message.reply_text(
        'Please, specify the week',
        reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)
    )
    return WEEK

async def week_sel(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    print("func week_sel")
    context.user_data['week'] = update.message.text

    # TODO: Localization ↓
    # if update.message.text != '‎‎‎Other':
    if len(update.message.text) - len(update.message.text.lstrip('\u200E')) != 3:
        
        if update.message.from_user.language_code == 'ru':
            reply_keyboard = [
                ['‎Понедельник'], 
                ['‎‎Вторник'], 
                ['‎‎‎Среда'], 
                ['‎‎‎‎Четверг'], 
                ['‎‎‎‎‎Пятница'], 
                ['‎‎‎‎‎‎Суббота'], 
                ['‎‎‎‎‎‎‎Воскресенье']
            ]
        else:
            reply_keyboard = [
                ['‎Monday'], 
                ['‎‎Tuesday'], 
                ['‎‎‎Wednesday'], 
                ['‎‎‎‎Thursday'], 
                ['‎‎‎‎‎Friday'], 
                ['‎‎‎‎‎‎Saturday'], 
                ['‎‎‎‎‎‎‎Sunday']
            ]

        if update.message.from_user.language_code == 'ru':
            msg = "Укажите день недели"
        else:
            msg = "Please, specify the date"

        await update.message.reply_text(
            'Specify the date',
            reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)
        )
        return DAY
    else:
        print('\033[91mERROR: Week "Other" (digit code 3) is not supported yet\033[0m')
        return ConversationHandler.END

# async def specific_date_selection(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
#     context.user_data['specific_date'] = update.message.text
#     return await lesson_number_selection(update, context)

async def day_sel(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    print("func day_sel")
    context.user_data['day'] = update.message.text
    # reply_keyboard = [[str(x) for x in range(1, 5)], [str(x) for x in range(5, 9)], ['Cancel']]
    reply_keyboard = [[str(x) for x in range(1, 5)], [str(x) for x in range(5, 9)]]
    
    if update.message.from_user.language_code == 'ru':
        msg = "Номер урока?"
    else:
        msg = "What is the lesson number?"

    await update.message.reply_text(
        msg,
        reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)
    )
    # print(2343)
    return LESSON_NUMBER

async def lesson_number_sel(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    # print("010")
    print("func lesson_number_sel")
    context.user_data['lesson_number'] = update.message.text
    print(2455)

    if context.user_data['lesson_number'] == 'Cancel':
        await cancel_add_conv(update, context)
        print(2459)
        return ConversationHandler.END
    
    print('context.user_data["type"]:', context.user_data['type'])
    print('context.user_data["week"]:', context.user_data['week'])
    print(len(context.user_data['type']) - len(context.user_data['type'].lstrip('\u200E')))
    if len(context.user_data['type']) - len(context.user_data['type'].lstrip('\u200E')) == 1:
        # if a lesson is being added
        if update.message.from_user.language_code == 'ru':
            msg = "Добавить как единовременное событие или регулярное?"
        else:
            msg = "Would you like to add it as a one-time event or as a regular one?"
        if update.message.from_user.language_code == 'ru':
            reply_keyboard = [['‎Единовременное', '‎‎Регулярное']]
        else:
            reply_keyboard = [['‎One-time', '‎‎Regular']]
        
        print(2472)
        await update.message.reply_text(
            msg,
            reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)
        )

        return EVENT_TYPE_IF_REGULAR
    
    print(2478)
    return await if_one_time_event_or_regular_sel(update, context)

# async def event_type_selection(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
#     context.user_data['event_type_if_regular'] = update.message.text
#     return await if_one_time_event_or_regular_sel(update, context)

async def if_one_time_event_or_regular_sel(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    print("func if_one_time_event_or_regular_sel")
    if len(context.user_data['type']) - len(context.user_data['type'].lstrip('\u200E')) == 1:
    # if a lesson is being added
        context.user_data['event_type_if_regular'] = update.message.text
    else:
        context.user_data['event_type_if_regular'] = None
    # if context.user_data['type'] = '‎Lesson':

    print(2509)

    if update.message.from_user.language_code == 'ru':
        # reply_keyboard = [['‎Для себя', '‎‎Для онлайн-расписания', '‎‎‎Для всех расписаний, указанных как связанные с этим']]
        reply_keyboard = [['‎Для себя', '‎‎Для онлайн-расписания']]
    else:
        # reply_keyboard = [['‎For yourself', '‎‎For the schedule of your class', '‎‎‎For all the schedules that are connected']]
        reply_keyboard = [['‎For yourself', '‎‎For the schedule of your class']]

    if update.message.from_user.language_code == 'ru':
        msg = "Добавить…"
    else:
        msg = "Would you like to add it:"

    await update.message.reply_text(
        msg,
        reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)
    )
    return ADD_FOR

async def add_for(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    print("func add_for")
    context.user_data['add_for'] = update.message.text
    print(update.message.text)

    if count_lrm_symbols(str(context.user_data['type'])) == 3:
        # if mark as done
        reply_keyboard = ['✓']
        if update.message.from_user.language_code == 'ru':
            msg = "Выберете стиль пометки"
        else:
            msg = "Select the style of the mark"
            
        await update.message.reply_text(
            msg,
            reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)
        )
    else:

        if count_lrm_symbols(str(context.user_data['type'])) == 1:
            # if a lesson is being added
            if update.message.from_user.language_code == 'ru':
                msg = "Введите название урока"
            else:
                msg = "Specify the name of the lesson"
        if count_lrm_symbols(str(context.user_data['type'])) == 2 or count_lrm_symbols(str(context.user_data['type'])) == 4:
            # if a hw or a note is being added
            if update.message.from_user.language_code == 'ru':
                msg = "Введите текст"
            else:
                msg = "Enter the text"
        await update.message.reply_text(
            msg
        )

    return CONTENT

async def content_input(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    print("func content_input")
    context.user_data['content'] = update.message.text
    # await update.message.reply_text(f"Data collected: {context.user_data}")
    if count_lrm_symbols(str(context.user_data['type'])) == 1:
        if update.message.from_user.language_code == 'ru':
            msg = "Введите номер аудитории"
        else:
            msg = "Enter the room number"
        await update.message.reply_text(msg)
        return ROOM
    else:
        context.user_data['room'] = None
        return await room_input(update, context)


async def room_input (update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    print("func room_input")
    if count_lrm_symbols(str(context.user_data['type'])) == 1:
        context.user_data['room'] = update.message.text
    else:
        context.user_data['room'] = None

    # if len(str(context.user_data['type'])) - len((context.user_data['type']).lstrip('\u200E')) == 1:
    if count_lrm_symbols(str(context.user_data['type'])) == 1:
        # if a lesson is being added
        command_type = f"/al"
    elif count_lrm_symbols(str(context.user_data['type'])) == 2:
        # if a hw is being added
        command_type = f"/ah"
    elif count_lrm_symbols(str(context.user_data['type'])) == 3:
        # if a hw mark is being added
        command_type = f"/done"
    elif count_lrm_symbols(str(context.user_data['type'])) == 4:
        # if a note is being added
        command_type = f"/an"
    else:
        console.log('\033[91mERROR: This LRM code is not supported\033[0m')
    console.log(count_lrm_symbols(str(context.user_data['type'])))


    if count_lrm_symbols(str(context.user_data['week'])) == 1:
        # if a current week is being selected
        week = "c"
    elif count_lrm_symbols(str(context.user_data['week'])) == 2:
        # if a next week is being selected
        week = "n"
    elif count_lrm_symbols(str(context.user_data['week'])) == 3:
        # if a other week is being selected
        print('\033[91mERROR: Week "Other" (digit code 3) is not supported yet\033[0m')
    else:
        console.log('\033[91mERROR: This LRM code is not supported\033[0m')
    console.log(count_lrm_symbols(str(context.user_data['week'])))

    day = count_lrm_symbols(str(context.user_data['day']))
    console.log(count_lrm_symbols(str(context.user_data['day'])))

    lesson = context.user_data['lesson_number']

    if count_lrm_symbols(str(context.user_data['event_type_if_regular'])) == 1:
        exclusivity = 0
    elif count_lrm_symbols(str(context.user_data['event_type_if_regular'])) == 2:
        exclusivity = 1
    else:
        console.log('\033[91mERROR: This LRM code is not supported\033[0m')
    console.log(count_lrm_symbols(str(context.user_data['event_type_if_regular'])))

    if count_lrm_symbols(str(context.user_data['add_for'])) == 1:
        # if a for yourself is being selected
        add_for = 0
    elif count_lrm_symbols(str(context.user_data['add_for'])) == 2:
        # if a for the schedule of your class is being selected
        add_for = 1
    elif count_lrm_symbols(str(context.user_data['add_for'])) == 3:
        # if a for all the schedules that are connected is being selected
        add_for = 2
    else:
        console.log(count_lrm_symbols(str(context.user_data['add_for'])))
        console.log('context.user_data["add_for"]:', context.user_data['add_for'])
        console.log('\033[91mERROR: This LRM code is not supported\033[0m')
    console.log(count_lrm_symbols(str(context.user_data['add_for'])))

    content = context.user_data['content']

    room = context.user_data['room']

    command = f"{command_type} {week} {day} {lesson} {add_for} {exclusivity if command_type == '/al' else ''} {content} {room if command_type == '/al' else ''}"

    print(command)

    await update.message.reply_text(command)

    if command_type == "/al":
        await al_command(update, context, overwrite_update_message=command)
    elif command_type == "/ah":
        await ah_command(update, context, overwrite_update_message=command)
    elif command_type == "/done":
        await done_command(update, context, overwrite_update_message=command)
    elif command_type == "/an":
        await an_command(update, context, overwrite_update_message=command)
    else:
        console.log('\033[91mERROR: This LRM code is not supported\033[0m')

    with open('command_logs.txt', 'a') as f:
        f.write(command + " via /add " + 'by ' + str(update.message.chat.id) + str(time.time()) + '\n')

    return ConversationHandler.END

async def cancel_add_conv(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    print("func cancel_add_conv")
    await update.message.reply_text('Operation cancelled.')
    return ConversationHandler.END



def count_lrm_symbols(string):
    count = 0
    for char in string:
        if char == '\u200e' or char == '\u200c':
            # U+200E sometimes turn into U+200C for some reason
            count += 1
        else:
            break
    return count




async def ls_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """list week lessons and hw: *** /ls 4 *** is getting 4th week; default is current"""
    global adding_from_week
    print('EXECUTING LS_COMMAND')
    start_ls_timestamp = time.time()
    user_id = update.message.chat.id
    await getUserInfo(update.message.chat.id)
    await getCurrentTemporalInfo()
    # print('In ls_command: tables_user_admin_in: ' + str(tables_user_admin_in))
    # print('In ls_command: tables_user_allowed_in: ' + str(tables_user_allowed_in))
    # print('In ls_command: table_user_in: ' + str(table_user_in))
    with open('mainArray.json', 'r') as fileMA:
        mainArray = json.load(fileMA)
    text = update.message.text
    words = text.split()
    await getCurrentTemporalInfo()
    # print('In ls_command: words: ' + str(words))

    if len(words) == 1:
        adding_from_week = current_week_utz
        # print('executing if, len(words) == 1')
    else:
        if words[1] != 'n' and words[1] != 'c' and words[1] != 'N' and words[1] != 'C':
            adding_from_week = int(words[1])
        elif words[1] == 'n' or words[1] == 'N':
            adding_from_week = current_week_utz + 1
        elif words[1] == 'c' or words[1] == 'C':
            adding_from_week = current_week_utz
        # print('words[1]: ' + words[1])
        # print('adding_from_week: ' + str(adding_from_week))
        # print('добрались до else')
    
    await getWeekArray(table_user_in, adding_from_week)
    await get_room_number_weekArray(table_user_in, adding_from_week)

    # print('In ls_command: adding_from_week: ' + str(adding_from_week))
    # print('In ls_command: room_number_weekArray: ' + str(room_number_weekArray))
    # print('In ls_command: ' + str(room_number_weekArray[0]))
    # print('In ls_command: ' + str(weekArray))

    if weekArray and semigraphic_mode_on == False:
        await update.message.reply_text(f"""WEEK {int(adding_from_week)}
Current week (UTC): {current_week_utc}
Current week (UTZ): {current_week_utz}
Time zone {utz}

fileMA: {fileMA}

You are administrator in {tables_user_admin_in}

You may make edits in {tables_user_allowed_in}

Table: {table_user_in}

MONDAY:
1: {weekArray[0]} {"[" + room_number_weekArray[0] + "]" if room_number_weekArray[0] else ''}
2: {weekArray[1]} {"[" + room_number_weekArray[1] + "]" if room_number_weekArray[1] else ''}
3: {weekArray[2]} {"[" + room_number_weekArray[2] + "]" if room_number_weekArray[2] else ''}
4: {weekArray[3]} {"[" + room_number_weekArray[3] + "]" if room_number_weekArray[3] else ''}
5: {weekArray[4]} {"[" + room_number_weekArray[4] + "]" if room_number_weekArray[4] else ''}
6: {weekArray[5]} {"[" + room_number_weekArray[5] + "]" if room_number_weekArray[5] else ''}
7: {weekArray[6]} {"[" + room_number_weekArray[6] + "]" if room_number_weekArray[6] else ''}
8: {weekArray[7]} {"[" + room_number_weekArray[7] + "]" if room_number_weekArray[7] else ''}

TUESDAY:
1: {weekArray[10]} {"[" + room_number_weekArray[10] + "]" if room_number_weekArray[10] else ''}
2: {weekArray[11]} {"[" + room_number_weekArray[11] + "]" if room_number_weekArray[11] else ''}
3: {weekArray[12]} {"[" + room_number_weekArray[12] + "]" if room_number_weekArray[12] else ''}
4: {weekArray[13]} {"[" + room_number_weekArray[13] + "]" if room_number_weekArray[13] else ''}
5: {weekArray[14]} {"[" + room_number_weekArray[14] + "]" if room_number_weekArray[14] else ''} 
6: {weekArray[15]} {"[" + room_number_weekArray[15] + "]" if room_number_weekArray[15] else ''} 
7: {weekArray[16]} {"[" + room_number_weekArray[16] + "]" if room_number_weekArray[16] else ''}
8: {weekArray[17]} {"[" + room_number_weekArray[17] + "]" if room_number_weekArray[17] else ''}

WEDNESDAY:
1: {weekArray[20]} {"[" + room_number_weekArray[20] + "]" if room_number_weekArray[20] else ''}
2: {weekArray[21]} {"[" + room_number_weekArray[21] + "]" if room_number_weekArray[21] else ''}
3: {weekArray[22]} {"[" + room_number_weekArray[22] + "]" if room_number_weekArray[22] else ''}
4: {weekArray[23]} {"[" + room_number_weekArray[23] + "]" if room_number_weekArray[23] else ''}
5: {weekArray[24]} {"[" + room_number_weekArray[24] + "]" if room_number_weekArray[24] else ''}
6: {weekArray[25]} {"[" + room_number_weekArray[25] + "]" if room_number_weekArray[25] else ''}
7: {weekArray[26]} {"[" + room_number_weekArray[26] + "]" if room_number_weekArray[26] else ''}
8: {weekArray[27]} {"[" + room_number_weekArray[27] + "]" if room_number_weekArray[27] else ''}

THURSDAY:
1: {weekArray[30]} {"[" + room_number_weekArray[30] + "]" if room_number_weekArray[30] else ''}
2: {weekArray[31]} {"[" + room_number_weekArray[31] + "]" if room_number_weekArray[31] else ''}
3: {weekArray[32]} {"[" + room_number_weekArray[32] + "]" if room_number_weekArray[32] else ''}
4: {weekArray[33]} {"[" + room_number_weekArray[33] + "]" if room_number_weekArray[33] else ''}
5: {weekArray[34]} {"[" + room_number_weekArray[34] + "]" if room_number_weekArray[34] else ''}
6: {weekArray[35]} {"[" + room_number_weekArray[35] + "]" if room_number_weekArray[35] else ''}
7: {weekArray[36]} {"[" + room_number_weekArray[36] + "]" if room_number_weekArray[36] else ''}  
8: {weekArray[37]} {"[" + room_number_weekArray[37] + "]" if room_number_weekArray[37] else ''}

FRIDAY:
1: {weekArray[40]} {"[" + room_number_weekArray[40] + "]" if room_number_weekArray[40] else ''}
2: {weekArray[41]} {"[" + room_number_weekArray[41] + "]" if room_number_weekArray[41] else ''}
3: {weekArray[42]} {"[" + room_number_weekArray[42] + "]" if room_number_weekArray[42] else ''}
4: {weekArray[43]} {"[" + room_number_weekArray[43] + "]" if room_number_weekArray[43] else ''}
5: {weekArray[44]} {"[" + room_number_weekArray[44] + "]" if room_number_weekArray[44] else ''}
6: {weekArray[45]} {"[" + room_number_weekArray[45] + "]" if room_number_weekArray[45] else ''}
7: {weekArray[46]} {"[" + room_number_weekArray[46] + "]" if room_number_weekArray[46] else ''}
8: {weekArray[47]} {"[" + room_number_weekArray[47] + "]" if room_number_weekArray[47] else ''}

SATURDAY:
1: {weekArray[50]} {"[" + room_number_weekArray[50] + "]" if room_number_weekArray[50] else ''}
2: {weekArray[51]} {"[" + room_number_weekArray[51] + "]" if room_number_weekArray[51] else ''}
3: {weekArray[52]} {"[" + room_number_weekArray[52] + "]" if room_number_weekArray[52] else ''} 
4: {weekArray[53]} {"[" + room_number_weekArray[53] + "]" if room_number_weekArray[53] else ''}
5: {weekArray[54]} {"[" + room_number_weekArray[54] + "]" if room_number_weekArray[54] else ''}
6: {weekArray[55]} {"[" + room_number_weekArray[55] + "]" if room_number_weekArray[55] else ''}
7: {weekArray[56]} {"[" + room_number_weekArray[56] + "]" if room_number_weekArray[56] else ''}
8: {weekArray[57]} {"[" + room_number_weekArray[57] + "]" if room_number_weekArray[57] else ''}

SUNDAY:
1: {weekArray[60]} {"[" + room_number_weekArray[60] + "]" if room_number_weekArray[60] else ''}
2: {weekArray[61]} {"[" + room_number_weekArray[61] + "]" if room_number_weekArray[61] else ''}
3: {weekArray[62]} {"[" + room_number_weekArray[62] + "]" if room_number_weekArray[62] else ''}
4: {weekArray[63]} {"[" + room_number_weekArray[63] + "]" if room_number_weekArray[63] else ''}
5: {weekArray[64]} {"[" + room_number_weekArray[64] + "]" if room_number_weekArray[64] else ''}
6: {weekArray[65]} {"[" + room_number_weekArray[65] + "]" if room_number_weekArray[65] else ''}
7: {weekArray[66]} {"[" + room_number_weekArray[66] + "]" if room_number_weekArray[66] else ''}
8: {weekArray[67]} {"[" + room_number_weekArray[67] + "]" if room_number_weekArray[67] else ''}
""")

    elif weekArray and semigraphic_mode_on == True:
        await formSemigraphicTable(adding_from_week, user_id, 'lessons_only', weekArray, update = update)
        await update.message.reply_text(s_table, parse_mode = "HTML")
    else:
        await update.message.reply_text("There are no lessons this week.")
    weekArray.clear()
    room_number_weekArray.clear()


    print('END OF LS_COMMAND EXECUTION IN', time.time() - start_ls_timestamp)


async def ls_hw_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """list week lessons and hw: *** /ls_hw 4 *** is getting 4th week; default is current"""
    global adding_from_week
    print('EXECUTING LS_HW_COMMAND')
    start_ls_hw_timestamp = time.time()
    user_id = update.message.chat.id
    await getUserInfo(update.message.chat.id)
    await getCurrentTemporalInfo()
    done_hw_weekArray = await get_done_hw_weekArray(table_user_in, adding_from_week, update.message.chat.id)
    # print('In ls_command: tables_user_admin_in: ' + str(tables_user_admin_in))
    # print('In ls_command: tables_user_allowed_in: ' + str(tables_user_allowed_in))
    # print('In ls_command: table_user_in: ' + str(table_user_in))
    with open('mainArray.json', 'r') as fileMA:
        mainArray = json.load(fileMA)
    text = update.message.text
    words = text.split()
    await getCurrentTemporalInfo()
    # print('In ls_hw_command: words: ' + str(words))

    if len(words) == 1:
        adding_from_week = current_week_utz
        # print('executing if, len(words) == 1')
    else:
        adding_from_week = int(words[1])
        # print('words[1]: ' + words[1])
        # print('adding_from_week: ' + str(adding_from_week))

    await getWeekArray(table_user_in, adding_from_week)
    await getWeekArray_HW(table_user_in, adding_from_week)

    weekArray_HW = await getWeekArray_HW(table_user_in, adding_from_week)

    # print('In ls_hw_command: adding_from_week: ' + str(adding_from_week))
    # print(adding_from_week, current_week_utc, current_week_utz, utz, tables_user_admin_in, tables_user_allowed_in, table_user_in)

    # print(weekArray)
    # print(mainArray)
    # print(weekArray_HW)

    if weekArray and semigraphic_mode_on == False:
        # print('route if')
        await update.message.reply_text(f"""WEEK {adding_from_week}
Current week (UTC): {current_week_utc}
Current week (UTZ): {current_week_utz}
Time zone {utz}

You are administrator in {tables_user_admin_in}

You may make edits in {tables_user_allowed_in}

Table: {table_user_in}

MONDAY:
1: {weekArray[0]}
    • {weekArray_HW[0]}
2: {weekArray[1]}
    • {weekArray_HW[1]}
3: {weekArray[2]}
    • {weekArray_HW[2]}
4: {weekArray[3]}
    • {weekArray_HW[3]}
5: {weekArray[4]}
    • {weekArray_HW[4]}
6: {weekArray[5]}
    • {weekArray_HW[5]}
7: {weekArray[6]}
    • {weekArray_HW[6]}
8: {weekArray[7]}
    • {weekArray_HW[7]}

TUESDAY:
1: {weekArray[10]}
    • {weekArray_HW[10]}
2: {weekArray[11]}
    • {weekArray_HW[11]}
3: {weekArray[12]}
    • {weekArray_HW[12]}
4: {weekArray[13]}
    • {weekArray_HW[13]}
5: {weekArray[14]}
    • {weekArray_HW[14]}
6: {weekArray[15]}
    • {weekArray_HW[15]}
7: {weekArray[16]}
    • {weekArray_HW[16]}
8: {weekArray[17]}
    • {weekArray_HW[17]}

WEDNESDAY:
1: {weekArray[20]}
    • {weekArray_HW[20]}
2: {weekArray[21]}
    • {weekArray_HW[21]}
3: {weekArray[22]}
    • {weekArray_HW[22]}
4: {weekArray[23]}
    • {weekArray_HW[23]}
5: {weekArray[24]}
    • {weekArray_HW[24]}
6: {weekArray[25]}
    • {weekArray_HW[25]}
7: {weekArray[26]}
    • {weekArray_HW[26]}

THURSDAY:
1: {weekArray[30]}
    • {weekArray_HW[30]}
2: {weekArray[31]}
    • {weekArray_HW[31]}
3: {weekArray[32]}
    • {weekArray_HW[32]}
4: {weekArray[33]}
    • {weekArray_HW[33]}
5: {weekArray[34]}
    • {weekArray_HW[34]}
6: {weekArray[35]}
    • {weekArray_HW[35]}
7: {weekArray[36]}
    • {weekArray_HW[36]}
8: {weekArray[37]}
    • {weekArray_HW[37]}

FRIDAY:
1: {weekArray[40]}
    • {weekArray_HW[40]}
2: {weekArray[41]}
    • {weekArray_HW[41]}
3: {weekArray[42]}
    • {weekArray_HW[42]}
4: {weekArray[43]}
    • {weekArray_HW[43]}
5: {weekArray[44]}
    • {weekArray_HW[44]}
6: {weekArray[45]}
    • {weekArray_HW[45]}
7: {weekArray[46]}
    • {weekArray_HW[46]}
8: {weekArray[47]}
    • {weekArray_HW[47]}

SATURDAY:
1: {weekArray[50]}
    • {weekArray_HW[50]}
2: {weekArray[51]}
    • {weekArray_HW[51]}
3: {weekArray[52]}
    • {weekArray_HW[52]}
4: {weekArray[53]}
    • {weekArray_HW[53]}
5: {weekArray[54]}
    • {weekArray_HW[54]}
6: {weekArray[55]}
    • {weekArray_HW[55]}
7: {weekArray[56]}
    • {weekArray_HW[56]}
8: {weekArray[57]}
    • {weekArray_HW[57]}

SUNDAY:
1: {weekArray[60]}
    • {weekArray_HW[60]}
2: {weekArray[61]}
    • {weekArray_HW[61]}
3: {weekArray[62]}
    • {weekArray_HW[62]}
4: {weekArray[63]}
    • {weekArray_HW[63]}
5: {weekArray[64]}
    • {weekArray_HW[64]}
6: {weekArray[65]}
    • {weekArray_HW[65]}
7: {weekArray[66]}
    • {weekArray_HW[66]}
8: {weekArray[67]}
    • {weekArray_HW[67]}""")
    elif weekArray and semigraphic_mode_on == True:
        # print('done_hw_weekArray: ' + str(done_hw_weekArray))
        await formSemigraphicTable(adding_from_week, update.message.chat.id, 'hw', weekArray, weekArray_HW, done_hw_weekArray, update = update)
        await update.message.reply_text(s_table, parse_mode = "HTML")
    else:
        await update.message.reply_text("There are no lessons this week.")
    weekArray.clear()

    print('END OF LS_HW_COMMAND EXECUTION IN ', time.time() - start_ls_hw_timestamp)


async def ls_n_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print('EXECUTING LS_N_COMMAND')
    start_ls_n_timestamp = time.time()
    global adding_from_week
    user_id = update.message.chat.id
    await getUserInfo(update.message.chat.id)
    await getCurrentTemporalInfo()
    with open('mainArray.json', 'r') as fileMA:
        mainArray = json.load(fileMA)
    text = update.message.text
    words = text.split()

    if len(words) == 1:
        adding_from_week = current_week_utz
        # print('executing if, len(words) == 1')
    else:
        adding_from_week = int(words[1])
        # print('words[1]: ' + words[1])
        # print('adding_from_week: ' + str(adding_from_week))

    await getWeekArray(table_user_in, adding_from_week)

    weekArray_N = await getWeekArray_N(table_user_in, adding_from_week)

    # print('In ls_hw_command: adding_from_week: ' + str(adding_from_week))
    # print(adding_from_week, current_week_utc, current_week_utz, utz, tables_user_admin_in, tables_user_allowed_in, table_user_in)

    # print(weekArray)
    # print(mainArray)
    # print(weekArray_N)

    if weekArray:
#         print('route if')
        await update.message.reply_text(f"""WEEK {adding_from_week}
Current week (UTC): {current_week_utc}
Current week (UTZ): {current_week_utz}
Time zone {utz}

You are administrator in {tables_user_admin_in}

You may make edits in {tables_user_allowed_in}

Table: {table_user_in}""")

        i = 0
        for note in weekArray_N:
            if note != None:
                # print(note)
                await update.message.reply_text(f'Day {i // 10 + 1}, lesson {i % 10 + 1}:')
                await update.message.reply_text(note)
            i += 1

        # await update.message.reply_text(f"""# MONDAY:
# 1: {weekArray[0]}
#     • {weekArray_N[0]}
# 2: {weekArray[1]}
#     • {weekArray_N[1]}
# 3: {weekArray[2]}
#     • {weekArray_N[2]}
# 4: {weekArray[3]}
#     • {weekArray_N[3]}
# 5: {weekArray[4]}
#     • {weekArray_N[4]}
# 6: {weekArray[5]}
#     • {weekArray_N[5]}

# TUESDAY:
# 1: {weekArray[10]}
#     • {weekArray_N[10]}
# 2: {weekArray[11]}
#     • {weekArray_N[11]}
# 3: {weekArray[12]}
#     • {weekArray_N[12]}
# 4: {weekArray[13]}
#     • {weekArray_N[13]}
# 5: {weekArray[14]}
#     • {weekArray_N[14]}
# 6: {weekArray[15]}
#     • {weekArray_N[15]}

# WEDNESDAY:
# 1: {weekArray[20]}
#     • {weekArray_N[20]}
# 2: {weekArray[21]}
#     • {weekArray_N[21]}
# 3: {weekArray[22]}
#     • {weekArray_N[22]}
# 4: {weekArray[23]}
#     • {weekArray_N[23]}
# 5: {weekArray[24]}
#     • {weekArray_N[24]}
# 6: {weekArray[25]}
#     • {weekArray_N[25]}

# THURSDAY:
# 1: {weekArray[30]}
#     • {weekArray_N[30]}
# 2: {weekArray[31]}
#     • {weekArray_N[31]}
# 3: {weekArray[32]}
#     • {weekArray_N[32]}
# 4: {weekArray[33]}
#     • {weekArray_N[33]}
# 5: {weekArray[34]}
#     • {weekArray_N[34]}
# 6: {weekArray[35]}
#     • {weekArray_N[35]}

# FRIDAY:
# 1: {weekArray[40]}
#     • {weekArray_N[40]}
# 2: {weekArray[41]}
#     • {weekArray_N[41]}
# 3: {weekArray[42]}
#     • {weekArray_N[42]}
# 4: {weekArray[43]}
#     • {weekArray_N[43]}
# 5: {weekArray[44]}
#     • {weekArray_N[44]}
# 6: {weekArray[45]}
#     • {weekArray_N[45]}

# SATURDAY:
# 1: {weekArray[50]}
#     • {weekArray_N[50]}
# 2: {weekArray[51]}
#     • {weekArray_N[51]}
# 3: {weekArray[52]}
#     • {weekArray_N[52]}
# 4: {weekArray[53]}
#     • {weekArray_N[53]}
# 5: {weekArray[54]}
#     • {weekArray_N[54]}
# 6: {weekArray[55]}
#     • {weekArray_N[55]}

# SUNDAY:
# 1: {weekArray[60]}
#     • {weekArray_N[60]}
# 2: {weekArray[61]}
#     • {weekArray_N[61]}
# 3: {weekArray[62]}
#     • {weekArray_N[62]}
# 4: {weekArray[63]}
#     • {weekArray_N[63]}
# 5: {weekArray[64]}
#     • {weekArray_N[64]}
# 6: {weekArray[65]}
#     • {weekArray_N[65]}""")

    else:
        await update.message.reply_text("There are no lessons this week.")
    weekArray.clear()

    # print('END OF LS_HW_COMMAND EXECUTION')
    print('END OF LS_N_COMMAND EXECUTION IN ' + str(time.time() - start_ls_n_timestamp))


async def cs_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """create schedule command"""
    print('EXECUTING CS_COMMAND')
    start_timestamp = time.time()
    user_id = update.message.chat.id
    await getCurrentTemporalInfo()
    await getUserInfo(user_id)
    try:
        text = update.message.text
        # split the text into words
        words = text.split()

        # check if the command is formed correctly
        if len(words) > 3 or len(words) < 2:
            raise ValueError("""ERROR 779: INVALID COMMAND. Syntax example:
              
        ```
        /cs +14400
         ↑     ↑
        CMD TZinSECS
```""")

        with open('mainArray.json', 'r') as fileMA:
            mainArray = json.load(fileMA)
        taken_table_names = []
        for subarray in mainArray:
            if subarray[10] == 0:
                taken_table_names.append(subarray[4])

        proposed_table_name = None

        command = words[0]
        if len(words) == 3:
            proposed_table_name = str(words[2])


        
        # generating table name    
        table_name = None

        for i in itertools.count(start=1):
            for _ in range(26**3):  # Number of combinations for 3 upper-case Latin letters
                s = '{}-{}'.format(i, ''.join(random.choice(string.ascii_uppercase) for _ in range(3)))
                if s not in taken_table_names:
                    table_name = s
                    break
            if table_name is not None:
                break

        if table_name is None:
            raise RuntimeError("Ran out of new table names")

        if proposed_table_name not in taken_table_names and proposed_table_name is not None:
            table_name = proposed_table_name
        
        utz = words[1]

        # print(utz)

            # The additional subarray
        new_data = [0, time.time(), update.message.chat.id, 'cs', table_name, 0, 0, 0, 0, utz, 0, 0, 0, 0, 0,]

        # First, load the data already in the fileMA
        with open('mainArray.json', 'r') as fileMA:
            mainArray = json.load(fileMA)

        # Now append the new_data to your data
        mainArray.append(new_data)

        # Now write the data back to the fileMA
        with open('mainArray.json', 'w') as fileMA:
            json.dump(mainArray, fileMA)

        ti = []
        for i in range(160):
            ti.append('00:00')

        # filename = f"{table_user_in}_temporal_info.json"
        # with open(filename, 'w') as file:
        #     json.dump(ti, file)
        ti = getTableTemporalInfoFromMainArray(table_name)

        await save_data_for_interchange()

        await update.message.reply_text(f'Creating a new table {table_name}')
    
    except ValueError as e:
        # if anything goes wrong, tell the user
        await update.message.reply_text(str(e))

    print('END OF CS_COMMAND EXECUTION IN ' + str(time.time() - start_timestamp))


async def set_temporal_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """set temporal command
    
    ***
    /set_temporal 
    09:00 09:30 
    10:00 10:30 
    11:00 11:30 
    12:00 12:30 
    13:00 13:30 
    14:00 14:30
    ***"""
    
    print('EXECUTING SET_TEMPORAL_COMMAND')
    start_timestamp = time.time()
    user_id = update.message.chat.id
    await getCurrentTemporalInfo()
    await getUserInfo(user_id)
    try:
        text = update.message.text
        # split the text into words
        words = text.split()
        #temporal_info = {'first_lesson_start': words[1], 'first_lesson_end': words[2], 'second_lesson_start': words[3], 'second_lesson_end': words[4], 'third_lesson_start': words[5], 'third_lesson_end': words[6], 'fourth_lesson_start' : words[7], 'fourth_lesson_end': words[8], 'fifth_lesson_start': words[9], 'fifth_lesson_end': words[10], 'sixth_lesson_start': words[11], 'sixth_lesson_end': words[12]}
        ti = words
        """array with temporal info, 0 -- start of 1-st lesson, 1 -- end of it, 2 -- start of second... All in "00:00" format strings"""
        ti.remove(ti[0])

        # print(ti)

        if len(ti) < 21:
            for i in range(20 - len(ti)):
                ti.append('00:00')
            for i in range(7):
                ti.extend(ti)
        
        # print(ti)

        # OLD WAY to save (as a separate file):
        # filename = f"{table_user_in}_temporal_info.json"
        # with open(filename, 'w') as file:
        #     json.dump(ti, file)
        
        #res0|   time    |contrib_id| type  |table| w |d |l |cntnt|utz |vl|rg|ex|rn|r6
        await log([0, time.time(), update.message.chat.id, 'set_temporal', table_user_in, 0, 0, 0, ti, utz, 0, 0, 0, 0, 0])

        await update.message.reply_text(f'Setting temporal info for table {table_user_in}')
        await save_data_for_interchange(table_user_in)
    except ValueError as e:
        # if anything goes wrong, tell the user
        await update.message.reply_text(str(e))
    print('END OF SET_TEMPORAL_COMMAND EXECUTION IN ' + str(time.time() - start_timestamp))


async def au_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Add User command. Logs 5725753364 from *** /au 5725753364 *** to mainArray as [0, time.time(), update.message.chat.id, 'au', table_user_in, 0, 0, 0, newcomer_id, utz, 0, 0, 0, 0, 0,]. Now 5725753364 is allowed to contribute to this table"""
    print('EXECUTING AU_COMMAND')
    start_timestamp = time.time()
    await getUserInfo(update.message.chat.id)
    text = update.message.text
    words = text.split()
    if len(words) > 1:
        newcomer_id = words[1]
        if newcomer_id is not None and newcomer_id.startswith("@"):
            newcomer_id = newcomer_id[1:]
        new_data = [0, time.time(), update.message.chat.id, 'au', table_user_in, 0, 0, 0, newcomer_id, utz, 0, 0, 0, 0, 0,]
        if table_user_in in tables_user_admin_in:
            await log(new_data)
            await update.message.reply_text(f"User added to table {table_user_in}")
        else:
            await update.message.reply_text(f"You are not allowed to add new users to table {table_user_in}")
    else:
        chars = string.ascii_uppercase + string.digits
        # chars = ''.join(chr(i) for i in range(1, 0x110000)) # all unicode
        invite_code = ''.join(random.choice(chars) for _ in range(12))
        new_data = [0, time.time(), update.message.chat.id, 'ic', table_user_in, 0, 0, 0, invite_code, utz, 0, 0, 0, 0, 0,]
        if table_user_in in tables_user_admin_in:
            await log(new_data)
            await update.message.reply_text(f"Your new invite code is: ")
            await update.message.reply_text(invite_code)
        else:
            await update.message.reply_text(f"You are not allowed to add new users to table {table_user_in}")
    print('END OF AU_COMMAND EXECUTION IN ' + str(time.time() - start_timestamp))


async def ls_db_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """list db lists/arrays"""
    print('EXECUTING LS_MA_COMMAND')
    start_timestamp = time.time()
    await getCurrentTemporalInfo()
    await getUserInfo(update.message.chat.id)
    with open('mainArray.json', 'r') as fileMA:
        mainArray = json.load(fileMA)

    message = str(mainArray)
    await update.message.reply_text('mainArray:')
    # Split the message into a list of lines, respecting word boundaries
    lines = message.splitlines()

    # Join the lines back with line breaks to form a single string
    message_text = '\n'.join(lines)

    # Split the message into multiple smaller messages of maximum length 4096 characters
    wrapped_messages = textwrap.wrap(message_text, width=4096)

    # Send each wrapped message individually
    for wrapped_message in wrapped_messages:
        await update.message.reply_text(wrapped_message)

    print('END OF LS_MA_COMMAND EXECUTION IN ' + str(time.time() - start_timestamp))


async def toggle_semigraphics_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """tg_sg"""
    print('EXECUTING TOGGLE_SEMIGRAPHICS_COMMAND')
    start_timestamp = time.time()
    semigraphic_mode_on, tables_user_admin_in, tables_user_allowed_in, table_user_in, utz = await getUserInfo(update.message.chat.id)
    # print(semigraphic_mode_on)
    if semigraphic_mode_on == False:
        semigraphic_mode_on = True
    else:
        semigraphic_mode_on = False
    new_data = [0, time.time(), update.message.chat.id, 'ts', table_user_in, 0, 0, 0, semigraphic_mode_on, utz, 0, 0, 0, 0, 0,]

    #arr = [new_data]

    #with open ('sg_toggle_logs.json', 'w') as fileMA:
        #json.dump(arr, fileMA)

    with open('sg_toggle_logs.json', 'r') as file:
        sg_toggle_logs_array = json.load(file)

    sg_toggle_logs_array.append(new_data)

    with open('sg_toggle_logs.json', 'w') as file:
        json.dump(sg_toggle_logs_array, file)

    await update.message.reply_text(f"Semigr mode is now {semigraphic_mode_on}")
    print('END OF TOGGLE_SEMIGRAPHICS_COMMAND EXECUTION IN ' + str(time.time() - start_timestamp))




# from aiogram example

# button1 = InlineKeyboardButton(text="button1", callback_data="In_First_button")
# button2 = InlineKeyboardButton(
# 	text="button2", callback_data="In_Second_button")
# keyboard_inline = InlineKeyboardMarkup().add(button1, button2)

# # Message handler for the /button1 command


# @dp.message_handler(commands=['edit_log'])
# async def check(message: types.Message):
# 	await message.reply("hi! how are you", reply_markup=keyboard_inline)

# # Callback query handler for the inline keyboard buttons


# @dp.callback_query_handler(text=["In_First_button", "In_Second_button"])
# async def check_button(call: types.CallbackQuery):

# 	# Checking which button is pressed and respond accordingly
# 	if call.data == "In_First_button":
# 		await call.message.answer("Hi! This is the first inline keyboard button.")
# 	if call.data == "In_Second_button":
# 		await call.message.answer("Hi! This is the second inline keyboard button.")
# 	# Notify the Telegram server that the callback query is answered successfully
# 	await call.answer()


# #executor.start_polling(dp)









# @dp.callback_query_handler(lambda c: c.data == 'button1')
# async def process_button1(callback_query: types.CallbackQuery):
#     await callback_query.answer()
#     await callback_query.message.edit_text("Button 1 pressed!")
    
# @dp.callback_query_handler(lambda c: c.data == 'button2')
# async def process_button2(callback_query: types.CallbackQuery):
#     await callback_query.answer()
#     await callback_query.message.edit_text("Button 2 pressed!")









# @dp.message_handler(commands=['edit_log'])





async def edit_logs_command(update: Update, context: CallbackContext):
    global cr_pos, table_log_array
    keyboard = [
        [
            InlineKeyboardButton("UP", callback_data="up"),
            InlineKeyboardButton("DOWN", callback_data="down"),
        ],
        [InlineKeyboardButton("TOGGLE VALIDITY", callback_data="tv")],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    print('EXECUTING EDIT_LOG_COMMAND')
    start_timestamp = time.time()
    await getCurrentTemporalInfo()
    await getUserInfo(update.effective_user.id)

    with open('mainArray.json', 'r') as fileMA:
        mainArray = json.load(fileMA)

    table_log_array = [subarray for subarray in reversed(mainArray) if subarray[4] == table_user_in]
    cr_pos = 0

    message_text = generate_message(cr_pos, table_log_array)

    await update.effective_chat.send_message(
        text=("<pre>" + message_text + "</pre>"), parse_mode = 'HTML',
        reply_markup=reply_markup
    )

    print('END OF EDIT_LOG_COMMAND EXECUTION IN ' + str(time.time() - start_timestamp))


def generate_message(cr_pos, table_log_array):
    message_lines = []
    for i in range(6):
        line_index = i + cr_pos
        line = f"{'👉' if i == 0 else ''} {table_log_array[line_index]}"
        if len(line) < 300:
            message_lines.append(line)
            # print('s')
        else:
            message_lines.append(line[:300] + "&lt;…&gt;" + line[int(len(line)-32):])
            # print('e')
    message_lines.insert(0, "VALIDITY STATUS CORRECTION TERMINAL\n\nres0 / time_epoch / contributor_id / type / table / week / day / lesson / content / utz / validity (0 is good) / level (register) / exclusiveness of lesson addition (one-time event? 0. Keep until cancelation? 1.) / room_number / res6\n")

    return "\n".join(message_lines)


async def button_callback(update: Update, context: CallbackContext):
    global cr_pos, table_log_array
    query = update.callback_query
    callback_data = query.data

    if callback_data == 'down':
        if cr_pos < len(table_log_array) - 10:
            cr_pos += 1
    if callback_data == 'up':
        if cr_pos > 0:
            cr_pos -= 1

    elif callback_data == 'tv':
        if table_log_array[cr_pos][4] in tables_user_admin_in:
            line_index = cr_pos + 9  # Index of the 10th element in the current subarray
            if line_index >= 0 and line_index < len(table_log_array[0]):
                current_value = table_log_array[line_index][10]
                table_log_array[line_index][10] = 1 if current_value == 0 else 0

                # Update the mainArray with the modified table_log_array
                with open('mainArray.json', 'r') as fileMA:
                    mainArray = json.load(fileMA)
                    # print('tla', table_log_array[cr_pos])
                    # print('ma', mainArray[mainArray.index(table_log_array[cr_pos])])
                    # print(mainArray.index(table_log_array[cr_pos]))
                index = mainArray.index(table_log_array[cr_pos])
                if table_log_array[cr_pos][10] == 0:
                    table_log_array[cr_pos][10] = 1
                else:
                    table_log_array[cr_pos][10] = 0
                mainArray[index] = table_log_array[cr_pos]
                    # update.message.reply_text(table_log_array[0])
                # for subarray in mainArray:
                #     if subarray[4] == table_user_in:
                #         mainArray[line_index] = table_log_array[0]
                with open('mainArray.json', 'w') as fileMA:
                    json.dump(mainArray, fileMA)
                # print("validity changed")
            else:
                message_text = generate_message('NOT ALLOWED | YOU HAVE TO BE AN ADMINISTRATOR\n\n', cr_pos, table_log_array)
    message_text = generate_message(cr_pos, table_log_array)

    await query.edit_message_text(
        text=("<pre>" + message_text + "</pre>"), parse_mode = 'HTML',
        reply_markup=query.message.reply_markup
    )


# async def main():
#     updater = Updater('YOUR_TOKEN_HERE', use_context=True)
#     dp = updater.dispatcher
#     dp.add_handler(CommandHandler("edit_logs", edit_logs_command))
#     dp.add_handler(CallbackQueryHandler(button_callback))

#     await updater.start_polling()
#     updater.idle()



# Handle button presses
async def handle_button_press(update: Update, context: CallbackContext):
    query = update.callback_query
    button = query.callback_data

    if button == "up":
        cr_pos -= 1
    elif button == "down":
        cr_pos += 1
        # print(cr_pos)
    elif button == "prev":
        pass
    elif button == "next":
        pass
    elif button == "toggle_validity":
        pass



# Register the button handler
# Assuming you have an `Updater` object named `updater`
#updater = Updater(token=TOKEN, use_context=True)
#dispatcher = updater.dispatcher
#dispatcher.add_handler(CallbackQueryHandler(handle_button_press))

'''
async def button(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Parses the CallbackQuery and updates the message text."""
    query = update.callback_query

    # CallbackQueries need to be answered, even if no notification to the user is needed
    # Some clients may have trouble otherwise. See https://core.telegram.org/bots/api#callbackquery
    await query.answer()

    await query.edit_message_text(text=f"Selected option: {query.data}")
'''


# Responses

async def handle_response(text: str) -> str:
    
    if '/add' in text:
        return 'INCORRECT INPUT. You didn\'t cancel your last addition session. Try /cancel and then enter the command again.'

    return 'INCORRECT INPUT'


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Get basic info of the incoming message
    message_type: str = update.message.chat.type
    text: str = update.message.text

    # logs for debugging
    print(f'User ({update.message.chat.id}) in {message_type}: "{text}"')

    # erase bot handle from text
    if message_type == 'group':
        if BOT_USERNAME in text:
            new_text: str = text.replace(BOT_USERNAME, '').strip()
            response: str = await handle_response(new_text)
        else:
            return
    else:
        response: str = await handle_response(text)

    print('Bot:', response)
    await update.message.reply_text(response)


async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Enable logging
    import html
    import logging
    from telegram.constants import ParseMode

    logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
    )
    # set higher logging level for httpx to avoid all GET and POST requests being logged
    logging.getLogger("httpx").setLevel(logging.WARNING)
    logger = logging.getLogger(__name__)
    """Log the error and send a telegram message to notify the developer."""
    # Log the error before we do anything else, so we can see it even if something breaks.
    logger.error("Exception while handling an update:", exc_info=context.error)

    # traceback.format_exception returns the usual python message about an exception, but as a
    # list of strings rather than a single string, so we have to join them together.

    console = Console()
    if traceback_mode_is_rich:
        try:
            print(3588)
            raise context.error
        except Exception as e:
            print(3591)
            # console.log("TEST")
            try:
                console.print_exception(show_locals=True)
            except Exception as console_error:
                print(f"Error in console.print_exception: {console_error}")
            print(3593)
    else:
        tb_list = traceback.format_exception(None, context.error, context.error.__traceback__)
        tb_string = "".join(tb_list)

    print(tb_string)

    error_log_id = str(f"{int(time.time())}-{str(random.getrandbits(64))}")


    error_log = str(f"\n{error_log_id}\n\n{tb_string}\n")

    with open('error_logs.txt', 'a') as file:
        file.write(error_log)

    # Build the message with some markup and additional information about what happened.
    # You might need to add some logic to deal with messages longer than the 4096 character limit.
    update_str = update.to_dict() if isinstance(update, Update) else str(update)

    message = (
        "An exception was raised while handling an update\n\n"
        f"<pre>update = {html.escape(json.dumps(update_str, indent=2, ensure_ascii=False))}"
        "</pre>\n\n"
        f"<pre>context.chat_data = {html.escape(str(context.chat_data))}</pre>\n\n"
        f"<pre>context.user_data = {html.escape(str(context.user_data))}</pre>\n\n"
        f"<pre>{html.escape(tb_string)}</pre>\n\n"
        f"<pre>log_id: {error_log_id}</pre>"
    )


    # Finally, send the message TODO
    await context.bot.send_message(
        chat_id=DEVELOPER_CHAT_ID, text=message, parse_mode=ParseMode.HTML
    )


    # # _, _, tb = sys.exc_info()
    # # line_number = traceback.extract_tb(tb)[-1][1]
    # # print(f'Update {update} caused error {context.error} in line {line_number}')
    # import traceback
    # import sys
    # try:
    #     _, _, tb = sys.exc_info()
    #     tb_list = traceback.extract_tb(tb)
    #     if tb_list:
    #         # Extract the line number from the last entry in the traceback list, if it exists
    #         line_number = tb_list[-1].lineno
    #         print(f'Update {update} caused error {context.error} in line {line_number}')
    #     else:
    #         print(f'Update {update} caused error {context.error}, but no traceback is available.')
    # except Exception as err:
    #     print(f'An error occurred while handling another error: {err}')

    # try:
    #     traceback_formatted = traceback.format_exception(exc_type, exc_value, exc_traceback)
    #     traceback_string = ''.join(traceback_formatted)
    #     print(f"Full traceback of error in update {update}:\n{traceback_string}")
    # except Exception as e:
    #     print('ErrInErrhdl 3134XCVOI', e)
    # # Extract and print the complete formatted exception, including the stack trace
    # # exc_type, exc_value, exc_traceback = sys.exc_info()
    # # error_traceback = traceback.format_exception(exc_type, exc_value, exc_traceback)
    # # print(f"NEW ERR HANDLER: Update {update} caused error {context.error}:\n{''.join(error_traceback)}")
    # try:
    #     print(context.error)
    #     print('plplpl', sys.exc_info())

    #     exc_type = "Error getting one 978"
    #     exc_value = "Error getting one 098"
    #     exc_traceback = "Error getting one 765"
    #     exc_type, exc_value, exc_traceback = sys.exc_info()
    #     error_traceback = traceback.format_exception(exc_type, exc_value, exc_traceback)
    #     print(f"NEW ERR HANDLER: Update {update} caused error {context.error}:\n{''.join(error_traceback)}")
    # except Exception as e:
        # print('Error in error: ', e)


# Your function that performs some task and saves the result to a file
async def save_data_for_interchange(table_user_in):
    """argument: table id
    
    Saves data for interchange with other services to "interchange" folder — to call every time a table gets an update
    
    Used to send daily updates in other messagers"""

    # table_user_in = '1-HAL'
    # adding_from_week = 
    # Perform your task and save the result to a file
    # weekArray = getWeekArray()
    # weekArray_HW = getWeekArray_HW()


    await getCurrentTemporalInfo()
    week_calendar_boundaries = await getWeekCalendarBoundaries(current_week_utz)
    adding_from_week = current_week_utz

    weekArray = await getWeekArray(table_user_in, adding_from_week)

    wd_n = int(current_day_utz - 1)

    room_number_weekArray = await get_room_number_weekArray(table_user_in, adding_from_week)
    # filename = f"{table_user_in}_temporal_info.json"
    # with open(filename, 'r') as fileTI:
    #     ti = json.load(fileTI)
    ti = getTableTemporalInfoFromMainArray(table_user_in)

    for i in range(0, 200):
        try:
            if ti[i] == None:
                ti[i] = ' N/A '
        except TypeError:
            if ti == None:
                ti = []
                for i in range(0, 200):
                    ti.append(' N/A ')
            ti[i] = ' N/A '

    ti_nums = [
        [ti[20], ti[21], ti[22], ti[23], ti[24], ti[25], ti[26], ti[27], ti[28], ti[29], ti[30], ti[31], ti[32], ti[33], ti[34], ti[35], ti[36], ti[37], ti[38], ti[39]],  # monday
        [ti[40], ti[41], ti[42], ti[43], ti[44], ti[45], ti[46], ti[47], ti[48], ti[49], ti[50], ti[51], ti[52], ti[53], ti[54], ti[55], ti[56], ti[57], ti[58], ti[59]],
        [ti[60], ti[61], ti[62], ti[63], ti[64], ti[65], ti[66], ti[67], ti[68], ti[69], ti[70], ti[71], ti[72], ti[73], ti[74], ti[75], ti[76], ti[77], ti[78], ti[79]],
        [ti[80], ti[81], ti[82], ti[83], ti[84], ti[85], ti[86], ti[87], ti[88], ti[89], ti[90], ti[91], ti[92], ti[93], ti[94], ti[95], ti[96], ti[97], ti[98], ti[99]],
        [ti[100], ti[101], ti[102], ti[103], ti[104], ti[105], ti[106], ti[107], ti[108], ti[109], ti[110], ti[111], ti[112], ti[113], ti[114], ti[115], ti[116], ti[117], ti[118], ti[119]],
        [ti[120], ti[121], ti[122], ti[123], ti[124], ti[125], ti[126], ti[127], ti[128], ti[129], ti[130], ti[131], ti[132], ti[133], ti[134], ti[135], ti[136], ti[137], ti[138], ti[139]],
        [ti[140], ti[141], ti[142], ti[143], ti[144], ti[145], ti[146], ti[147], ti[148], ti[149], ti[150], ti[151], ti[152], ti[153], ti[154], ti[155], ti[156], ti[157], ti[158], ti[159]],  # sunday
    ]

    # print('in td wA: ', weekArray)
    wA_nums = [
        [weekArray[0], weekArray[1], weekArray[2], weekArray[3], weekArray[4], weekArray[5], weekArray[6], weekArray[7], weekArray[8], weekArray[9]],
        [weekArray[10], weekArray[11], weekArray[12], weekArray[13], weekArray[14], weekArray[15], weekArray[16], weekArray[17], weekArray[18], weekArray[19]],
        [weekArray[20], weekArray[21], weekArray[22], weekArray[23], weekArray[24], weekArray[25], weekArray[26], weekArray[27], weekArray[28], weekArray[29]],
        [weekArray[30], weekArray[31], weekArray[32], weekArray[33], weekArray[34], weekArray[35], weekArray[36], weekArray[37], weekArray[38], weekArray[39]],
        [weekArray[40], weekArray[41], weekArray[42], weekArray[43], weekArray[44], weekArray[45], weekArray[46], weekArray[47], weekArray[48], weekArray[49]],
        [weekArray[50], weekArray[51], weekArray[52], weekArray[53], weekArray[54], weekArray[55], weekArray[56], weekArray[57], weekArray[58], weekArray[59]],
        [weekArray[60], weekArray[61], weekArray[62], weekArray[63], weekArray[64], weekArray[65], weekArray[66], weekArray[67], weekArray[68], weekArray[69]],  # sunday
    ]

    # print(wA_nums)



    # if update.message.from_user.language_code == 'ru':
    wd_names = ['ПОНЕДЕЛЬНИК', 'ВТОРНИК', 'СРЕДА', 'ЧЕТВЕРГ', 'ПЯТНИЦА', 'СУББОТА', 'ВОСКРЕСЕНЬЕ']
    # else:
    #     wd_names = ['MONDAY', 'TUESDAY', 'WEDNESDAY', 'THURSDAY', 'FRIDAY', 'SATURDAY', 'SUNDAY']

    for i, element in enumerate(room_number_weekArray):
        if element is None:
            room_number_weekArray[i] = ' '

    for i, element in enumerate(room_number_weekArray):
        if len(str(element)) != 5:
            room_number_weekArray[i] = ' '*(5-len(str(element))) + str(element)
    
    # print(int(wd_n*10+1))
    # print(wd_n)
    # print(room_number_weekArray)

    s_table = (f"""┌──────────────────────────┐
│WEEK {str(int(adding_from_week))} {str(week_calendar_boundaries)}{' '*(20-(len(str(int(adding_from_week)))+len(str(week_calendar_boundaries))))}│
├──────────────────────────┤
│{wd_names[wd_n] + ' '*(26-len(wd_names[wd_n]))}│
├─┬─────┬─────┬─────┬──────┤
│1│{ti_nums[wd_n][0]}│{ti_nums[wd_n][1]}│{room_number_weekArray[wd_n*10+0]}│{str(wA_nums[wd_n][0]) + ' '*(6-len(str(wA_nums[wd_n][0]))) if wA_nums[wd_n][0] != None else '      '}│
├─┼─────┼─────┼─────┼──────┤
│2│{ti_nums[wd_n][2]}│{ti_nums[wd_n][3]}│{room_number_weekArray[wd_n*10+1]}│{str(wA_nums[wd_n][1]) + ' '*(6-len(str(wA_nums[wd_n][1]))) if wA_nums[wd_n][1] != None else '      '}│
├─┼─────┼─────┼─────┼──────┤
│3│{ti_nums[wd_n][4]}│{ti_nums[wd_n][5]}│{room_number_weekArray[wd_n*10+2]}│{str(wA_nums[wd_n][2]) + ' '*(6-len(str(wA_nums[wd_n][2]))) if wA_nums[wd_n][2] != None else '      '}│
├─┼─────┼─────┼─────┼──────┤
│4│{ti_nums[wd_n][6]}│{ti_nums[wd_n][7]}│{room_number_weekArray[wd_n*10+3]}│{str(wA_nums[wd_n][3]) + ' '*(6-len(str(wA_nums[wd_n][3]))) if wA_nums[wd_n][3] != None else '      '}│
├─┼─────┼─────┼─────┼──────┤
│5│{ti_nums[wd_n][8]}│{ti_nums[wd_n][9]}│{room_number_weekArray[wd_n*10+4]}│{str(wA_nums[wd_n][4]) + ' '*(6-len(str(wA_nums[wd_n][4]))) if wA_nums[wd_n][4] != None else '      '}│
├─┼─────┼─────┼─────┼──────┤
│6│{ti_nums[wd_n][10]}│{ti_nums[wd_n][11]}│{room_number_weekArray[wd_n*10+5]}│{str(wA_nums[wd_n][5]) + ' '*(6-len(str(wA_nums[wd_n][5]))) if wA_nums[wd_n][5] != None else '      '}│
├─┴─────┴─────┴─────┴──────┤
│TABLE ID: {table_user_in + ' '*(16-len(table_user_in))}│
└──────────────────────────┘""")
    # await update.message.reply_text(s_table, parse_mode='HTML')

    # print(s_table)


    # interchange_json_update = perform_task()
    # with open('result.txt', 'w') as file:
    #     file.write(result)

    td_upd_dic = {
        'updated_since_last_usage': True,
        'today_text': s_table,
        'weekArray': weekArray,
        'ti_nums': ti_nums,
        'room_number_weekArray': room_number_weekArray
    }

    if not os.path.exists('interchange'):
        os.makedirs('interchange')

    with open(f'interchange/wsbot_today_update_{table_user_in}.json', 'w') as fp:
        """for interchange with other programs"""
        json.dump(td_upd_dic, fp)
    # https://stackoverflow.com/questions/51943049/what-does-p-stand-for-in-fp-of-with-openfilename-w-as-fp

    return(s_table)


def get_list_of_all_tables():
    """returnes a list of all tables ever created in mainArray"""
    with open('mainArray.json', 'r') as fp:
        mainArray = json.load(fp)
    ids = [subarray[4] for subarray in data if subarray[3] == 'cs']
    return ids

async def update_interchange_data_for_all_tables(context):
    # print(random.randint(0, 100), '3255_0000')
    table_ids = get_list_of_all_tables()
    for table_id in table_ids:
        save_data_for_interchange(table_id)

from telegram.ext import Updater

# u = Updater(TOKEN, use_context=True)
# j = u.job_queue

# def callback_minute(context: telegram.ext.CallbackContext):
#     context.bot.send_message(chat_id='@examplechannel', 
#                              text='One message every minute')

# job_update_interchange_data_for_all_tables = j.run_repeating(update_interchange_data_for_all_tables, interval=60, first=10)
# """https://github.com/python-telegram-bot/v13.x-wiki/wiki/Extensions-%E2%80%93-JobQueue"""
# print(job_update_interchange_data_for_all_tables)


async def callback_timer(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.message.chat_id
    name = update.effective_chat.full_name
    await context.bot.send_message(chat_id=chat_id, text='Setting a timer for 1 minute!')
    # Set the alarm:
    context.job_queue.run_once(callback_alarm, 60, data=name, chat_id=chat_id)


if __name__ == '__main__':
    print('Starting bot...')
    app = Application.builder().token(TOKEN).build()

    convo_handler = ConversationHandler(
        entry_points=[CommandHandler('add', add_command)],
        states={
            TYPE: [MessageHandler(filters.TEXT & ~filters.COMMAND, type_sel)],
            WEEK: [MessageHandler(filters.TEXT & ~filters.COMMAND, week_sel)],
            # DAY: [MessageHandler(filters.TEXT & ~filters.COMMAND, specific_date_selection)],
            # SPECIFIC_DATE: [MessageHandler(filters.TEXT & ~filters.COMMAND, lesson_number_selection)],
            DAY: [MessageHandler(filters.TEXT & ~filters.COMMAND, day_sel)],
            LESSON_NUMBER: [MessageHandler(filters.TEXT & ~filters.COMMAND, lesson_number_sel)],
            EVENT_TYPE_IF_REGULAR: [MessageHandler(filters.TEXT & ~filters.COMMAND, if_one_time_event_or_regular_sel)],
            ADD_FOR: [MessageHandler(filters.TEXT & ~filters.COMMAND, add_for)],
            CONTENT: [MessageHandler(filters.TEXT & ~filters.COMMAND, content_input)],
            ROOM: [MessageHandler(filters.TEXT & ~filters.COMMAND, room_input)],
        },
        fallbacks=[CommandHandler('cancel', cancel_add_conv)]
    )

    app.add_handler(convo_handler)

    # Commands
    app.add_handler(CommandHandler('start', start_command))
    app.add_handler(CommandHandler('help', help_command))
    app.add_handler(CommandHandler('al', al_command))
    app.add_handler(CommandHandler('ah', ah_command))
    app.add_handler(CommandHandler('an', an_command))
    app.add_handler(CommandHandler('ls', ls_command))
    app.add_handler(CommandHandler('ls_hw', ls_hw_command))
    app.add_handler(CommandHandler('ls_n', ls_n_command))
    app.add_handler(CommandHandler('cs', cs_command))
    app.add_handler(CommandHandler('lg', lg_command))
    app.add_handler(CommandHandler('au', au_command))
    app.add_handler(CommandHandler('ls_db', ls_db_command))
    app.add_handler(CommandHandler('edit_logs', edit_logs_command))
    app.add_handler(CommandHandler('set_temporal', set_temporal_command))
    app.add_handler(CommandHandler('tg_sg', toggle_semigraphics_command))
    app.add_handler(CommandHandler('done', done_command))
    app.add_handler(CallbackQueryHandler(button_callback))
    app.add_handler(CommandHandler('today', today_command))
    app.add_handler(CommandHandler('mv', mv_command))
    # app.add_handler(CommandHandler('add', add_command))

    timer_handler = CommandHandler('timer', callback_timer)
    app.add_handler(timer_handler)

    job_queue = app.job_queue

    # Schedule the job to run every hour
    # hourly_job = job_queue.run_repeating(update_interchange_data_for_all_tables, interval=20)
   
    # Messages
    app.add_handler(MessageHandler(filters.TEXT, handle_message))

    # Errors
    app.add_error_handler(error)

    # Polls the bot
    # How often checks for new messages, secs
    print('Polling...')
    print('\033[92m▶ Telegram bot ┄┄ [ONLINE]\033[0m')
    # 
    # >>> print('\033[92m▶ WikiSchedule Telegram bot online!\033[0m') 
    # ▶ WikiSchedule Telegram bot online!
    # >>> print('\033[32m▶ WikiSchedule Telegram bot online!\033[0m') 
    # ▶ WikiSchedule Telegram bot online!
    # 
    # await executor.start_polling(dp)
    # asyncio.run(save_data_for_interchange())
    app.run_polling(poll_interval=True)
