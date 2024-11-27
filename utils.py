from pyrogram import filters
from pyrogram.handlers import MessageHandler

def start(client, message):
    message.reply_text('добро пожаловать в первый, наполненный багов бот котрый вряьли комуто будет нужен')

start_handler = MessageHandler(start, filters.command("start"))
