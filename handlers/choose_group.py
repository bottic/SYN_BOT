from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from aiogram import Router, F
from aiogram.filters import Command, StateFilter
from config import DATABASE_NAME
from utils.database import Database

from state.group import GroupState
from keyboards.button import schedule

router = Router()


GROUPS = ['дбо-101рпо', 'дбо-102рпо', 'дбо-161рпо', 'дбп-101рив']


@router.message(F.text.lower() == "ввести группу")
async def start_choose(message: Message, state:FSMContext):
    await message.answer(f'Введите свою группу\nФормат: ДБО-101рпо')
    await state.set_state(GroupState.choosing_group)


@router.message(GroupState.choosing_group, F.text.lower().in_(GROUPS))
async def set_group(message:Message, state:FSMContext):
    db = Database(DATABASE_NAME)
    db.add_user(message.from_user.id, message.text.lower())
    await state.set_state(GroupState.chosen_group)
    await message.answer("Вы успешно ввели группу\nЧто бы вы хотели узнать?", reply_markup=schedule)


@router.message(GroupState.choosing_group)
async def group_chosen_incorrectly(message: Message):
    await message.answer(
        text="Такой группы не существует, либо она будет добавлена в следующих обновлениях;)"
    )


@router.message(StateFilter(None))
async def group_chosen_incorrectly(message: Message):
    await message.answer(
        text="Пожалуйста, нажмите на кнопку и введите группу"
    )