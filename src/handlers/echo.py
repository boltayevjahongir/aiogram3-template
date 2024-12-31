from aiogram import Router
from aiogram.types import Message

router: Router = Router()

@router.message()  # Barcha xabarlarni qayta ishlaydi
async def echo_handler(message: Message):
    """
    Foydalanuvchining barcha xabarlariga javob qaytaruvchi handler.
    """
    await message.reply(f"Siz yuborgan xabar: {message.text}")
