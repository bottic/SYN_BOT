from aiogram import types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton




kb = [
    [types.KeyboardButton(text="📆Расписание")],
    # [types.KeyboardButton(text="👕Мерч")],
    [types.KeyboardButton(text="ℹ️Информация")],
    ]

main_kb = types.ReplyKeyboardMarkup(
    keyboard=kb,
    resize_keyboard=True,
    input_field_placeholder="Что бы вы хотели узнать?"
)
#Клавиатура для расписания
kb_schedule = [
        [types.KeyboardButton(text="📆Расписание на сегодняшний день"),
         types.KeyboardButton(text="📆Расписание на завтрашний день")],
        [types.KeyboardButton(text="📆Расписание на неделю")]
    ]

schedule = types.ReplyKeyboardMarkup(
    keyboard=kb_schedule,
    resize_keyboard=True,
    input_field_placeholder="Выберите один из пунктов"
)

#Клавиатура для выбора группы

