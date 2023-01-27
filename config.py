from multiprocessing.connection import Connection
from os import environ
from pyrogram.types import InlineKeyboardButton,InlineKeyboardMarkup


class Config(object):
        #Your telegram BOT username(without @) : get it from @BotFather
        BOT_USERNAME = environ.get("BOT_USERNAME")
        #Your telegram BOT API token : get it from @BotFather
        BOT_TOKEN = environ.get("BOT_TOKEN")
        #API_ID of your Telegram Account my.telegram.org/apps
        API_ID = int(environ.get("API_ID"))
        #API_HASH of your Telegram Account my.telegram.org/apps
        API_HASH = environ.get("API_HASH")
        #API_ID of your Telegram Account my.telegram.org/apps
        API_ID1 = int(environ.get("API_ID1"))
        #API_HASH of your Telegram Account my.telegram.org/apps
        API_HASH1 = environ.get("API_HASH1")
        #Your telegram user id
        OWNER_ID = environ.get("OWNER_ID")
        #For logs channel to note down important bot level events, recommend to make this public. ex: '-123456'
        LOG_GROUP_ID = environ.get("LOG_GROUP_ID")
        #Get From Here.https://www.mongodb.com/ (Same as MONGO_URL but give differant value for this) 
        BASE_DB = environ.get("BASE_DB")
        #Get From Here.https://www.mongodb.com/
        MONGO_URL = environ.get("MONGO_URL")
        #Don't change this value:https://arq.hamker.in
        ARQ_API_URL = environ.get("ARQ_API_URL")
        #Get this from @ARQRobot.
        ARQ_API_KEY = environ.get("ARQ_API_KEY")
        #now you can set custom command handler for TotalSecurity like : / ! ,
        COMMAND_PREFIXES = environ.get("COMMAND_PREFIXES")
        #The Telegram channel id you want focus user.(User can't start your bot without join it)
        F_SUB_CHANNEL = environ.get("F_SUB_CHANNEL")

class var(object):
        #TotalSecurity group start message here 
        group_start_text = "Hey :) PM me if you have any questions on how to use me!"
        #TotalSecurity help menu text message here 
        help_text = """
**Welcome to the help menu**

I am a group management bot with some useful features.
You can choose an option below by clicking a button.
If you have any bugs or questions about how to use me.

**All commands can be used with the following: / **"""
        #TotalSecurity start menu conections(split commands on start)
        Connection_text_start = "** Ejecute /connections para ver o desconectarse de grupos!**"
        #TotalSecurity private start message here
        pm_start_text = """
Hey there {},my name is {}
An  advanced telegram Group management Bot For helpYou Protect Your Groups & Suit For All Your Needs.feel free to add me to your groups! """
        #Languages change text menu here 
        lang_text = "Choose Your languages"

        #Languages change button menu here this will show current languages TotalSecurity can message
        lang_keyboard = InlineKeyboardMarkup(
                [
                        [
                                InlineKeyboardButton(text="🇱🇷 English", callback_data="languages_en")
                        ],
                        [
                                InlineKeyboardButton(text="🇪🇸 Español", callback_data="languages_es"), 
                                InlineKeyboardButton(text="🇵🇹 Portugues", callback_data="languages_pt")
                        ],  
                        [
                                InlineKeyboardButton("« Back", callback_data='startcq')
                        ]
                ]
)
        #TotalSecurity informations button menu here
        about_buttons = InlineKeyboardMarkup(
                [
                        [
                                InlineKeyboardButton(text="👥Support Group", url="https://t.me/+SynslZ3fFe5XNFbn"),
                                InlineKeyboardButton(text="👤News Channel", url="https://t.me/+SynslZ3fFe5XNFbn")
                        ], 
                        [
                                InlineKeyboardButton("« Back", callback_data='startcq')
                        ]
                ]
)
        #TotalSecurity private start button menu here
        home_keyboard_pm = InlineKeyboardMarkup(
                [
                        [
                                InlineKeyboardButton(text="Add Me To Your Chat 🎉",url=f"http://t.me/{Config.BOT_USERNAME}?startgroup=new")
                        ],
                        [
                                InlineKeyboardButton(text="About ✨",callback_data="_about"),
                                InlineKeyboardButton(text="languages 🌏",callback_data="_langs")
                        ],
                        [
                                InlineKeyboardButton(text="Help Menu ⚒",callback_data="bot_commands")
                        ],
                        [
                                InlineKeyboardButton(text="Website 💭",url=f"https://t.me/+SynslZ3fFe5XNFbn"),
                                InlineKeyboardButton(text="News Channel 📢",url=f"https://t.me/+SynslZ3fFe5XNFbn")
                        ]
                ]
)
        