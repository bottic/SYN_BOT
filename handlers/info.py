from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command

from keyboards.start import start_botton

router = Router()


@router.message(Command("info"))
async def answer_schedule(message: Message):
    await message.answer(
        "Разработчики: \n{<} Студенты фокультета программирования {<}\n\nЯзыкин Артем \nИлья Конищук \nТретьяков Андрей")
    await message.answer(f"⚙ПАРАМЕТРЫ:\nУстановленный часовой пояс: UTC+3\nУстановленная группа:")






