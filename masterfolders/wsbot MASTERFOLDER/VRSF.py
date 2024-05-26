# VK regular schedule forward

# Replace OpenMeteo if ever deployed for commercial environment

getpage_language = 'russian'

logging_mode_is_loguru = True

import asyncio
from vkbottle import Keyboard, KeyboardButtonColor, Text
import os
# from vkbottle import API
from PIL import Image, ImageDraw, ImageFont

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

import traceback


if logging_mode_is_loguru == True:
    import sys
    from loguru import logger
    logger.remove()
    logger.add(sys.stderr, level="WARNING")
else:
    import logging
    logging.getLogger("vkbottle").setLevel(logging.INFO)

print('line 55  compiling openmeteo_requests')  # right after it struggling

timestamp1 = time.time()
import openmeteo_requests
print(f"compiling took {time.time() - timestamp1}{' f#cking' if time.time() - timestamp1 > 10 else ''} seconds")
print('line 60')
import requests_cache
print('line 62  compiling pandas')  # right after it struggling
timestamp1 = time.time()
import pandas as pd
print(f"compiling took {time.time() - timestamp1}{' f#cking' if time.time() - timestamp1 > 10 else ''} seconds")
# print('line 66')
from retry_requests import retry

# print('line 69')

data_file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'config.json'))

# Open the config.json file
with open(data_file_path) as file:
    data = json.load(file)

token = data['vk_bot_token']
# print('Token:', token)

# token = ""
bot = Bot(token=token)
photo_uploader = PhotoMessageUploader(bot.api)

def get_weather_data_from_openmeteo(lat, lon):
    """Get weather data from Open-Meteo API"""

    # Setup the Open-Meteo API client with cache and retry on error
    cache_session = requests_cache.CachedSession('.cache', expire_after = 3600)
    retry_session = retry(cache_session, retries = 5, backoff_factor = 0.2)
    openmeteo = openmeteo_requests.Client(session = retry_session)
    # "latitude": 58.08,
    # "longitude": 52.4,
    # Make sure all required weather variables are listed here
    # The order of variables in hourly or daily is important to assign them correctly below
    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": lat,
        "longitude": lon,
        "daily": ["weather_code", "temperature_2m_max", "temperature_2m_min", "apparent_temperature_max", "apparent_temperature_min", "sunrise", "sunset", "daylight_duration", "sunshine_duration", "uv_index_max", "uv_index_clear_sky_max", "precipitation_sum", "rain_sum", "showers_sum", "snowfall_sum", "precipitation_hours", "precipitation_probability_max", "wind_speed_10m_max", "wind_gusts_10m_max", "wind_direction_10m_dominant", "shortwave_radiation_sum", "et0_fao_evapotranspiration"],
        "timezone": "auto",
        "forecast_days": 1
    }
    responses = openmeteo.weather_api(url, params=params)

    # Process first location. Add a for-loop for multiple locations or weather models
    response = responses[0]
    print(f"Coordinates {response.Latitude()}°E {response.Longitude()}°N")
    print(f"Elevation {response.Elevation()} m asl")
    print(f"Timezone {response.Timezone()} {response.TimezoneAbbreviation()}")
    print(f"Timezone difference to GMT+0 {response.UtcOffsetSeconds()} s")

    # Process daily data. The order of variables needs to be the same as requested.
    daily = response.Daily()
    daily_weather_code = daily.Variables(0).ValuesAsNumpy()
    daily_temperature_2m_max = daily.Variables(1).ValuesAsNumpy()
    daily_temperature_2m_min = daily.Variables(2).ValuesAsNumpy()
    daily_apparent_temperature_max = daily.Variables(3).ValuesAsNumpy()
    daily_apparent_temperature_min = daily.Variables(4).ValuesAsNumpy()
    daily_sunrise = daily.Variables(5).ValuesAsNumpy()
    daily_sunset = daily.Variables(6).ValuesAsNumpy()
    daily_daylight_duration = daily.Variables(7).ValuesAsNumpy()
    daily_sunshine_duration = daily.Variables(8).ValuesAsNumpy()
    daily_uv_index_max = daily.Variables(9).ValuesAsNumpy()
    daily_uv_index_clear_sky_max = daily.Variables(10).ValuesAsNumpy()
    daily_precipitation_sum = daily.Variables(11).ValuesAsNumpy()
    daily_rain_sum = daily.Variables(12).ValuesAsNumpy()
    daily_showers_sum = daily.Variables(13).ValuesAsNumpy()
    daily_snowfall_sum = daily.Variables(14).ValuesAsNumpy()
    daily_precipitation_hours = daily.Variables(15).ValuesAsNumpy()
    daily_precipitation_probability_max = daily.Variables(16).ValuesAsNumpy()
    daily_wind_speed_10m_max = daily.Variables(17).ValuesAsNumpy()
    daily_wind_gusts_10m_max = daily.Variables(18).ValuesAsNumpy()
    daily_wind_direction_10m_dominant = daily.Variables(19).ValuesAsNumpy()
    daily_shortwave_radiation_sum = daily.Variables(20).ValuesAsNumpy()
    daily_et0_fao_evapotranspiration = daily.Variables(21).ValuesAsNumpy()

    daily_data = {"date": pd.date_range(
        start = pd.to_datetime(daily.Time(), unit = "s"),
        end = pd.to_datetime(daily.TimeEnd(), unit = "s"),
        freq = pd.Timedelta(seconds = daily.Interval()),
        inclusive = "left"
    )}
    daily_data["weather_code"] = daily_weather_code
    daily_data["temperature_2m_max"] = daily_temperature_2m_max
    daily_data["temperature_2m_min"] = daily_temperature_2m_min
    daily_data["apparent_temperature_max"] = daily_apparent_temperature_max
    daily_data["apparent_temperature_min"] = daily_apparent_temperature_min
    daily_data["sunrise"] = daily_sunrise
    daily_data["sunset"] = daily_sunset
    daily_data["daylight_duration"] = daily_daylight_duration
    daily_data["sunshine_duration"] = daily_sunshine_duration
    daily_data["uv_index_max"] = daily_uv_index_max
    daily_data["uv_index_clear_sky_max"] = daily_uv_index_clear_sky_max
    daily_data["precipitation_sum"] = daily_precipitation_sum
    daily_data["rain_sum"] = daily_rain_sum
    daily_data["showers_sum"] = daily_showers_sum
    daily_data["snowfall_sum"] = daily_snowfall_sum
    daily_data["precipitation_hours"] = daily_precipitation_hours
    daily_data["precipitation_probability_max"] = daily_precipitation_probability_max
    daily_data["wind_speed_10m_max"] = daily_wind_speed_10m_max
    daily_data["wind_gusts_10m_max"] = daily_wind_gusts_10m_max
    daily_data["wind_direction_10m_dominant"] = daily_wind_direction_10m_dominant
    daily_data["shortwave_radiation_sum"] = daily_shortwave_radiation_sum
    daily_data["et0_fao_evapotranspiration"] = daily_et0_fao_evapotranspiration

    daily_dataframe = pd.DataFrame(data = daily_data)
    print('daily_dataframe', daily_dataframe)
    return daily_data

daily_data = get_weather_data_from_openmeteo(58.08, 52.4)
# print('shortwave_radiation_sum', daily_data['shortwave_radiation_sum'])


def get_weather_description(code, language):
    """Get description of weather from WMO code

Languages: ru, en

Codes: "00" -- "99" """
    with open(f"WeatherCodes-{language}.json", 'r', encoding='utf-8') as file:
        weather_codes = json.load(file)
    for item in weather_codes:
        if item[0] == code:
            return item[1]  # Return the description
    return "Code not found"  # Return a default message if the code isn't found

# print(f"{get_weather_description(str(int(daily_data['weather_code'])), 'ru')} plfucmz9")
async def send_schedule_updates():

    try:
        filename = f'forward_group-table_dictionary.json'
        with open(filename, 'r') as file:
            clientListDic = json.load(file)
    except:
        print('\n\n🟥 ERROR 8761JL01QV: json file not found 🟥\n\n')

    # print(clientListDic)


    try:
        daily_data = get_weather_data_from_openmeteo(58.08, 52.4)
    except:
        print('\n\n🟥 ERROR UHYY5789LU: getting weather 🟥\n\n')

    for peer_id, table_id in clientListDic.items():
        # print(f"Key: {peer_id}, Value: {table_id}")
        # peer_id | table_id
        # key     |    value

        try:
            # TODO: replace with imported from mainArray


            with open(f'interchange/wsbot_today_update_{table_id}.json', 'r') as file:
                tz = 14400  # TODO: replace with imported from mainArray
                wsbot_today_update = json.load(file)
            # print('wsbot_today_update', wsbot_today_update)
            
            
            
            try:
                # print('ntaoir', str(int(daily_data['weather_code'])))
                # msg_to_img_str = f"""{int(daily_data['temperature_2m_min'])} {int(daily_data["temperature_2m_max"])}
                msg_to_img_str = f"""{get_weather_description(str(int(daily_data['weather_code'])), 'ru')}
{str(int(daily_data['temperature_2m_min']))} ↔ {str(int(daily_data["temperature_2m_max"]))}°C, ветер {str(int(daily_data["wind_speed_10m_max"]))} м/c
{wsbot_today_update['today_text']}
Это расписание обновляется
сообществом WikiSchedule.
Вы можете внести свой вклад
через Telegram: {data['telegram_bot_username']}"""
                message_image = string_to_image(msg_to_img_str)
                message_image.save('message_image.png', 'PNG')
                image_path = os.path.abspath('message_image.png')
                # print('image_path', image_path)

                try:
                    image = await photo_uploader.upload(
                    file_source=image_path,
                    peer_id=peer_id,)
                except Exception as e:
                    print('\n\n🟥 ERROR 86xxVDEU4837 🟥\n\n', e)
                try:
                    # print('image', image)
                    await message.answer(attachment=image)
                except Exception as e:
                    print('\n\n🟥 ERROR 88xx58YUUY 🟥\n\n', e)
                
                try:
                    await bot.api.messages.send(peer_id=peer_id, attachment=image, random_id=0)
                except Exception as e:
                    print('\n\n🟥 ERROR 90xx584TNE: attachment was not sent 🟥\n\n', e)
                
                # await bot.api.messages.send(peer_id=peer_id, message=wsbot_today_update['today_text'], random_id=0)
            except Exception as e:
                print('\n\n🟥 ERROR 27059sexcm75: message was not sent 🟥\n\n', str(e), '\n\n')
                # print()
        except:
            print('Empty iteration')
            
        # from PIL import Image, ImageDraw, ImageFont

        # table_string = """
        # ┌─────┬─────┐
        # │ Col1 │ Col2 │
        # ├─────┼─────┤
        # │ Val1 │ Val2 │
        # ├─────┼─────┤
        # │ Val3 │ Val4 │
        # └─────┴─────┘
        # """

        # # Load a font
        # font_path = r"C:\Users\qwert\Downloads\JetBrainsMono-2.304\fonts\ttf\JetBrainsMonoNL-Regular.ttf"  # This should be the path to a font file (ttf or otf)
        # font_size = 12
        # try:
        #     font = ImageFont.truetype(font_path, font_size)
        # except IOError:
        #     print(f"\n\n🟥Error 84ufDH57 Font not found: {font_path} 🟥\n\n")
            
        # # Create an ImageDraw instance
        # draw = ImageDraw.Draw(Image.new('RGB', (1, 1)))  # Create a temporary blank image

        # # Use the font object to measure the text size
        # text_width, text_height = draw.textsize(table_string, font=font)

        # # Create the actual image with proper dimensions
        # image_width = text_width + 20  # Add some padding
        # image_height = text_height + 20
        # image = Image.new('RGB', (image_width, image_height), "white")

        # # Create a new ImageDraw object for the final image
        # draw = ImageDraw.Draw(image)

        # # Draw the text onto the image
        # draw.text((10, 10), table_string, font=font, fill='black')

        # # Save the image
        # image.save('table_image.png')

    
def string_to_image(table_string):

    # Load a font
    font_path = r"C:\Users\qwert\Downloads\JetBrainsMono-2.304\fonts\ttf\JetBrainsMonoNL-Regular.ttf"
    # TODO: replace with imported font path
    font_size = 12
    try:
        font = ImageFont.truetype(font_path, font_size)
    except IOError:
        print(f"\n\n🟥Error 84ufDH57 Font not found: {font_path} 🟥\n\n")

    # Create an ImageDraw instance
    image_draw = ImageDraw.Draw(Image.new('RGB', (1, 1)))

    # Use the new methods to measure text size
    bbox = image_draw.textbbox((0, 0), table_string, font=font)
    text_width, text_height = bbox[2] - bbox[0], bbox[3] - bbox[1]

    # Create the actual image with proper dimensions
    image_width = text_width + 20  # Add some padding
    image_height = text_height + 20
    image = Image.new('RGB', (image_width, image_height), "white")

    # Create a new ImageDraw object for the final image
    image_draw = ImageDraw.Draw(image)

    # Draw the text onto the image
    image_draw.text((10, 10), table_string, font=font, fill='black')

    # Save the image
    image.save('table_image.png')

    return image


import platform
if platform.system()=='Windows':
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

# asyncio.run(main())
# schedule.every(5).seconds.do(print, 'ao')
# schedule.every.day.at("10:00").do(send_schedule_updates)
schedule.every().day.at("02:06").do(print, 'a^^o')
schedule.every().day.at("07:00").do(send_schedule_updates)
# Local tz
# asyncio.run(send_schedule_updates())
# asyncio.run(send_schedule_updates())
# asyncio.run(send_schedule_updates())
print('\033[92m▶ VRSF service [ONLINE]\033[0m')
while True:
    schedule.run_pending()
