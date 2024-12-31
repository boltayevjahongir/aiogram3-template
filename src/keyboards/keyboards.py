# Create your keyboards here.
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

def main_menu_keyboard(language: str) -> ReplyKeyboardMarkup:
    """
    Asosiy menyu uchun default (oddiy) klaviatura.
    """

    main_menu_kz = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="🚕 Такси шақыру")],
            [KeyboardButton(text="📦 Жеткізу (Доставка)")],
            [KeyboardButton(text="🚖 Такси болу")],
            [KeyboardButton(text="💱 Тілді өзгерту")],
        ],
        resize_keyboard=True  # Tugmalarni ekran hajmiga moslashtirish
    )

    main_menu_ru = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="🚕 Вызвать такси")],
            [KeyboardButton(text="📦 Доставка товара")],
            [KeyboardButton(text="🚖 Стать водителем")],
            [KeyboardButton(text="💱 Изменить язык")],
        ],
        resize_keyboard=True  # Tugmalarni ekran hajmiga moslashtirish
    )

    return main_menu_kz if language == 'kz' else main_menu_ru



def cancel_keyboard(language: str) -> ReplyKeyboardMarkup:
    """
    Bekor qilish uchun klaviatura.
    :param language: Til kodi ("kz", "ru").
    """
    text = {
        "kz": "🔙 Қайту (артқа)",
        "ru": "🔙 Назад"
    }.get(language, "🔙 Назад")  # Default til ruscha
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text=text)]
        ],
        resize_keyboard=True
    )