from aiogram.types import Message

from aiogram import Router, F

from config import DATABASE_NAME
from keyboards.button import schedule
from utils.database import Database

from data.main_data import get_week_schedule

from state.group import GroupState

router = Router()


@router.message(F.text.lower() == "📆расписание на неделю", GroupState.chosen_group)
async def hand_set_group(message: Message):
    db = Database(DATABASE_NAME)
    user = db.select_user(message.from_user.id)
    grop = user[2]
    s = get_week_schedule(grop)
    if s == '<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<\n':
        await message.answer("На этой неделе у вас нет пар;))")
    else:
        await message.answer("Вот ваше расписание:", reply_markup=schedule)
        await message.answer(s)

