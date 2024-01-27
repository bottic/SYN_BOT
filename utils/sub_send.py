from aiogram import Bot
from config import DATABASE_NAME
from utils.database import Database


async def send_sub_cron(bot: Bot):
    db = Database(DATABASE_NAME)
    chats = db.select_all_subscribe_user()
    print(chats)
    for chat in chats:
        await bot.send_message(chat[0], f'Сообщение по рассписанию')
