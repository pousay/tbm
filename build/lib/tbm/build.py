import os
import inquirer
import time


def write(path: str, content: str):
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)


def build():
    print("~" * 40)
    for i in range(1, 4):
        print(f"LOADING{'.' * i}", end="\r")
        time.sleep(0.3)

    os.system("cls" if os.name == "nt" else "clear")

    questions = [
        inquirer.Text(
            "name",
            "ENTER YOUR PROJECT NAME >>> ",
        ),
        inquirer.List(
            "type",
            message="CHOOSE YOUR PROJECT TYPE >>> ",
            choices=["Telegram bot", "Client bot"],
        ),
    ]

    answers = inquirer.prompt(questions)

    is_telegram_bot = True if answers["type"] == "Telegram bot" else False

    name = answers["name"]
    root = name.strip()
    os.mkdir(root)

    # run.py
    write(
        root + "/run.py",
        RUN.format(
            name,
            "bot_token=config.TOKEN ,"
            if is_telegram_bot
            else "phone_number=config.PHONE_NUMBER ,",
        ),
    )

    # config.py
    write(
        root + "/config.py",
        CONFIG.format(
            'TOKEN = "" #bot token here'
            if is_telegram_bot
            else 'PHONE_NUMBER = "+" #phone number here',
        ),
    )

    # database.py
    os.mkdir(root + "/database")
    write(root + "/database.py", DB.format(name))

    # keys.py
    write(root + "/keys.py", KEYS)

    # plugins/*.py      handlers
    os.mkdir(root + "/plugins")
    write(root + "/plugins/admin_panel.py", AP)
    write(root + "/plugins/user_panel.py", UP)

    # gitignore
    write(
        root + "/.gitignore",
        f"config.py\n\ndatabase\ndatabase/{name}.db",
    )

    # reqs.txt
    write(root + "/requirements.txt", "pyrogram==2.0.106")

    write(root + "/README.md", name + "\n\n")


RUN = """
from pyrogram import Client
import config

app = Client(
    name='{}' ,
    api_id=config.API_ID ,
    api_hash=config.API_HASH ,
    {}
    plugins=dict(root="plugins") ,
)






app.run()
"""

CONFIG = """
API_ID = 1234 #api id here
API_HASH = "" #api hash here
{}


SUDO = 1234 #admin id here
"""

DB = """
from sqlite3 import connect

conn = connect("database/{}.db")
cursor = conn.cursor()



#code here 



#simple example [user table] :
cursor.execute(
    '''
    CREATE TABLE IF NOT EXISTS users(
        id INT PRIMARY KEY NOT NULL,
        step INT NOT NULL,
        joined_date TEXT NOT NULL,
        is_banned INT NOT NULL
    )'''
)

"""

AP = """
from pyrogram import Client, filters, types
from database import something #change this to your functions [if necessary]
import config
import keys

@Client.on_message(filters.user(config.SUDO))
async def admin_panel(bot:Client, mes:types.Message):
    #code here

    text = mes.text
    if text == '/start' :
        answer = '''
Hello from tgm, a telegram bot package manager
welcome Admin :)) 
        
    '''
        await mes.reply(answer,True,reply_markup=keys.Admin_start)



"""

UP = """
from pyrogram import Client, filters, types
from database import something #change this to your functions [if necessary]
import config
import keys


@Client.on_message(~filters.user(config.SUDO))
async def user_panel(bot:Client, mes:types.Message):
    #code here

    text = mes.text
    if text == '/start' : 
        await mes.reply('Hello From tgm, a telegram bot package manager :))',True, reply_markup=keys.Home)


"""

KEYS = """
from pyrogram.types import (
    ReplyKeyboardMarkup,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
)



#customize your keyboards here
# this is a simple example

Admin_start = ReplyKeyboardMarkup(
    [["user panel"], ["admin panel"]], resize_keyboard=True
)
Back = ReplyKeyboardMarkup([["↪️ BACK ↪️"]], resize_keyboard=True)

# user start
Home = ReplyKeyboardMarkup(
    [
        ["ACCOUNT INFO"],
        ["HELP", "SUPPORT"],
    ],
    resize_keyboard=True,
)
"""
