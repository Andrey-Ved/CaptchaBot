from aiogram.dispatcher.filters import Text
from random import randint

from captcha_bot import DIGIT_IN_WRITING, BUTTON_PREDICATE
from captcha_bot.dispatcher import dp, keyboard
from captcha_bot.services import *


@dp.message_handler(content_types=['left_chat_member'])
async def handler_left_chat_member(message):
    await bot.delete_message(message.chat.id, message.message_id)


@dp.message_handler()
@dp.edited_message_handler()
async def handler_check_message(message):
    if not await check_chats(message):
        return

    if message.from_user.id in doubtful_users:
        forwarded = bool(getattr(message, "forward_date"))
        with_links = False

        for entity in message.entities:
            if entity.type in ['url', 'text_link', 'mention']:
                with_links = True

        if forwarded or with_links:
            await bot.restrict_chat_member(
                chat_id=message.chat.id,
                user_id=message.from_user.id,
                permissions=OnlyReadPermissions,
                until_date=until_date()
            )

            await bot.delete_message(message.chat.id, message.message_id)


@dp.message_handler(content_types=['new_chat_members'])
async def handler_new_member(message):
    if not await check_chats(message):
        return

    number_captcha = str(randint(0, 5))
    number_captcha_in_writing = DIGIT_IN_WRITING[number_captcha]

    text = SPEECHES['greeting with riddle'](
        name=message.new_chat_members[0].first_name,
        number=number_captcha_in_writing
    )

    current_user = int(message.new_chat_members[0].id)
    doubtful_users[current_user] = False, str(datetime.now()), number_captcha

    test_message = await message.answer(text=text, reply_markup=keyboard)

    await deferred_verification(
        message.chat.id,
        test_message.message_id, current_user
    )

    await bot.delete_message(message.chat.id, message.message_id)


@dp.callback_query_handler(Text(startswith=BUTTON_PREDICATE))
async def handler_process_callback(callback_query):
    current_user = callback_query.from_user.id
    button = callback_query.data.split(BUTTON_PREDICATE[-1])[1]

    if current_user not in doubtful_users:
        await bot.answer_callback_query(callback_query.id, SPEECHES['not you'])
        return

    if doubtful_users[current_user].captcha == button:
        await bot.answer_callback_query(callback_query.id, SPEECHES['right'])
        del doubtful_users[current_user]
        await bot.delete_message(
            callback_query.message.chat.id,
            callback_query.message.message_id
        )
    else:
        await bot.answer_callback_query(
            callback_query.id,
            SPEECHES['not right']
        )

        await bot.restrict_chat_member(
            chat_id=callback_query.message.chat.id,
            user_id=current_user,
            permissions=OnlyReadPermissions,
            until_date=until_date()
        )
