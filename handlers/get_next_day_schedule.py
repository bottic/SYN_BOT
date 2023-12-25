from aiogram.types import Message

from aiogram import Router, F

from config import DATABASE_NAME
from keyboards.button import schedule
from utils.database import Database

from data.main_data import get_next_day_schedule

from state.group import GroupState

router = Router()


@router.message(F.text.lower() == "📆расписание на завтрашний день", GroupState.chosen_group)
async def get_next_day_schedule(message: Message):
    db = Database(DATABASE_NAME)
    user = db.select_user(message.from_user.id)
    grop = user[2]
    s = get_next_day_schedule(grop)
    print(s)
    if ')()(' in s:
        await message.answer(s.split(':')[0], reply_markup=schedule)
    else:
        await message.answer("Вот ваше расписание:", reply_markup=schedule)
        await message.answer(s, reply_markup=schedule)


