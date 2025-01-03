from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def language_selection_keyboard() -> InlineKeyboardMarkup:
    """
    Til tanlash uchun inline klaviatura.
    """
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="🇰🇿 Қазақша", callback_data="lang_kz"),
        InlineKeyboardButton(text="🇷🇺 Русский", callback_data="lang_ru")]
    ])


def cancel_order_keyboard(language: str) -> InlineKeyboardMarkup:
    """
    Buyurtmani bekor qilish uchun inline klaviatura.
    """
    if language == "kz":
        return InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text="❌ Бекор қилиш", callback_data="cancel_order")]
        ])
    else:
        return InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text="❌ Бекор қилиш", callback_data="cancel_order")]
        ])