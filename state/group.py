from aiogram.filters.state import State, StatesGroup


class GroupState(StatesGroup):
    start = State()
    choosing_group = State()
    chosen_group = State()