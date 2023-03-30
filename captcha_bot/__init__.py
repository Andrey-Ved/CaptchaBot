from aiogram import types
import os
from dotenv import load_dotenv, find_dotenv


load_dotenv(find_dotenv())

BOT_TOKEN = os.getenv('BOT_TOKEN')

RAILWAY_APP_NAME = os.getenv('RAILWAY_APP_NAME')

WEBHOOK_HOST = f'https://{RAILWAY_APP_NAME}.railway.app'
WEBHOOK_PATH = f'/webhook/{BOT_TOKEN}'
WEBHOOK_URL = f'{WEBHOOK_HOST}{WEBHOOK_PATH}'

WEBAPP_HOST = '0.0.0.0'
WEBAPP_PORT = os.getenv('PORT', default=8000)

MAX_CHATS_NUMBER = 10

WORKS_CHATS = {}
for i in range(MAX_CHATS_NUMBER):
    chat_id = os.getenv('CHAT_ID_' + str(i))
    if chat_id:
        WORKS_CHATS[chat_id] = 'chat_id_' + str(i)

USERS_DATA_FILE = os.getenv('USERS_DATA_FILE')

BAN_TIME = 30  # minutes
TIME_FOR_TEST = 30  # seconds

BUTTONS_NUMBER = 6
BUTTON_PREDICATE = 'btn_'

assert BUTTON_PREDICATE[-1] not in BUTTON_PREDICATE[0:-1], "BUTTON_PREDICATE has incorrect format"

DIGIT_IN_WRITING = {'1': 'ОДИН',
                    '2': 'ДВА',
                    '3': 'ТРИ',
                    '4': 'ЧЕТЫРЕ',
                    '5': 'ПЯТЬ',
                    '0': 'НОЛЬ'}

for BUTTON in range(BUTTONS_NUMBER):
    assert str(BUTTON) in DIGIT_IN_WRITING, "DIGIT_IN_WRITING does not contain desired key"

OnlyReadPermissions = types.ChatPermissions(can_send_messages=False,
                                            can_send_media_messages=False,
                                            can_send_polls=False,
                                            can_send_other_messages=False,
                                            can_add_web_page_previews=False,
                                            can_change_info=False,
                                            can_invite_users=False,
                                            can_pin_messages=False)

SPEECHES = {'wrong chat id': 'Брать чужих ботов без спроса очень не хорошо.',
            'not you': 'Не тебя проверяю!',
            'right': 'Правильно!',
            'not right': 'Неправильно, я тебя баню!',
            'greeting with riddle': (lambda name, number:
                                     f'Привет, {name}! Это анти-спам проверка. Если ты не бот, ' +
                                     f'нажми в течение {TIME_FOR_TEST} сек. кнопку c цифрой {number}')
            }
