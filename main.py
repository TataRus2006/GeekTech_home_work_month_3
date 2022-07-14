from aiogram import types
from aiogram.utils import executor
from aiogram.types import ParseMode, InlineKeyboardMarkup, InlineKeyboardButton
from config import bot, dp
import logging

@dp.message_handler(commands=['start'])
async def start_message(message: types.Message):
    await bot.send_message(message.from_user.id,
                           f"Шаломуалейкум {message.from_user.full_name}" )


@dp.message_handler(commands=['help'])
async def start_message(message: types.Message):
    await bot.send_message(message.from_user.id,
                           f"Бог в помощь!")


@dp.message_handler(commands=['quiz'])
async def quiz_handler(message: types.Message):
    markup = InlineKeyboardMarkup()
    button_call_1 = InlineKeyboardButton("NEXT", callback_data='button_call_1')
    markup.add(button_call_1)

    question = "Чем должен владеть богатый человек?"
    answers = [
        'женой и тёщей',
        'собакой и кошкой',
        'колом и двором',
        'машиной и работой',
        "лопатой и тяпкой",
        "руками и мозгами"
    ]
    await bot.send_poll(
        chat_id=message.chat.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=2,
        explanation="у бедного нет «ни кола, ни двора»",
        explanation_parse_mode=ParseMode.MARKDOWN_V2,
        reply_markup=markup
    )


@dp.callback_query_handler(lambda call: call.data == "button_call_1")
async def quiz_2(call: types.CallbackQuery):

    question = "С каким животным готов расстаться голодный человек?"
    answers = [
        "с бараном",
        "с собакой",
        "с пчелой",
        "с комаром",
        "с червячком",
        "с коровой",
    ]
    await bot.send_poll(
        chat_id=call.message.chat.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=4,
        explanation="«заморить червячка»",
        explanation_parse_mode=ParseMode.MARKDOWN_V2
    )


@dp.message_handler(commands=['meme'])
async def meme_handler(message: types.message):
    photo = open("media/meme_Python.jpg", 'rb')
    await bot.send_photo(message.chat.id, photo=photo)


@dp.message_handler()
async def echo(message: types.Message):
    if message.text.isdigit():
        await bot.send_message(message.from_user.id, int(message.text) * int(message.text))
    else:
        await bot.send_message(message.from_user.id, message.text)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True)
