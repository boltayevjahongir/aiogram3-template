from aiogram import Router
from aiogram.types import Message

router: Router = Router()

@router.message()  # Barcha xabarlarni qayta ishlaydi
async def echo_handler(message: Message):
    """
    Foydalanuvchining barcha xabarlariga javob qaytaruvchi handler.
    """
    answer_text = f"📝 Қолданба:\n\nБотты қолдану үшін төмендегі 🔠 кнопкадардан пайдаланыңыз немесе...\n\n👉 /start - МӘЗІР\n👉 /taxi - 🚕 Такси шақыру\n👉 /partner - 🚖 Такси болу"
    await message.answer(answer_text)
