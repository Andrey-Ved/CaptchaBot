from captcha_bot.dispatcher import bot, dp, doubtful_users, keyboard
from datetime import datetime, timedelta
from pytz import timezone
from asyncio import sleep

from captcha_bot import (BAN_TIME, TIME_FOR_TEST,
                         BUTTONS_NUMBER, BUTTON_PREDICATE,
                         DIGIT_IN_WRITING,
                         OnlyReadPermissions,
                         SPEECHES,
                         RAILWAY_APP_NAME,
                         WEBHOOK_URL, WEBHOOK_PATH, WEBHOOK_URL,
                         WEBAPP_HOST, WEBAPP_PORT,
                         BOT_TOKEN,
                         WORKS_CHATS,
                         USERS_DATA_FILE)


def until_date():
    return datetime.now() + timedelta(minutes=BAN_TIME)


async def check_chats(message):
    if message.chat.id in WORKS_CHATS:
        return True

    await bot.send_message(message.chat.id, SPEECHES['wrong chat id'])

    return False


async def deferred_verification(chat_id, test_message_id, user_id):
    await sleep(TIME_FOR_TEST)

    if user_id not in doubtful_users:
        return

    await bot.restrict_chat_member(chat_id=chat_id,
                                   user_id=user_id,
                                   permissions=OnlyReadPermissions,
                                   until_date=until_date())

    await bot.delete_message(chat_id, test_message_id)
