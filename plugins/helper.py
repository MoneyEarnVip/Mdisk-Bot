# (c) HeimanPictures
import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

import os

from config import Config

import pyrogram
logging.getLogger("pyrogram").setLevel(logging.WARNING)

from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton



START = """
Hi {}!
        
This Is MDisk Bot For Free 😇
Read /help Carefully & Do Follow All Given Instruction...
For More Bots Join @TamilanXBots
"""

HELP = """
**How To?**
__➢ Send Me Link From https://mypowerdisk.com/mybox and upload link or video here.
➢ Get Link after uploading in that site.
➢ Now Paste that link in this bot__

**NOTE:**
__➢ Do Not Spam, Send Link One By One__

"""

# NON_OWNER = "You Can't Use Me Ask My [Owner](tg://user?id={})"


START_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('Help', callback_data='help'),
        InlineKeyboardButton('Close', callback_data='close')
        ]]
    )
HELP_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('📮 Update 📮', url='https://telegram.dog/tamilanxbots/'),
        InlineKeyboardButton('🛠️ Support 🛠️', url='https://telegram.dog/tamilanxbots/'),
        ],[
        InlineKeyboardButton('Home', callback_data='home'),
        InlineKeyboardButton('Close', callback_data='close')
        ]]
    )

CLOSE_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('Close', callback_data='close')
        ]]
    )



@Client.on_message(filters.command('start') & filters.private)
async def start(bot, message):
        await message.reply_chat_action("typing")
        await message.reply_text(
            text=START.format(message.from_user.mention),
            disable_web_page_preview=True,
            reply_markup=START_BUTTONS
        )


@Client.on_message(filters.command('help') & filters.private)
async def help(bot, message):
        await message.reply_chat_action("typing")
        await message.reply_text(
            text=HELP,
            disable_web_page_preview=True,
            reply_markup=HELP_BUTTONS
        )



@Client.on_callback_query()
async def cb_data(bot, update):
    if update.data == "home":
        await update.message.edit_text(
            text=START.format(update.from_user.mention),
            disable_web_page_preview=True,
            reply_markup=START_BUTTONS
        )
    elif update.data == "help":
        await update.message.edit_text(
            text=HELP,
            disable_web_page_preview=True,
            reply_markup=HELP_BUTTONS
        )
    else:
        await update.message.delete()
