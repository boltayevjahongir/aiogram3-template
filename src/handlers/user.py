from aiogram import Router
from aiogram.types import Message
from src.keyboards.inline_keyboards import language_selection_keyboard
from src.keyboards.keyboards import cancel_keyboard, main_menu_keyboard

router: Router = Router()

LANGUAGE_CHANGE_TEXTS = ["💱 Тілді өзгерту", "💱 Изменить язык"]

@router.message(lambda message: message.text in LANGUAGE_CHANGE_TEXTS)
async def change_language_handler(message: Message):
    """
    Foydalanuvchi "💱 Тілді өзгерту" yoki "💱 Изменить язык" tugmasini bosganda.
    """
    keyboard = language_selection_keyboard()
    await message.answer("Тілді таңдаңыз / Выберите язык:", reply_markup=keyboard)

CALL_TAXI_BUTTON = ["🚕 Такси шақыру", "🚕 Вызвать такси"]
@router.message(lambda message: message.text in CALL_TAXI_BUTTON)
async def call_taxi_handler(message: Message):
    """
    Foydalanuvchi "🚕 Вызвать такси" yoki "🚕 Такси шақыру" tugmasini bosganda.
    """
    answer_text = "Шығатын мекен-жайыңыз" if message.text == CALL_TAXI_BUTTON[0] else "Откуда выезжаете?"
    lang = 'kz' if message.text == CALL_TAXI_BUTTON[0] else 'ru'
    cancel_k = cancel_keyboard(language=lang)
    await message.answer(answer_text, reply_markup=cancel_k)


CANCEL_BUTTON = ["🔙 Қайту (артқа)", "🔙 Назад"]

@router.message(lambda message: message.text in CANCEL_BUTTON)
async def cancel_handler(message: Message):
    """
    Foydalanuvchi "🔙 Қайту (артқа)" yoki "🔙 Назад" tugmasini bosganda.
    """
    await message.answer("Здравствуйте! Как я могу вам помочь?", reply_markup=main_menu_keyboard('ru'))