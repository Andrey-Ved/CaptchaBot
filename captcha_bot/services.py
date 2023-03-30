from asyncio import sleep
from datetime import datetime, timedelta

from captcha_bot import (
    BAN_TIME, TIME_FOR_TEST, OnlyReadPermissions, SPEECHES, WORKS_CHATS
)
from captcha_bot.dispatcher import bot, doubtful_users


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

    await bot.restrict_chat_member(
        chat_id=chat_id,
        user_id=user_id,
        permissions=OnlyReadPermissions,
        until_date=until_date()
    )

    await bot.delete_message(chat_id, test_message_id)
