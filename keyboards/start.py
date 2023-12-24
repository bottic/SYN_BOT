from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

start_botton = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(
            text='Ввести группу'
        )
    ]
], resize_keyboard=True, one_time_keyboard=True, input_field_placeholder='Для продолжения нажмите на кнопку ниже')