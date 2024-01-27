from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command

from keyboards.start import start_botton

router = Router()


@router.message(Command("start"))
async def cmd_start(message: Message):
    await message.answer(
        "Разработчики: \n{<} Студенты фокультета программирования {<}\n\nЯзыкин Артем \nИлья Конищук \nТретьяков Андрей")
    await message.answer(f'❗️ Обращаем ваше внимание, если у вас закрытый профиль бот может работать некорректно')
    await message.answer(f"Привет, {message.from_user.first_name}, я бот-помощник от факультета программирования. "
                         f"Пожалуйста, введите группу, чтобы я мог понимать откуда вы", reply_markup=start_botton)




