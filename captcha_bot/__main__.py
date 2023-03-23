import logging
from aiogram import executor
# from aiogram.utils.executor import start_webhook
from captcha_bot.handlers import *


# async def on_startup(dispatcher):
#     await bot.set_webhook(WEBHOOK_URL, drop_pending_updates=True)
#
# async def on_shutdown(dispatcher):
#     await bot.delete_webhook()


def main():
    # logging.basicConfig(level=logging.DEBUG)
    logging.basicConfig(level=logging.INFO)

    logging.info('Restart and run server.')
    logging.info(f'Local datetime: {datetime.now()}')
    logging.info(f"Moscow datetime: {datetime.now(timezone('Europe/Moscow'))}")

    # start_webhook(dispatcher=dp,
    #             webhook_path=WEBHOOK_PATH,
    #             skip_updates=True,
    #             on_startup=on_startup,
    #             on_shutdown=on_shutdown,
    #             host=WEBAPP_HOST,
    #             port=WEBAPP_PORT, )
    executor.start_polling(dp, skip_updates=True)


if __name__ == '__main__':
    main()
