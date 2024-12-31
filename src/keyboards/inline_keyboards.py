from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def language_selection_keyboard() -> InlineKeyboardMarkup:
    """
    Til tanlash uchun inline klaviatura.
    """
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="🇰🇿 Қазақша", callback_data="lang_kz"),
        InlineKeyboardButton(text="🇷🇺 Русский", callback_data="lang_ru")]
    ])
