from aiogram import Router, F
from aiogram.types import Message
from src.keyboards.inline_keyboards import language_selection_keyboard, cancel_order_keyboard
from src.keyboards.keyboards import cancel_keyboard, main_menu_keyboard, number_peoples_keyboard, summa_keyboard, \
    tel_nomer_keyboard, unfinished_keyboard, edit_order_keyboard, edit_people_keyboard, edit_summa_keyboard, \
    edit_tel_nomer_keyboard
from aiogram.fsm.context import FSMContext

from src.states.states import TaxiState
router: Router = Router()
lang = 'kz'
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
async def call_taxi_handler(message: Message, state: FSMContext):
    """
    Foydalanuvchi "🚕 Вызвать такси" yoki "🚕 Такси шақыру" tugmasini bosganda.
    """
    answer_text = "Шығатын мекен-жайыңыз" if message.text == CALL_TAXI_BUTTON[0] else "Откуда выезжаете?"
    cancel_k = cancel_keyboard(language=lang)
    await state.set_state("TaxiState:Location")

    await message.answer(answer_text, reply_markup=cancel_k)


CANCEL_BUTTON = ["🔙 Қайту (артқа)", "🔙 Назад"]

@router.message(lambda message: message.text in CANCEL_BUTTON)
async def cancel_handler(message: Message, state: FSMContext):
    """
    Foydalanuvchi "🔙 Қайту (артқа)" yoki "🔙 Назад" tugmasini bosganda.
    """
    await state.clear()
    await message.answer("Здравствуйте! Как я могу вам помочь?", reply_markup=main_menu_keyboard(lang))


@router.message(TaxiState.Location)
async def start_taxi_order_l(message: Message, state: FSMContext):
    """
    Foydalanuvchi taksi buyurtma holatida "Boshlash" tugmasini bosganda.
    """
    await state.update_data(location=message.text)
    answer_text = "Баратын мекен-жайыңыз?" if lang == 'kz' else "Куда едете?"
    cancel_k = cancel_keyboard(language=lang)
    await state.set_state("TaxiState:Destination")

    await message.answer(answer_text, reply_markup=cancel_k)


@router.message(TaxiState.Destination)
async def start_taxi_order_d(message: Message, state: FSMContext):
    """
    Foydalanuvchi taksi buyurtma holatida "Boshlash" tugmasini bosganda.
    """
    await state.update_data(destination=message.text)
    answer_text = "Неше адам отырасыздар?" if lang == 'kz' else "Сколько человек вы будете?"
    number_peoples = number_peoples_keyboard(language=lang)
    await state.set_state("TaxiState:Number_People")

    await message.answer(answer_text, reply_markup=number_peoples)


@router.message(TaxiState.Number_People)
async def start_taxi_order_n(message: Message, state: FSMContext):
    """
    Foydalanuvchi taksi buyurtma holatida "Boshlash" tugmasini bosganda.
    """
    msg = message.text
    if msg not in ["1", "2", "3", "4"]:
        answer_text = "Төменде берілген түймелерді ғана пайдаланыңыз!" if lang == 'kz' else "Пожалуйста! Используйте только ниже предоставленные кнопки!"
        return await message.answer(answer_text)

    await state.update_data(number_people=message.text)
    answer_text = "Ұсынатын бағаңыз (₸)? Бағаны сан ретінде төменде жазсаңыз болады." if lang == 'kz' else "Введите цену заказа"
    summa = summa_keyboard(language=lang)
    await state.set_state("TaxiState:Summa")

    await message.answer(answer_text, reply_markup=summa)

@router.message(TaxiState.Summa)
async def start_taxi_order_s(message: Message, state: FSMContext):
    """
    Foydalanuvchi taksi buyurtma holatida "Boshlash" tugmasini bosganda.
    """
    msg = message.text
    if not msg.isdigit():
        answer_text = "Бағаны сан ретінде көрсету қажет!" if lang == 'kz' else "Некорректная цена! Пожалуйста, используйте только числа!"
        return await message.answer(answer_text)

    await state.update_data(summa=message.text)
    answer_text = "Телефон номеріңіз?" if lang == 'kz' else "Введите ваш номер телефона"
    cancel_k = tel_nomer_keyboard(language=lang)
    await state.set_state("TaxiState:Tel_Nomer")

    await message.answer(answer_text, reply_markup=cancel_k)


@router.message(TaxiState.Tel_Nomer)
async def start_taxi_order_t(message: Message, state: FSMContext):
    """
    Foydalanuvchi taksi buyurtma holatida "Boshlash" tugmasini bosganda.
    """
    if message.contact:
        keyboard = unfinished_keyboard(lang)
        await state.update_data(tel_nomer=message.contact.phone_number)
        await state.set_state("TaxiState:UnFinished")
        location = (await state.get_data()).get("location")
        destination = (await state.get_data()).get("destination")
        number_people = (await state.get_data()).get("number_people")
        summa = (await state.get_data()).get("summa")
        tel_nomer = (await state.get_data()).get("tel_nomer")
        answer_kz = f"Тапсырысты жіберу үшін растау қажет\n\n<b>Қайдан</b>: {location}\n<b>Қайда</b>: {destination}\n<b>Адам саны</b>: {number_people}\n<b>Бағасы:</b>: {summa}₸\n<b>Телефон</b>: {tel_nomer}\n\nТапсырысты растау үшін - ✅ Тапсырысты жіберу батырмасын таңдау қажет"
        answer_ru = f"Требуется подтверждение чтобы продолжить\n\n<b>Откуда</b>: {location}\n<b>Куда</b>: {destination}\n<b>Количество пассажиров:</b>: {number_people}\n<b>Цена:</b>: {summa}₸\n<b>Номер телефона</b>: {tel_nomer}\n\nДля подтверждения заказа необходимо нажать на кнопку - ✅ Отправить заказ"
        if lang == 'kz':
            await message.answer(answer_kz, reply_markup=keyboard, parse_mode="HTML")
        else:
            await message.answer(answer_ru, reply_markup=keyboard, parse_mode="HTML")
    else:
        answer_text = "Телефон форматы қате" if lang == 'kz' else "Неверный формат номера телефона!"
        return await message.answer(answer_text)


CONFIRM_ORDER_BTN = ["✅ Тапсырысты жіберу", "✅ Отправить заказ"]
@router.message(TaxiState.UnFinished, lambda message: message.text in CONFIRM_ORDER_BTN)
async def confirm_handler_uf(message: Message, state: FSMContext):
    """
        ✅ Тапсырысты жіберу
    """
    answer_ru = """Дождитесь ответа\n\nОбработка заказа...\n\n- Водитель свяжется с вами\n\nTelegram, Благодарим вас за использования сервиса: <b>ZAISAN TAXI!</b>"""
    answer_kz = """Жауапты күтіңіз\n\nТапсырыс өңделуде...\n\n- Жүргізуші сізге хабарласатын болады\n\nTelegram, <b>ZAISAN TAXI</b> сервисін қолданғаныңызға Рахмет!"""
    await state.set_state("TaxiState:Finish")

    if lang == 'kz':
        await message.answer(answer_kz, reply_markup=cancel_order_keyboard(lang), parse_mode='HTML')
        await message.answer('🚖')

    else:
        await message.answer(answer_ru, reply_markup=cancel_order_keyboard(lang), parse_mode='HTML')
        await message.answer('🚖')

EDIT_ORDER_BTN = ["🖊 Өзгеріс еңгізу", "🖊 Редактировать заказ"]
@router.message(TaxiState.UnFinished, lambda message: message.text in EDIT_ORDER_BTN)
async def edit_handler_uf(message: Message, state: FSMContext):
    """
        🖊 Өзгеріс еңгізу
    """
    answer_text = "Өзгерту үшін қажетті ұяшықты таңдаңыз" if lang == 'kz' else "Выберите пункт, которую вы хотите изменить"
    await message.answer(answer_text, reply_markup=edit_order_keyboard(language=lang))





EDIT_ORDER_BTNS = ["🌍 Шығатын мекенжай", "🌍 Баратын мекенжай", "👥 Адам саны", "💰 Жол ақысы", "📱 Телефон номер", "🌍 Место вызова", "🌍 Место назначения (прибытия)", "👥 Количество пассажиров", "💰 Цена заказа", "📱 Номер телефона"]
@router.message(TaxiState.UnFinished, lambda message: message.text in EDIT_ORDER_BTNS)
async def edit_order_btn(message: Message, state: FSMContext):
    """
        🌍 Шығатын мекенжай
    """
    if message.text == EDIT_ORDER_BTNS[0]:
        answer_text = "Шығатын мекен-жайыңыз" if lang == 'kz' else "Откуда выезжаете?"
        await state.set_state("TaxiState:Edit_Location")
        await message.answer(answer_text)
    elif message.text == EDIT_ORDER_BTNS[1]:
        answer_text = "Баратын мекен-жайыңыз?" if lang == 'kz' else "Куда едете?"
        await state.set_state("TaxiState:Edit_Destination")
        await message.answer(answer_text)
    elif message.text == EDIT_ORDER_BTNS[2]:
        answer_text = "Неше адам отырасыздар?" if lang == 'kz' else "Сколько человек вы будете?"
        await state.set_state("TaxiState:Edit_Number_People")
        await message.answer(answer_text,  reply_markup=edit_people_keyboard())
    elif message.text == EDIT_ORDER_BTNS[3]:
        answer_text = "Ұсынатын бағаңыз (₸)? Бағаны сан ретінде төменде жазсаңыз болады." if lang == 'kz' else "Введите цену заказа"
        await state.set_state("TaxiState:Edit_Summa")
        await message.answer(answer_text, reply_markup=edit_summa_keyboard())
    elif message.text == EDIT_ORDER_BTNS[4]:
        answer_text = "Телефон номеріңіз?" if lang == 'kz' else "Введите ваш номер телефона"
        await state.set_state("TaxiState:Edit_Tel_Nomer")
        await message.answer(answer_text, reply_markup=edit_tel_nomer_keyboard(language=lang))
    else:
        await message.answer("Тек қажетті ұяшықтарды таңдаңыз!")


@router.message(TaxiState.Edit_Location)
async def edit_order(message: Message, state: FSMContext):
    """
        🌍 Шығатын мекенжай
    """
    await state.update_data(location=message.text)
    keyboard = unfinished_keyboard(lang)
    location = (await state.get_data()).get("location")
    destination = (await state.get_data()).get("destination")
    number_people = (await state.get_data()).get("number_people")
    summa = (await state.get_data()).get("summa")
    tel_nomer = (await state.get_data()).get("tel_nomer")
    answer_kz = f"Тапсырысты жіберу үшін растау қажет\n\n<b>Қайдан</b>: {location}\n<b>Қайда</b>: {destination}\n<b>Адам саны</b>: {number_people}\n<b>Бағасы:</b>: {summa}₸\n<b>Телефон</b>: {tel_nomer}\n\nТапсырысты растау үшін - ✅ Тапсырысты жіберу батырмасын таңдау қажет"
    answer_ru = f"Требуется подтверждение чтобы продолжить\n\n<b>Откуда</b>: {location}\n<b>Куда</b>: {destination}\n<b>Количество пассажиров:</b>: {number_people}\n<b>Цена:</b>: {summa}₸\n<b>Номер телефона</b>: {tel_nomer}\n\nДля подтверждения заказа необходимо нажать на кнопку - ✅ Отправить заказ"
    await state.set_state("TaxiState:UnFinished")
    if lang == 'kz':
        await message.answer(answer_kz, reply_markup=keyboard, parse_mode="HTML")
    else:
        await message.answer(answer_ru, reply_markup=keyboard, parse_mode="HTML")


@router.message(TaxiState.Edit_Destination)
async def edit_order_d(message: Message, state: FSMContext):
    """
        🌍 Баратын мекенжай
    """
    await state.update_data(destination=message.text)
    keyboard = unfinished_keyboard(lang)
    location = (await state.get_data()).get("location")
    destination = (await state.get_data()).get("destination")
    number_people = (await state.get_data()).get("number_people")
    summa = (await state.get_data()).get("summa")
    tel_nomer = (await state.get_data()).get("tel_nomer")
    answer_kz = f"Тапсырысты жіберу үшін растау қажет\n\n<b>Қайдан</b>: {location}\n<b>Қайда</b>: {destination}\n<b>Адам саны</b>: {number_people}\n<b>Бағасы:</b>: {summa}₸\n<b>Телефон</b>: {tel_nomer}\n\nТапсырысты растау үшін - ✅ Тапсырысты жіберу батырмасын таңдау қажет"
    answer_ru = f"Требуется подтверждение чтобы продолжить\n\n<b>Откуда</b>: {location}\n<b>Куда</b>: {destination}\n<b>Количество пассажиров:</b>: {number_people}\n<b>Цена:</b>: {summa}₸\n<b>Номер телефона</b>: {tel_nomer}\n\nДля подтверждения заказа необходимо нажать на кнопку - ✅ Отправить заказ"
    await state.set_state("TaxiState:UnFinished")
    if lang == 'kz':
        await message.answer(answer_kz, reply_markup=keyboard, parse_mode="HTML")
    else:
        await message.answer(answer_ru, reply_markup=keyboard, parse_mode="HTML")


@router.message(TaxiState.Edit_Number_People)
async def edit_order_n(message: Message, state: FSMContext):
    """
        👥 Адам саны
    """
    msg = message.text
    if msg not in ["1", "2", "3", "4"]:
        answer_text = "Төменде берілген түймелерді ғана пайдаланыңыз!" if lang == 'kz' else "Пожалуйста! Используйте только ниже предоставленные кнопки!"
        return await message.answer(answer_text)

    await state.update_data(number_people=message.text)
    keyboard = unfinished_keyboard(lang)
    location = (await state.get_data()).get("location")
    destination = (await state.get_data()).get("destination")
    number_people = (await state.get_data()).get("number_people")
    summa = (await state.get_data()).get("summa")
    tel_nomer = (await state.get_data()).get("tel_nomer")
    answer_kz = f"Тапсырысты жіберу үшін растау қажет\n\n<b>Қайдан</b>: {location}\n<b>Қайда</b>: {destination}\n<b>Адам саны</b>: {number_people}\n<b>Бағасы:</b>: {summa}₸\n<b>Телефон</b>: {tel_nomer}\n\nТапсырысты растау үшін - ✅ Тапсырысты жіберу батырмасын таңдау қажет"
    answer_ru = f"Требуется подтверждение чтобы продолжить\n\n<b>Откуда</b>: {location}\n<b>Куда</b>: {destination}\n<b>Количество пассажиров:</b>: {number_people}\n<b>Цена:</b>: {summa}₸\n<b>Номер телефона</b>: {tel_nomer}\n\nДля подтверждения заказа необходимо нажать на кнопку - ✅ Отправить заказ"
    await state.set_state("TaxiState:UnFinished")
    if lang == 'kz':
        await message.answer(answer_kz, reply_markup=keyboard, parse_mode="HTML")
    else:
        await message.answer(answer_ru, reply_markup=keyboard, parse_mode="HTML")

@router.message(TaxiState.Edit_Summa)
async def edit_order_s(message: Message, state: FSMContext):
    """
        💰 Жол ақысы
    """
    msg = message.text
    if not msg.isdigit():
        answer_text = "Бағаны сан ретінде көрсету қажет!" if lang == 'kz' else "Некорректная цена! Пожалуйста, используйте только числа!"
        return await message.answer(answer_text)

    await state.update_data(summa=message.text)
    keyboard = unfinished_keyboard(lang)
    location = (await state.get_data()).get("location")
    destination = (await state.get_data()).get("destination")
    number_people = (await state.get_data()).get("number_people")
    summa = (await state.get_data()).get("summa")
    tel_nomer = (await state.get_data()).get("tel_nomer")
    answer_kz = f"Тапсырысты жіберу үшін растау қажет\n\n<b>Қайдан</b>: {location}\n<b>Қайда</b>: {destination}\n<b>Адам саны</b>: {number_people}\n<b>Бағасы:</b>: {summa}₸\n<b>Телефон</b>: {tel_nomer}\n\nТапсырысты растау үшін - ✅ Тапсырысты жіберу батырмасын таңдау қажет"
    answer_ru = f"Требуется подтверждение чтобы продолжить\n\n<b>Откуда</b>: {location}\n<b>Куда</b>: {destination}\n<b>Количество пассажиров:</b>: {number_people}\n<b>Цена:</b>: {summa}₸\n<b>Номер тел��фона</b>: {tel_nomer}\n\nДля подтверждения заказа необходимо нажать на кнопку - ✅ Отправить заказ"
    await state.set_state("TaxiState:UnFinished")
    if lang == 'kz':
        await message.answer(answer_kz, reply_markup=keyboard, parse_mode="HTML")
    else:
        await message.answer(answer_ru, reply_markup=keyboard, parse_mode="HTML")

@router.message(TaxiState.Edit_Tel_Nomer)
async def edit_order_t(message: Message, state: FSMContext):
    """
        📱 Телефон номер
    """
    if message.contact:
        keyboard = unfinished_keyboard(lang)
        await state.update_data(tel_nomer=message.contact.phone_number)
        location = (await state.get_data()).get("location")
        destination = (await state.get_data()).get("destination")
        number_people = (await state.get_data()).get("number_people")
        summa = (await state.get_data()).get("summa")
        tel_nomer = (await state.get_data()).get("tel_nomer")
        answer_kz = f"Тапсырысты жіберу үшін растау қажет\n\n<b>Қайдан</b>: {location}\n<b>Қайда</b>: {destination}\n<b>Адам саны</b>: {number_people}\n<b>Бағасы:</b>: {summa}₸\n<b>Телефон</b>: {tel_nomer}\n\nТапсырысты растау үшін - ✅ Тапсырысты жіберу батырмасын таңдау қажет"
        answer_ru = f"Требуется подтверждение чтобы продолжить\n\n<b>Откуда</b>: {location}\n<b>Куда</b>: {destination}\n<b>Количество пассажиров:</b>: {number_people}\n<b>Цена:</b>: {summa}₸\n<b>Номер телефона</b>: {tel_nomer}\n\nДля подтверждения заказа необходимо нажать на кнопку - ✅ Отправить заказ"
        await state.set_state("TaxiState:UnFinished")
        if lang == 'kz':
            await message.answer(answer_kz, reply_markup=keyboard, parse_mode="HTML")
        else:
            await message.answer(answer_ru, reply_markup=keyboard, parse_mode="HTML")
    else:
        answer_text = "Телефон форматы қате" if lang == 'kz' else "Неверный формат номера телефона!"
        return await message.answer(answer_text)




CANCEL_ORDER_BTN = ["❌ Тапсырысты жою", "❌ Отменить заказ"]
@router.message(TaxiState.UnFinished, lambda message: message.text in CANCEL_ORDER_BTN)
async def cancel_handler_uf(message: Message, state: FSMContext):
    """
        ❌ Тапсырысты жою
    """
    await state.clear()
    await message.answer("🚖", reply_markup=main_menu_keyboard(lang))




