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
from pdf2image import convert_from_path, convert_from_bytes
from pdf2image.exceptions import (
PDFInfoNotInstalledError,
PDFPageCountError,
PDFSyntaxError
)

import PyPDF2
from pdf2image import convert_from_path

import tracemalloc
tracemalloc.start(100)
# TODO: remove
from vkbottle import DocMessagesUploader

from vkbottle import PhotoMessageUploader
from vkbottle.bot import Bot

import sys
print(sys.path)
# import pytesseract
from pdf2image import convert_from_path
import PyPDF2
import io
# import rich

# import sys
# from loguru import logger
# logger.remove()
# logger.add(sys.stderr, level="WARNING")

import logging
logging.getLogger("vkbottle").setLevel(logging.INFO)


import os
# os.chdir('C:/Users/qwert/wsbot foulder')

sys.path.append('C:/Users/qwert/wsbot foulder')
# allows to execute functions from wsbot in this directory
# TODO: move to a more convinient, obvious for end user to specify own place

# import C:/Users/qwert/wsbot foulder/mainArray.json
# from wsbot import today_command, getCurrentTemporalInfo, getWeekCalendarBoundaries, getWeekArray, get_room_number_weekArray
# import wsbot

data_file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'config.json'))
with open(data_file_path) as file:
    data = json.load(file)
    """configuration data dictionary"""
vk_bot_token = data['vk_bot_token']
print(f'Token: {vk_bot_token}')

token = vk_bot_token
bot = Bot(token=token)
photo_uploader = PhotoMessageUploader(bot.api)

async def get_pdf_names_in_MASTERFOLDER():
    """Returns a list of .pdf file names in MASTERFOLDER (the one py file is in), as a list, no ".pdf" at the end of each string"""
    print('57823')
    tb_list = []
    for i in os.listdir('textbooks/'):
        if i.endswith('.pdf') and not i.endswith('_temp.pdf'):
            tb_list.append(i[:-4])
            print('tb_list', end=' ')
            print(tb_list)
    return tb_list

# asyncio.run(get_pdf_names_in_MASTERFOLDER())

# acceptable inquries:
# In groups:
#     234 engSmith @getpage
#     @getpage 694
#     382 @getpage
#     @getpage
# In chats:
#     329 engSmith
#     289
#     x

async def conv_pdf_to_image(doc, tb_id, page_number):

    # await message.answer('q;ylwupf')
    # await message.answer(f'textbooks/{tb_id}_temp.pdf')
    try:
        image = convert_from_path(pdf_path = f'textbooks/{tb_id}_temp.pdf', poppler_path = r"C:\\poppler-windows-23.08.0-0")
        print('fucm' + str(image))
        image = await photo_uploader.upload(
        file_source="C:\\Users\\qwert\\OneDrive\\Изображения\\Screenshots\\Снимок экрана (28).png",
        peer_id=message.peer_id,
    )
        print('nttntnao')
        await message.answer(attachment=image)
    except PDFInfoNotInstalledError:
        await message.answer('Nya!\n\nAn exception occured while uploading the image version.\n\nIt looks like we\'ve got PDFInfoNotInstalledError, senpai. Is Poppler installed? Is it added to PATH? If you are running this program on a Windows machine, chanses are, it\'s not.\n\nPlease refer to the library documentation: https://pypi.org/project/pdf2image/ (or just replace it with a better library with fewer dependencies)')
    except:
        await message.answer('NYA!\n\nAn exception occured while uploading the image version.\n\nIs Poppler installed, senpai? Is it added to PATH, baka? If you are running this program on a Windows machine, chanses are, it\'s not.\n\nPlease refer to the library documentation: https://pypi.org/project/pdf2image/ (or just replace it with a better library with fewer dependencies)')



















async def get_doc(tb_id, page_number):

    print('STARTING GET_DOC')

    # page_number -= 1  # replace 1 with your page number (note: PyPDF2 uses 0 indexing)  

    input_pdf_path = f'textbooks/{tb_id}.pdf'
    temp_pdf_path = f'textbooks/{tb_id}_temp.pdf'

    # Open the pdf
    with open(input_pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        print('file received')

        # try:
        # Get the specified page
        page = reader.pages[page_number - 1]  # decrement by 1 because PyPDF2 counts from 0
        print('page assigned')
        # except IndexError:
        #     return

        # Create a PDF writer object
        writer = PyPDF2.PdfWriter()
        
        # Add the page to the writer
        writer.add_page(page)
        print('page added to writer')
        
        # Output the page to a new pdf
        with open(temp_pdf_path, 'wb') as output_pdf:
            writer.write(output_pdf)
            print('page written to temp location')

    return output_pdf, temp_pdf_path



global utz
async def today_command(table_user_in, utz):
    """List schedule for today"""
    print('EXECUTING TODAY_COMMAND')
    utz == 14400
    current_week_utc, current_day_utc, current_week_utz, current_day_utz, current_lesson_num_utz, current_lesson_id_utz = await getCurrentTemporalInfo()
    week_calendar_boundaries = await getWeekCalendarBoundaries(current_week_utz)
    adding_from_week = current_week_utz
    await getWeekArray(table_user_in, adding_from_week)
    room_number_weekArray = await get_room_number_weekArray(table_user_in, adding_from_week)
    filename = f"{table_user_in}_temporal_info.json"
    with open(filename, 'r') as fileTI:
        ti = json.load(fileTI)
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

    print(wA_nums)


    if getpage_language == 'russian':
        wd_names = ['ПОНЕДЕЛЬНИК', 'ВТОРНИК', 'СРЕДА', 'ЧЕТВЕРГ', 'ПЯТНИЦА', 'СУББОТА', 'ВОСКРЕСЕНЬЕ']
    else:
        wd_names = ['MONDAY', 'TUESDAY', 'WEDNESDAY', 'THURSDAY', 'FRIDAY', 'SATURDAY', 'SUNDAY']

    for i, element in enumerate(room_number_weekArray):
        if element is None:
            room_number_weekArray[i] = ' '

    for i, element in enumerate(room_number_weekArray):
        if len(str(element)) != 5:
            room_number_weekArray[i] = ' '*(5-len(str(element))) + str(element)
    
    print(int(wd_n*10+1))
    print(wd_n)
    print(room_number_weekArray)

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
    print('END OF TODAY_COMMAND EXECUTION')
    return s_table




@bot.on.message()
async def general_handler(message: Message):
    print('MSGMSGMSG ' + str(message))
    print(message.peer_id, 'pppiii')
    text = message.text
    words = text.split()
    # if len(words) == 3:
    #     if words[0].isdigit():
    #         # case if msg is: --<number> <tb_id> [<handle>]-- ~~329 engSmith [@getpage]~~
    #         # "[]" means "optional" # no more, ignore it
    #         page_number = words[0]
    #         tb_id = words[1]
    #         if len(words) == 3:
    #             handle = words[2]
    #     else:
    #         # case if msg is: --<tb_id> [<handle>]-- ~~329 engSmith [@getpage]~~
    # if len(words) == 2:
    #     if words[0].isdigit():
    #         # case if msg is: --<number> <tb_id>-- ~~329 engSmith~~
    #         page_number = words[0]
    #         tb_id = words[1]
    #     else:
    #     tb_id = words[0]
    #     # case if msg is: --<tb_id> [<handle>]-- ~~329 engSmith [@getpage]~~
    #         handle = words[1]

    # for word in words:
    #     if word.startswith('['):
    #         word = 

    print('received msg', text)
    print('words', words)

    # await today_command('1-HAL', 14400)

    page_number = None
    tb_id = None
    handle = None

    if words[0].isdigit():
        page_number = int(words[0])
    elif words[0].startswith('@') or words[0].startswith('['):
        handle = words[0]
    else:
        tb_id = words[0]

    if len(words) >= 2:

        if words[1].isdigit():
            page_number = int(words[1])
        elif words[1].startswith('@') or words[1].startswith('['):
            handle = words[1]
        else:
            tb_id = words[1]

    if len(words) == 3:

        if words[2].isdigit():
            page_number = int(words[2])
        elif words[2].startswith('@') or words[2].startswith('['):
            handle = words[2]
        else:
            tb_id = words[2]

    # cases: 
    # 1: page and tb is reported
    # 2: only page is reported
    # 3: only tb is reported

    # 1:

    if handle == '@all':
        return



    print(f'page_number: {page_number},')
    print(f'tb_id: {tb_id},')
    print(f'handle: {handle}')

    # await message.answer(f'page_number: {page_number}, tb_id: {tb_id}, handle: {handle}')

    list_of_pdfs = await get_pdf_names_in_MASTERFOLDER()

    print('list_of_pdfs', list_of_pdfs)



    # users_info = await bot.api.users.get(message.from_id)
    # keyboard = Keyboard(one_time=False, inline=True)
    # # О параметрах one_time и inline вы можете прочитать в документации к апи вконтакте
    # keyboard.add(Text("Кнопка 1"), color=KeyboardButtonColor.POSITIVE)
    # # Первая строка (ряд) добавляется автоматически
    # keyboard.add(Text("Кнопка 2"))
    # keyboard.add(Text("Кнопка 3"))
    # keyboard.row()  # Переходим на следующую строку
    # keyboard.add(Text("Кнопка 2"))
    # keyboard.add(Text("Кнопка 3"))
    # keyboard.add(Text("Кнопка 2"))
    # keyboard.row()  # Переходим на следующую строку
    # keyboard.add(Text("Кнопка 3"))
    # keyboard.add(Text("Кнопка 2"))
    # keyboard.add(Text("Кнопка 3"))
    # await message.answer(message="""Пожалуйста, выберете учебник:""", keyboard=keyboard.get_json())

    eol = '\n'
    # TODO decide if 'eol' or 'EOL'

    if tb_id is None or tb_id not in list_of_pdfs:
        keyboard = Keyboard(one_time=False, inline=True)
        # О параметрах one_time и inline вы можете прочитать в документации к апи вконтакте
        
        for tb in list_of_pdfs:
            keyboard.row()
            keyboard.add(Text(str(page_number) + ' ' + str(tb)))

        await message.answer(message=f"{'Учебник не найден.' + eol + eol if tb_id is not None else ''}Пожалуйста, выберете учебник:", keyboard=keyboard.get_json())

        # keyboard.add(Text("Кнопка 3", payload={"command": 3}))




    # if tb_id not in list_of_pdfs:
    #     if getpage_language == 'russian':
    #         await message.answer(f'Учебник не найден.\n\n{tb_id}.pdf отсутствует в папке "textbooks".\n\nВот список доступных учебников:\n\n{list_of_pdfs}')
    #     else: # TODO decide if moe
    #         await message.answer(f'No such textbook found.\n\nNo {tb_id}.pdf in foulder "textbooks".\n\nHere are available textbooks, senpai:\n\n{list_of_pdfs}')
    #     return

    try:

        # Send a message to the user.
        loading_msg = await bot.api.messages.send(user_id=message.peer_id, message="💬 Загрузка страницы…", random_id=0)

        output_pdf, temp_pdf_path = await get_doc(tb_id, page_number)
        
        # Delete the message.
        await bot.api.messages.delete(message_ids=[loading_msg], delete_for_all=True)

    except IndexError:
        await message.answer('IndexError: Страница не найдена')
        return
    
    # Send a message to the user.
    loading_to_server_msg = await bot.api.messages.send(user_id=message.peer_id, message="🛰 Отправка…", random_id=0)


    doc_uploader = DocMessagesUploader(bot.api)

    # await message.answer(temp_pdf_path)
    # await message.answer(output_pdf)
    print('uploading...')
    
    upl_start_time = time.time()                   
            
    doc = await doc_uploader.upload(
    title=f'{tb_id}_temp.pdf',
    file_source=f'textbooks/{tb_id}_temp.pdf',
    peer_id=message.peer_id
    )
                                            
    print("Doc uploaded in ", time.time() - upl_start_time, " seconds")         

    # Delete the message.
    await bot.api.messages.delete(message_ids=[loading_to_server_msg], delete_for_all=True)

    ans_start_time = time.time()
    await message.answer(attachment=doc)
    print("Doc was sent in ", time.time() - ans_start_time)

    await getWeek(None, None)

        # ^^^ IT WORKS ^^^


    # await conv_pdf_to_image(doc, tb_id, page_number)



    # photo = await photo_uploader.upload(
    # file_source="C:\\Users\\qwert\\OneDrive\\Изображения\\Screenshots\\Снимок экрана (28).png",
    # peer_id=message.peer_id,
    # )
    # await message.answer(attachment=photo)






    # import typing
    # from vkbottle import Bot, types
    # from vkbottle.api import API
    # from vkbottle.exception_factory import VKError

    # async def upload_doc(api: API, peer_id: int, file_path: str) -> typing.Union[str, None]:
    #     try:
    #         upload_server = (await api.docs.get_messages_upload_server(peer_id=peer_id, type="doc")).upload_url
    #         upload_file = api.http.post(upload_server, files={"file": open(file_path, "rb")}).json()

    #         doc = await api.docs.save(file=upload_file['file'], title=file_path)
    #         return f"doc{doc[0]['owner_id']}_{doc[0]['id']}"

    #     except VKError as e:
    #         print(e)
    #         return None

    # @bot.on.message()
    # async def handle(message: types.Message):
    #     # Suppose we want to send a PDF document located in the local directory.
    #     pdf_path = "lorem_ipsum_example.pdf"
        
    #     doc_attachment = await upload_doc(api, message.peer_id, pdf_path)
    #     if doc_attachment:
    #         await message.answer("Here is your PDF file", attachment=doc_attachment)







    # from vkbottle import PhotoMessageUploader, DocMessagesUploader
    # from vkbottle.bot import Bot, Message



    # doc = await DocMessagesUploader.upload(
    # title='textbook',
    # file_source=temp_pdf_path,
    # peer_id=message.peer_id,
    # )
    # await message.answer(attachment=doc)

    # # Convert PDF into images
    # images = convert_from_path(temp_pdf_path)

    # # Save images to file
    # for i, image in enumerate(images):
    #     image.save(f'textbooks/{tb_id}_page_{page_number}_img_{i+1}.png', 'PNG')

    # # Don't forget to delete your temporary pdf file
    # import os
    # os.remove(temp_pdf_path)



















    return

    users_info = await bot.api.users.get(message.from_id)
    keyboard = Keyboard(one_time=False, inline=True)
    # О параметрах one_time и inline вы можете прочитать в документации к апи вконтакте
    keyboard.add(Text("Кнопка 1"), color=KeyboardButtonColor.POSITIVE)
    # Первая строка (ряд) добавляется автоматически
    keyboard.row()  # Переходим на следующую строку
    keyboard.add(Text("Кнопка 2"))
    keyboard.add(Text("Кнопка 3", payload={"command": 3}))
    await message.answer(message="""Пожалуйста, выберете учебник:""", keyboard=keyboard.get_json())

bot.run_forever()

# async def main():
#     await today_command('1-HAL', 14400)


print(os.listdir())












# async def main():
#     api = API("token")
#     await api.wall.post(message="Hello, world!")

# asyncio.run(main())



# from vkbottle.bot import Bot

# bot = Bot("token")

# @bot.on.message()
# async def handler(_) -> str:
#     return "Hello world!"

# bot.run_forever()