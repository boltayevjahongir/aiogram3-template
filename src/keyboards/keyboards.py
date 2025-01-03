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


def number_peoples_keyboard(language: str) -> ReplyKeyboardMarkup:
    text = {
        "kz": "🔙 Қайту (артқа)",
        "ru": "🔙 Назад"
    }.get(language, "🔙 Назад")
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="1"),
             KeyboardButton(text="2"),
             KeyboardButton(text="3"),
             KeyboardButton(text="4")],
            [KeyboardButton(text=text)]

        ],
        resize_keyboard=True
    )


def summa_keyboard(language: str) -> ReplyKeyboardMarkup:
    text = {
        "kz": "🔙 Қайту (артқа)",
        "ru": "🔙 Назад"
    }.get(language, "🔙 Назад")
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="250"),
             KeyboardButton(text="300"),
             KeyboardButton(text="350")],
             [KeyboardButton(text="400"),
             KeyboardButton(text="450"),
             KeyboardButton(text="500")],
             [KeyboardButton(text="550"),
             KeyboardButton(text="600"),
             KeyboardButton(text="700")],
             [KeyboardButton(text="800"),
             KeyboardButton(text="900"),
             KeyboardButton(text="1000")],
             [KeyboardButton(text="1500"),
             KeyboardButton(text="2000"),
             KeyboardButton(text="5000")],
            [KeyboardButton(text=text)]

        ],
        resize_keyboard=True
    )

def tel_nomer_keyboard(language: str) -> ReplyKeyboardMarkup:
    text = {
        "kz": "🔙 Қайту (артқа)",
        "ru": "🔙 Назад"
    }.get(language, "🔙 Назад")
    text_tel = {
        "kz": "📱 Телефон номер жіберу",
        "ru": "📱 Отправить номер телефона"
    }.get(language, "📱 Отправить номер телефона")

    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text=text_tel, request_contact=True)],
            [KeyboardButton(text=text)]
        ],
        resize_keyboard=True
    )

def unfinished_keyboard(language: str) -> ReplyKeyboardMarkup:
    btn_ru = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="✅ Отправить заказ")],
            [KeyboardButton(text="🖊 Редактировать заказ")],
            [KeyboardButton(text="❌ Отменить заказ")]
        ],
        resize_keyboard=True
    )

    btn_kz = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="✅ Тапсырысты жіберу")],
            [KeyboardButton(text="🖊 Өзгеріс еңгізу")],
            [KeyboardButton(text="❌ Тапсырысты жою")]
        ],
        resize_keyboard=True
    )

    if language == 'kz':
        return btn_kz
    else:
        return btn_ru


def edit_order_keyboard(language: str) -> ReplyKeyboardMarkup:
    if language == 'kz':
        return ReplyKeyboardMarkup(
            keyboard=[
                [KeyboardButton(text="🌍 Шығатын мекенжай")],
                [KeyboardButton(text="🌍 Баратын мекенжай")],
                [KeyboardButton(text="👥 Адам саны")],
                [KeyboardButton(text="💰 Жол ақысы")],
                [KeyboardButton(text="📱 Телефон номер")],
            ],
            resize_keyboard=True
        )
    else:
        return ReplyKeyboardMarkup(
            keyboard=[
                [KeyboardButton(text="🌍 Место вызова")],
                [KeyboardButton(text="🌍 Место назначения (прибытия)")],
                [KeyboardButton(text="👥 Количество пассажиров")],
                [KeyboardButton(text="💰 Цена заказа")],
                [KeyboardButton(text="📱 Номер телефона")],
            ],
            resize_keyboard=True
        )

def edit_people_keyboard() -> ReplyKeyboardMarkup:
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="1"),
             KeyboardButton(text="2"),
             KeyboardButton(text="3"),
             KeyboardButton(text="4")],
        ],
        resize_keyboard=True
    )

def edit_summa_keyboard() -> ReplyKeyboardMarkup:
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="250"),
             KeyboardButton(text="300"),
             KeyboardButton(text="350")],
             [KeyboardButton(text="400"),
             KeyboardButton(text="450"),
             KeyboardButton(text="500")],
             [KeyboardButton(text="550"),
             KeyboardButton(text="600"),
             KeyboardButton(text="700")],
             [KeyboardButton(text="800"),
             KeyboardButton(text="900"),
             KeyboardButton(text="1000")],
             [KeyboardButton(text="1500"),
             KeyboardButton(text="2000"),
             KeyboardButton(text="5000")],
        ],
        resize_keyboard=True
    )

def edit_tel_nomer_keyboard(language: str) -> ReplyKeyboardMarkup:
    if language == 'kz':
        return ReplyKeyboardMarkup(
            keyboard=[
                [KeyboardButton(text="📱 Телефон номер жіберу", request_contact=True)],
            ],
            resize_keyboard=True
        )
    else:
        return ReplyKeyboardMarkup(
            keyboard=[
                [KeyboardButton(text="📱 Отправить номер телефона", request_contact=True)],
            ],
            resize_keyboard=True
        )
matn = """
✅ Отправить заказ

🖊 Редактировать заказ
Выберите пункт, которую вы хотите изменить

🌍 Место назначения (прибытия)
👥 Количество пассажиров


💰 Цена заказа
Введите цену заказа  (tugmalar cancel chiqmasdan)


📱 Номер телефона
Введите ваш номер телефона

Неверный формат номера телефона!  nomer bo'lmasa 



❌ Отменить заказ
🚖

✅ Тапсырысты жіберу


🖊 Өзгеріс еңгізу
Өзгерту үшін қажетті ұяшықты таңдаңыз


🌍 Шығатын мекенжай
Шығатын мекен-жайыңыз


🌍 Баратын мекенжай
Баратын мекен-жайыңыз?

👥 Адам саны
Неше адам отырасыздар?

💰 Жол ақысы
Ұсынатын бағаңыз (₸)? Бағаны сан ретінде төменде жазсаңыз болады.

📱 Телефон номер
Телефон номеріңіз?

Телефон форматы қате    -  tel bo'masa

❌ Тапсырысты жою
🚖
"""