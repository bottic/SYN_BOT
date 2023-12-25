from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command
from utils.database import Database
from config import DATABASE_NAME

from keyboards.start import start_botton

router = Router()


@router.message(Command("info"))
async def answer_schedule(message: Message):
    db = Database(DATABASE_NAME)
    user = db.select_user(message.from_user.id)
    grop = user[2]
    await message.answer(
        "Разработчики: \n{<} Студенты фокультета программирования {<}\n\nЯзыкин Артем \nИлья Конищук \nТретьяков Андрей")
    await message.answer(f"⚙ПАРАМЕТРЫ:\nУстановленный часовой пояс: UTC+3\nУстановленная группа: {grop}")






