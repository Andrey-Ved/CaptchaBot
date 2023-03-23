from aiogram import types

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

SPEECHES = {'wrong chat id': 'брать чужих ботов без спроса очень не хорошо',
            'not you': 'Не тебя проверяю',
            'right': 'правильно',
            'not right': 'неправильно, я тебя баню',
            'greeting with riddle': (lambda name, number:
                                     f'Привет, {name}! Это анти-спам проверка. Если ты не бот, ' +
                                     f'нажми в течение {TIME_FOR_TEST} сек. кнопку c цифрой {number}')
            }
