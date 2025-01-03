from aiogram import Router
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery
from src.keyboards.keyboards import main_menu_keyboard
from src.states.states import TaxiState

router: Router = Router()
lang = 'ru'


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
        await callback.message.answer("Салем! Сізге қандай қызмет көрсете аламын?",
                                      reply_markup=main_menu_keyboard('kz'))

    await callback.answer()  # Callbackni tugatish


@router.callback_query(TaxiState.Finish)
async def finish_taxi_order(callback: CallbackQuery, state: FSMContext):
    """
    Taksi buyurtma tugmasini bosganda.
    """
    await state.clear()
    if lang == 'kz':
        await callback.message.answer("Telegram, сіздің тапсырысыңыз кері қайтарылды. \n\n- <b>ZAIAN TAXI</b> қызметін қолданғаныңызға рахмет!", reply_markup=main_menu_keyboard(lang), parse_mode="HTML")

    else:
        await callback.message.answer("Telegram, ваш заказ был отменен.  \n\n- - Благодарим вас за использования сервиса: <b>ZAISAN TAXI</b>", reply_markup=main_menu_keyboard(lang), parse_mode="HTML")







