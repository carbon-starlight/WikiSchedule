# print("""
# ██╗    ██╗██╗██╗  ██╗██╗███████╗ ██████╗██╗  ██╗███████╗██████╗ ██╗   ██╗██╗     ███████╗    
# ██║    ██║██║██║ ██╔╝██║██╔════╝██╔════╝██║  ██║██╔════╝██╔══██╗██║   ██║██║     ██╔════╝    
# ██║ █╗ ██║██║█████╔╝ ██║███████╗██║     ███████║█████╗  ██║  ██║██║   ██║██║     █████╗      
# ██║███╗██║██║██╔═██╗ ██║╚════██║██║     ██╔══██║██╔══╝  ██║  ██║██║   ██║██║     ██╔══╝      
# ╚███╔███╔╝██║██║  ██╗██║███████║╚██████╗██║  ██║███████╗██████╔╝╚██████╔╝███████╗███████╗    
#  ╚══╝╚══╝ ╚═╝╚═╝  ╚═╝╚═╝╚══════╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚═════╝  ╚═════╝ ╚══════╝╚══════╝    
                                                                                             
# """)

displayVersion = False
# Configure version number font here
numberFontIsLightLine = True
numberFontIsBoldLine = False
preset_config = None

import json
# import os
import subprocess
import sys

with open('config.json', 'r') as f:
    config = json.load(f)
version = config["version"]

NumAssmbl = {
    "0": ["╔═╗", "║ ║", "╚═╝"],
    "1": [" ╦ ", " ║ ", " ╩ "],
    "2": ["╔═╗", "╔═╝", "╚═╝"],
    "3": ["╔═╗", " ═╣", "╚═╝"],
    "4": ["╦ ╦", "╚═╣", "  ╩"],
    "5": ["╔═╗", "╚═╗", "╚═╝"],
    "6": ["╔═╗", "╠═╗", "╚═╝"],
    "7": ["╔═╗", " ═╣", "  ╩"],
    "8": ["╔═╗", "╠═╣", "╚═╝"],
    "9": ["╔═╗", "╚═╣", "╚═╝"],
}

NumAssmblLightLine = {
    "0": ["┌─┐", "│ │", "└─┘"],
    "1": [" ┬ ", " │ ", " ┴ "],
    "2": ["┌─┐", "┌─┘", "└─┘"],
    "3": ["┌─┐", " ─┤", "└─┘"],
    "4": ["┬ ┬", "└─┤", "  ┴"],
    "5": ["┌─┐", "└─┐", "└─┘"],
    "6": ["┌─┐", "├─┐", "└─┘"],
    "7": ["┌─┐", " ─┤", "  ┴"],
    "8": ["┌─┐", "├─┤", "└─┘"],
    "9": ["┌─┐", "└─┤", "└─┘"],
}

NumAssmblBoldLine = {
    "0": ["┏━┓", "┃ ┃", "┗━┛"],
    "1": [" ┳ ", " ┃ ", " ┻ "],
    "2": ["┏━┓", "┏━┛", "┗━┛"],
    "3": ["┏━┓", " ━┫", "┗━┛"],
    "4": ["┳ ┳", "┗━┫", "  ┻"],
    "5": ["┏━┓", "┗━┓", "┗━┛"],
    "6": ["┏━┓", "┣━┓", "┗━┛"],
    "7": ["┏━┓", " ━┫", "  ┻"],
    "8": ["┏━┓", "┣━┫", "┗━┛"],
    "9": ["┏━┓", "┗━┫", "┗━┛"],
}


if numberFontIsLightLine:
    NumAssmbl = NumAssmblLightLine
if numberFontIsBoldLine:
    NumAssmbl = NumAssmblBoldLine

parts = version.split(".")
if len(parts) == 1:
    parts.append(None)
    parts.append(None)
if len(parts) == 2:
    parts.append(None)
version = parts
# print(version)
if displayVersion:
        
    print(f"""
╦ ╦┬┬┌─┬╔═╗┌─┐┬ ┬┌─┐┌┬┐┬ ┬┬  ┌─┐  {NumAssmbl[version[0]][0]} {NumAssmbl[version[1]][0] if version[1] != None else ''} {                                  NumAssmbl[version[2]][0] if version[2] != None else ''} 
║║║│├┴┐│╚═╗│  ├─┤├┤  │││ ││  ├┤   {NumAssmbl[version[0]][1]} {NumAssmbl[version[1]][1] if version[1] != None else ''} {                                  NumAssmbl[version[2]][1] if version[2] != None else ''} 
╚╩╝┴┴ ┴┴╚═╝└─┘┴ ┴└─┘─┴┘└─┘┴─┘└─┘  {NumAssmbl[version[0]][2]}o{NumAssmbl[version[1]][2] if version[1] != None else ''}{"o" if version[2] != None else ''}{NumAssmbl[version[2]][2] if version[2] != None else ''} 
""")
else:
    print(f"""
╦ ╦┬┬┌─┬╔═╗┌─┐┬ ┬┌─┐┌┬┐┬ ┬┬  ┌─┐
║║║│├┴┐│╚═╗│  ├─┤├┤  │││ ││  ├┤ 
╚╩╝┴┴ ┴┴╚═╝└─┘┴ ┴└─┘─┴┘└─┘┴─┘└─┘
""")


"""
╦ ╦┬┬┌─┬╔═╗┌─┐┬ ┬┌─┐┌┬┐┬ ┬┬  ┌─┐  ┌─┐ ┌─┐ ┌─┐
║║║│├┴┐│╚═╗│  ├─┤├┤  │││ ││  ├┤   ┌─┘ │ │ │ │
╚╩╝┴┴ ┴┴╚═╝└─┘┴ ┴└─┘─┴┘└─┘┴─┘└─┘  └─┘o└─┘o└─┘

╔═╗ ╔═╗ ╔═╗
╔═╝ ║ ║ ║ ║
╚═╝o╚═╝o╚═╝

╦ ╦┬┬┌─┬╔═╗┌─┐┬ ┬┌─┐┌┬┐┬ ┬┬  ┌─┐  ╔═╗ ╔═╗ ╔═╗
║║║│├┴┐│╚═╗│  ├─┤├┤  │││ ││  ├┤   ╔═╝ ║ ║ ║ ║
╚╩╝┴┴ ┴┴╚═╝└─┘┴ ┴└─┘─┴┘└─┘┴─┘└─┘  ╚═╝o╚═╝o╚═╝

"""

# print(_0[0], _1[0], _2[0], _3[0], _4[0], _5[0], _6[0], _7[0], _8[0], _9[0])
# print(_0[1], _1[1], _2[1], _3[1], _4[1], _5[1], _6[1], _7[1], _8[1], _9[1])
# print(_0[2], _1[2], _2[2], _3[2], _4[2], _5[2], _6[2], _7[2], _8[2], _9[2])


print('Welcome to WikiSchedule set script — command line edition!')
print('Please, proceed through the following steps to set up your server.\n')
print('You can also proceed with one of pre-set configurations by pressing a number: 1 — saved tokens, no VK; 2 — saved tokens, VK on.')

preconfig = None
# change_token = ((input(f'\nDo you want to ensure dependencies are installed? (If it is the first time you run this program on this computer / virtual enviroment it is recommended to leave "y") (y/n) [y]: ')).lower() or 'y') == 'y'
change_token = input(f'\nDo you want to ensure dependencies are installed? (If it is the first time you run this program on this computer / virtual enviroment it is recommended to leave "y") (y/n) [y]: ').lower() or 'y'

if change_token == '' or change_token == 'y':
    change_token == True
if change_token == 'n':
    change_token == False

print(change_token)

if change_token not in ('1', '2'):

    if change_token:
        # Ensure that we are using the same Python executable that is running this script
        print('Installing dependences...')
        python_executable = sys.executable
        
        # Define the command to install dependencies
        command = [python_executable, '-m', 'pip', '--timeout=1000', 'install', '-r', 'requirements.txt']
        
        # Run the command
        try:
            subprocess.check_call(command)
            print("All requirements have been installed.")
        except subprocess.CalledProcessError as e:
            print(f"An error occurred while trying to install dependencies: {e}")
            sys.exit(1)


    with open('config.json', 'r') as f:
        data = json.load(f)

    # change_username = input(f'The Telegram bot username is currently set to {data["telegram_bot_username"]}. Do you want to change it? (y/n) [n]: ').lower() == 'y'

    user_input = input(f'The Telegram bot username is currently set to "{data["telegram_bot_username"]}". Would you like to change it? (y/n) [n]: ')
    change_username = (user_input.lower() or 'n') == 'y'
    # print(change_username)

    if change_username:
        new_username = input('Enter the new username: ')
        data['telegram_bot_username'] = new_username

    # print(f'')

    user_input = input(f'\nThe Telegram bot token is currently set to "{data["telegram_bot_token"]}". Would you like to change it? (y/n) [n]: ')
    change_token = (user_input.lower() or 'n') == 'y'
    # change_token = (input(f'\nThe Telegram bot token is currently set to "{data["telegram_bot_token"]}". Would you like to change it? (y/n) [n]: ').lower() or 'n') == 'y'
    # print(change_token)

    # new_token = input('Enter the new token (or type "c" to cancel): ')

    if change_token:
        new_token = input('Enter the new token: ')
        data['telegram_bot_token'] = new_token

    user_input = (f'\nMessages from the bot will be sent to a developer\'s chat with the following ID: "{data["developer_telegram_chat_id"]}". Would you like to change it? (y/n) [n]: ')
    change_chat_id = (user_input.lower() or 'n') == 'y'

    if change_chat_id:
        new_chat_id = input('Enter the new chat ID: ')
        data['developer_telegram_chat_id'] = new_chat_id

    user_input = input(f'\nWikiSchedule also supports forwarding messages to a VK group chat and storing a textbook database that can be accessed via VK group. Would you like to enable it? (y/n) [n]: ')
    forward_to_vk = (user_input.lower() or 'n') == 'y'

    change_vk_bot_token = False
    if forward_to_vk:
        user_input = input(f'\nThe VK bot token is currently set to "{data["vk_bot_token"]}". Would you like to change it? (y/n) [n]: ')
        change_vk_bot_token = (user_input.lower() or 'n') == 'y'

    if change_vk_bot_token:
        new_vk_bot_token = input('\nEnter the new token: ')
        data['vk_bot_token'] = new_vk_bot_token

    with open('config.json', 'w') as f:
        json.dump(data, f)
else:
    preset_config = str(change_token)

if preset_config == '1':
    forward_to_vk = False
elif preset_config == '2':
    forward_to_vk = True

print('')

print('Starting wsbot.py...')

import subprocess
from pathlib import Path

# # Assuming __file__ is defined in your script, otherwise, replace it with another method to get the current script directory.
# current_script_dir = Path(__file__).parent.resolve()
# relative_path_to_wsbot = Path("masterfolders/wsbot MASTERFOLDER")
# wsbot_dir = current_script_dir / relative_path_to_wsbot

# # Adjust the command to just the script name, because cwd is set to the script's directory
# subprocess.Popen(['python', 'wsbot.py'], cwd=str(wsbot_dir))

wsbot_dir = Path(__file__).parent.resolve() / Path("masterfolders/wsbot MASTERFOLDER")

# Adjust the command to just the script name, because cwd is set to the script's directory



try:
    processes = []

    # Start wsbot.py
    wsbot_process = subprocess.Popen(
        ['python', 'wsbot.py'], 
        cwd=str(Path(__file__).parent.resolve() / Path("masterfolders/wsbot MASTERFOLDER"))
    )
    processes.append(wsbot_process)

    if forward_to_vk:
        print('Starting getpage.py...')
        getpage_process = subprocess.Popen(
            ['python', 'getpage.py'], 
            cwd=str(Path(__file__).parent.resolve() / Path("masterfolders/getpage MASTERFOLDER"))
        )
        processes.append(getpage_process)

        print('Starting VRSF.py...')
        vrsf_process = subprocess.Popen(
            ['python', 'VRSF.py'], 
            cwd=str(Path(__file__).parent.resolve() / Path("masterfolders/wsbot MASTERFOLDER"))
        )
        processes.append(vrsf_process)

        print('Starting VRSFS.py...')
        vrsfs_process = subprocess.Popen(
            ['python', 'VRSFS.py'], 
            cwd=str(Path(__file__).parent.resolve() / Path("masterfolders/wsbot MASTERFOLDER"))
        )
        processes.append(vrsfs_process)

    finish = input('Enter "f" to finish execution.')

finally:
    # Stop all started processes
    for proc in processes:
        proc.terminate()  # Send SIGTERM
        try:
            proc.wait(timeout=5)  # Wait for process to gracefully exit
        except subprocess.TimeoutExpired:
            proc.kill()  # Force kill if it doesn't exit in time

    print('All subprocesses were terminated.')



# subprocess.Popen(['python', 'wsbot.py'], cwd=str(Path(__file__).parent.resolve() / Path("masterfolders/wsbot MASTERFOLDER")))
# # subprocess.Popen(['python', 'add_webapp.py'], cwd=str(Path(__file__).parent.resolve() / Path("masterfolders/wsbot MASTERFOLDER")))

# if forward_to_vk:
#     print('Starting getpage.py...')
#     subprocess.Popen(['python', 'getpage.py'], cwd=str(Path(__file__).parent.resolve() / Path("masterfolders/getpage MASTERFOLDER")))
#     print('Starting VRSF.py...')
#     subprocess.Popen(['python', 'VRSF.py'], cwd=str(Path(__file__).parent.resolve() / Path("masterfolders/wsbot MASTERFOLDER")))
#     print('Starting VRSFS.py...')
#     subprocess.Popen(['python', 'VRSFS.py'], cwd=str(Path(__file__).parent.resolve() / Path("masterfolders/wsbot MASTERFOLDER")))

# finish = input('Enter "f" or <Ctrl+C> to finish execution.')









# scripts = ['masterfolders/wsbot MASTERFOLDER/wsbot.py', 'masterfolders/getpage MASTERFOLDER/getpage.py', 'masterfolders/getpage MASTERFOLDER/VRSF.py', 'masterfolders/getpage MASTERFOLDER/VRSFS.py']

# # List to track the process objects
# processes = []

# # Launch the scripts in separate processes
# for script in scripts:
#     proc = subprocess.Popen(['python', script])
#     processes.append(proc)
