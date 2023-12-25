from aiogram import Bot
from aiogram.types import BotCommand, BotCommandScopeDefault


async def set_commands(bot: Bot):
    commands = [
        BotCommand(
            command='start',
            description='Запуск бота'
        ),
        BotCommand(
            command='info',
            description='Помощь в работе с ботом'
        ),
        BotCommand(
            command='set_group',
            description='Ввести группу'
        )
    ]
    await bot.set_my_commands(commands, BotCommandScopeDefault())
