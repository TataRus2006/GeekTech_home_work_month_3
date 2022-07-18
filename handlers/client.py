from aiogram import types, Dispatcher
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ParseMode
from config import bot


async def start_handler(message: types.Message):
    await bot.send_message(message.chat.id,
                           f"Шаломуалейкум {message.from_user.full_name}")


async def help_handler(message: types.Message):
    await bot.send_message(message.chat.id,
                           f"Бог в помощь!")


async def quiz_handler(message: types.Message):
    markup = InlineKeyboardMarkup()
    button_call_1 = InlineKeyboardButton("NEXT", callback_data='button_call_1')
    markup.add(button_call_1)

    question = "Сколько на данный момент существует языков программирования?"
    answers = [
        'Около 500',
        'Чуть более 1000',
        'Более 8000'
    ]
    await bot.send_poll(
        chat_id=message.chat.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=2,
        explanation="Их, ну очень много»",
        explanation_parse_mode=ParseMode.MARKDOWN_V2,
        reply_markup=markup
    )


async def meme_handler(message: types.Message):
    photo = open("media/meme_Python.jpg", 'rb')
    await bot.send_photo(message.chat.id, photo=photo)


def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(start_handler, commands=['start'])
    dp.register_message_handler(help_handler, commands=['help'])
    dp.register_message_handler(quiz_handler, commands=['quiz'])
    dp.register_message_handler(meme_handler, commands=['meme'])
