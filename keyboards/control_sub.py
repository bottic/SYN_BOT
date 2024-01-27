from aiogram import types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder


def add_sub(user_id):
    kb = InlineKeyboardBuilder()
    kb.button(text='✅ Подписаться на рассылку', callback_data=f'edit_sub_{user_id}')
    kb.adjust(1)
    return kb.as_markup()

def del_sub(user_id):
    kb = InlineKeyboardBuilder()
    kb.button(text='Отписаться от рассылки', callback_data=f'edit_sub_{user_id}')
    kb.adjust(1)
    return kb.as_markup()