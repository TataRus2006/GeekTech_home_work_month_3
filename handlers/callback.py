from aiogram import types, Dispatcher
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ParseMode
from config import bot


async def quiz_2(call: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    button_call_2 = InlineKeyboardButton("NEXT", callback_data='button_call_2')
    markup.add(button_call_2)

    question = "Какая основная цель эзотерических языков программирования?"
    answers = [
        "Исследования границ возможностей разработки языков программирования",
        "Создание программ путем манипулирования визуальными объектами и эзотерическими формами",
        "Таких языков программирования не существует"
    ]
    await bot.send_poll(
        chat_id=call.message.chat.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=0,
        explanation="«Экзорцизм? нет, речь про Эзотеризм»",
        explanation_parse_mode=ParseMode.MARKDOWN_V2,
        reply_markup=markup
    )


async def quiz_3(call: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    button_call_3 = InlineKeyboardButton("NEXT", callback_data='button_call_3')
    markup.add(button_call_3)

    question = "Как называется первый в мире высокоуровневый язык программирования?"
    answers = [
        "Фортран",
        "Ада",
        "Планкалкюль"

    ]
    await bot.send_poll(
        chat_id=call.message.chat.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=2,
        explanation="«Историю надо знать»",
        explanation_parse_mode=ParseMode.MARKDOWN_V2,
        reply_markup=markup
    )


async def quiz_4(call: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    button_call_4 = InlineKeyboardButton("NEXT", callback_data='button_call_4')
    markup.add(button_call_4)

    question = "Кого называют «бабушкой Кобола»?"
    answers = [
        "Грейс Хоппер",
        "Ада Лавлейс",
        "Мэри Микер"
    ]
    await bot.send_poll(
        chat_id=call.message.chat.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=0,
        explanation="«Кобол это общий бизнес ориентированный язык "
                    "Она разработала первый компилятор для компьютерного языка программирования»",
        explanation_parse_mode=ParseMode.MARKDOWN_V2,
        reply_markup=markup
    )


async def quiz_5(call: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    button_call_5 = InlineKeyboardButton("NEXT", callback_data='button_call_5')
    markup.add(button_call_5)

    question = "Для чего Джоном Маккарти был создан язык программирования Лисп?"
    answers = [
        "Для работ по искусственному интеллекту",
        "Для управления бытовыми приборами",
        "Для реализации компьютерной модели вселенной"
    ]
    await bot.send_poll(
        chat_id=call.message.chat.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=0,
        explanation="«Джон Маккарти американский информатик, изобретатель»",
        explanation_parse_mode=ParseMode.MARKDOWN_V2,
        reply_markup=markup
    )


async def quiz_6(call: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    button_call_6 = InlineKeyboardButton("NEXT", callback_data='button_call_6')
    markup.add(button_call_6)

    question = "Является ли язык программирования Си объектно-ориентированным?"
    answers = [
        "Да",
        "Нет"
    ]
    await bot.send_poll(
        chat_id=call.message.chat.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=1,
        explanation="«Легко, если значешь язык программирования Си»",
        explanation_parse_mode=ParseMode.MARKDOWN_V2,
        reply_markup=markup
    )


async def quiz_7(call: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    button_call_7 = InlineKeyboardButton("NEXT", callback_data='button_call_7')
    markup.add(button_call_7)

    question = "К синтаксису каких языков программирования наиболее близок синтаксис C#?"
    answers = [
        "Фортран и Паскаль ",
        "Ruby и Python",
        "C++ и Java"
    ]
    await bot.send_poll(
        chat_id=call.message.chat.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=2,
        explanation="«Легко, если значешь язык программирования C Sharp»",
        explanation_parse_mode=ParseMode.MARKDOWN_V2,
        reply_markup=markup
    )


async def quiz_8(call: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    button_call_8 = InlineKeyboardButton("NEXT", callback_data='button_call_8')
    markup.add(button_call_8)

    question = "Что такое ассемблер?"
    answers = [
        "Низкоуровневый язык программирования",
        "Утилита трансляции программы в объектный код компьютера",
        "Высокоуровневый язык программирования"
    ]
    await bot.send_poll(
        chat_id=call.message.chat.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=1,
        explanation="«Ассемблер не путать с языком ассемблера»",
        explanation_parse_mode=ParseMode.MARKDOWN_V2,
        reply_markup=markup
    )


async def quiz_9(call: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    button_call_9 = InlineKeyboardButton("NEXT", callback_data='button_call_9')
    markup.add(button_call_9)

    question = "С какого языка началась традиция использования фразы «Hello, world!» в самой первой программе " \
               "при изучении нового языка программирования?"
    answers = [
        "Си",
        "C#",
        "C++",
        "Java"
    ]
    await bot.send_poll(
        chat_id=call.message.chat.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=0,
        explanation="«Надо знать историю»",
        explanation_parse_mode=ParseMode.MARKDOWN_V2,
        reply_markup=markup
    )


async def quiz_10(call: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    button_call_10 = InlineKeyboardButton("NEXT", callback_data='button_call_10')
    markup.add(button_call_10)
    photo = open("media/python_quiz2.png", 'rb')
    await bot.send_photo(call.message.chat.id, photo=photo)
    question = "Что выведет код?"
    answers = [
        "'¯\\\_(ツ)_//¯'",
        "'¯\_(ツ)_//¯'",
        "'¯\\\_(ツ)_/¯'",
        "Ничего из перечисленного"
    ]
    await bot.send_poll(
        chat_id=call.message.chat.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=1,
        explanation="«Последовательности в Python",
        explanation_parse_mode=ParseMode.MARKDOWN_V2,
        reply_markup=markup
    )


async def quiz_11(call: types.CallbackQuery):
    photo = open("media/python_quiz.png", 'rb')
    await bot.send_photo(call.message.chat.id, photo=photo)
    question = "Что выведет код? "
    answers = [
        "50 100",
        "50",
        "100",
        "Ни один из этих вариантов"
    ]
    await bot.send_poll(
        chat_id=call.message.chat.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=2,
        explanation="«Хитрый оператор AND в Python»",
        explanation_parse_mode=ParseMode.MARKDOWN_V2
    )


def register_handlers_callback(dp: Dispatcher):
    dp.register_callback_query_handler(quiz_2, lambda call: call.data == "button_call_1")
    dp.register_callback_query_handler(quiz_3, lambda call: call.data == "button_call_2")
    dp.register_callback_query_handler(quiz_4, lambda call: call.data == "button_call_3")
    dp.register_callback_query_handler(quiz_5, lambda call: call.data == "button_call_4")
    dp.register_callback_query_handler(quiz_6, lambda call: call.data == "button_call_5")
    dp.register_callback_query_handler(quiz_7, lambda call: call.data == "button_call_6")
    dp.register_callback_query_handler(quiz_8, lambda call: call.data == "button_call_7")
    dp.register_callback_query_handler(quiz_9, lambda call: call.data == "button_call_8")
    dp.register_callback_query_handler(quiz_10, lambda call: call.data == "button_call_9")
    dp.register_callback_query_handler(quiz_11, lambda call: call.data == "button_call_10")
