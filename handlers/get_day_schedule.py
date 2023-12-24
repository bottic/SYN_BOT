from aiogram.types import Message

from aiogram import Router, F

from config import DATABASE_NAME
from keyboards.button import schedule
from utils.database import Database

from data.main_data import get_day_schedule

from state.group import GroupState

router = Router()


@router.message(F.text.lower() == "📆расписание на сегодняшний день", GroupState.chosen_group)
async def set_group(message: Message):
    db = Database(DATABASE_NAME)
    user = db.select_user(message.from_user.id)
    grop = user[2]
    s = get_day_schedule(grop)
    if s == '':
        await message.answer("Сегодняшние пары уже закончились")
    else:
        await message.answer("Вот ваше расписание:", reply_markup=schedule)
        await message.answer(s)

