from aiogram.types import Message, CallbackQuery

from aiogram import Router, F

from config import DATABASE_NAME
from keyboards.control_sub import add_sub, del_sub
from utils.database import Database

from data.main_data import get_day_schedule

from state.group import GroupState

router = Router()


@router.message(F.text.lower() == "📆 проверить статус рассылки", GroupState.chosen_group)
async def hand_get_status_sub(message: Message):
    db = Database(DATABASE_NAME)
    user = db.select_user(message.from_user.id)
    status_sub = user[3]
    if status_sub == 0:
        await message.answer(f"Вы не подписаны на ежедневную рассылку", reply_markup=add_sub(user[1]))
    else:
        await message.answer(f"Вы подписаны на ежедневную рассылку", reply_markup=del_sub(user[1]))


async def edit_sub(call: CallbackQuery):
    db = Database(DATABASE_NAME)
    user = db.select_user(call.data.split('_')[-1])
    if int(user[3]) == 0:
        db.change_subscribe(user[1], True)
        await call.message.edit_text("Вы подписаны на рассылку", reply_markup=del_sub(user[1]))
    else:
        db.change_subscribe(user[1], False)
        await call.message.edit_text("Вы не подписаны на рассылку", reply_markup=add_sub(user[1]))



