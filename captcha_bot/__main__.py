import logging
from pathlib import Path

from aiogram.utils.executor import start_polling

from captcha_bot import USERS_DATA_FILE
from captcha_bot.handlers import *


def main():
    Path(USERS_DATA_FILE).parent.mkdir(parents=True, exist_ok=True)

    log_name = f'logs/{datetime.now().strftime("%Y-%m-%d")}.log'
    Path(log_name).parent.mkdir(parents=True, exist_ok=True)

    logging.basicConfig(
        level=logging.INFO,
        filename=log_name,
        filemode="a"
    )

    start_polling(dp, skip_updates=True)


if __name__ == '__main__':
    main()
