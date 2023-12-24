from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command

from keyboards.start import start_botton

router = Router()


@router.message(Command("start"))
async def cmd_start(message: Message):
    await message.answer(
        "Разработчики: \n{<} Студенты фокультета программирования {<}\n\nЯзыкин Артем \nИлья Конищук \nТретьяков Андрей")
    await message.answer("Привет, я бот-помощник от факультета программирования", reply_markup=start_botton)




