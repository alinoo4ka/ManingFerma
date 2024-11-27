import os
from pyrogram import Client, filters
from utils import start_handler

API_ID = int(os.environ.get('20045757', ''))
API_HASH = os.environ.get('7d3ea0c0d4725498789bd51a9ee02421', '')
BOT_TOKEN = os.environ.get('6954388145:AAHx9TnuzOmw3Ae4RE4EHPPEMUzD1Pgz5kY', '')


app = Client(
    session_name="DJwjndk",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

app.add_handler(start_handler)

print("Бот запущен!")
app.run()
