from aiogram import Router
from aiogram.types import CallbackQuery

from src.keyboards.keyboards import main_menu_keyboard

router: Router = Router()

@router.callback_query()
async def callback_handler(callback: CallbackQuery):
    """
    Inline tugma bosilganda:
    1. Tanlangan tilni saqlash.
    2. Foydalanuvchiga tasdiq va salomlashish xabarini yuborish.
    """

    if callback.data == "lang_ru":
        await callback.message.delete()
        await callback.message.answer("🇷🇺 Язык успешно выбран!")
        await callback.message.answer("Здравствуйте! Как я могу вам помочь?", reply_markup=main_menu_keyboard('ru'))
    elif callback.data == "lang_kz":
        await callback.message.delete()
        await callback.message.answer("🇰🇿 Тіл сәтті таңдалды!")
        await callback.message.answer("Салем! Сізге қандай қызмет көрсете аламын?", reply_markup=main_menu_keyboard('kz'))

    await callback.answer()  # Callbackni tugatish
