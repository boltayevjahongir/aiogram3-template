from aiogram import Bot
from aiogram.types import BotCommand

async def set_bot_commands(bot: Bot):
    """
    Telegram bot uchun komandalar ro'yxatini o'rnatadi.
    """
    commands = [
        BotCommand(command="/start", description="Басынан бастау 👈 бас"),
        BotCommand(command="/taxi", description="TAXI ШАҚЫРУ 👈 бас"),
    ]
    await bot.set_my_commands(commands)
