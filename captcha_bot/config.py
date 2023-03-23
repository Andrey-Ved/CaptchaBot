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

WORKS_CHATS = {os.getenv('CHAT_ID_1'): 'chat_id_1',
               os.getenv('CHAT_ID_2'): 'chat_id_2'}

USERS_DATA_FILE = os.getenv('USERS_DATA_FILE')
