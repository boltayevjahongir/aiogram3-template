from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command  # Command filter'ini import qilish

from src.keyboards.inline_keyboards import language_selection_keyboard
from src.keyboards.keyboards import main_menu_keyboard

router: Router = Router()


@router.message(Command(commands=["start"]))  # "commands" o'rniga Command filter ishlatamiz
async def start_handler(message: Message):
    """
    /start komandasini qayta ishlovchi handler.
    """
    inline_keyboard = language_selection_keyboard()
    # keyboard = main_menu_keyboard('ru')

    await message.answer("Тілді таңдаңыз / Выберите язык:", reply_markup=inline_keyboard)
