from aiogram.filters.state import State, StatesGroup


class GroupState(StatesGroup):
    choosing_group = State()
    chosen_group = State()