from aiogram import Bot, Dispatcher
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from captcha_bot.users_data import *
from captcha_bot import (
    BOT_TOKEN, USERS_DATA_FILE, BUTTONS_NUMBER, BUTTON_PREDICATE)


bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

doubtful_users = UsersWithFile(USERS_DATA_FILE)

buttons = [
    InlineKeyboardButton(str(i),
                         callback_data=BUTTON_PREDICATE + str(i))
    for i in range(0, BUTTONS_NUMBER)
]

keyboard = InlineKeyboardMarkup(row_width=BUTTONS_NUMBER).add(*buttons)
