from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from aiogram import Router, F
from aiogram.filters import Command, StateFilter
from config import DATABASE_NAME
from keyboards.start import start_botton
from utils.database import Database

from state.group import GroupState
from keyboards.button import schedule

router = Router()


GROUPS = ['дбо-101рпо', 'дбо-102рпо', 'дбо-161рпо', 'дбп-101рив']


@router.message(F.text.lower() == "ввести группу")
async def hand_start_choose(message: Message, state:FSMContext):
    await message.answer(f'Введите свою группу\nФормат: ДБО-101рпо')
    await state.set_state(GroupState.choosing_group)


@router.message(Command("set_group"))
async def hand_set_group(message: Message, state:FSMContext):
    await message.answer(f'Введите свою группу\nФормат: ДБО-101рпо')
    await state.set_state(GroupState.choosing_group)


@router.message(GroupState.choosing_group, F.text.lower().in_(GROUPS))
async def hand_end_choose(message:Message, state:FSMContext):
    db = Database(DATABASE_NAME)
    group = message.text.lower()
    user_tg_id = message.from_user.id
    user_data = db.select_user(user_tg_id)
    users_chat_id = message.chat.id
    if user_data is None:
        db.add_user(user_tg_id, group, users_chat_id)
    else:
        db.change_user(group, user_tg_id)
    await state.set_state(GroupState.chosen_group)
    await message.answer("Вы успешно ввели группу\nЧто бы вы хотели узнать?", reply_markup=schedule)


@router.message(GroupState.choosing_group)
async def hand_group_chosen_incorrectly(message: Message):
    await message.answer(
        text="Такой группы не существует, либо она будет добавлена в следующих обновлениях;)"
    )


@router.message(StateFilter(None))
async def hand_group_not_chosen_(message: Message):
    await message.answer(
        text="Пожалуйста, нажмите на кнопку, а затем введите группу", reply_markup=start_botton
    )