from aiogram import types, Dispatcher
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ParseMode
from config import bot
from keyboards import client_kb
from database.bot_db import sql_command_random
from parser import cars
import asyncio


async def start_handler(message: types.Message):
    await bot.send_message(message.chat.id,
                           f"Шаломуалейкум {message.from_user.full_name}", reply_markup=client_kb.mainMenu)


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


async def dice_handler(message: types.Message):
    await bot.send_message(message.chat.id, f"Кости для бота")
    player1 = await bot.send_dice(message.chat.id, emoji='🎲')
    await asyncio.sleep(3)
    await bot.send_message(message.chat.id, f"У бота выпало {player1.dice.value}")
    await bot.send_message(message.chat.id, f"Кости для {message.from_user.full_name}")
    player2 = await bot.send_dice(message.chat.id, emoji='🎲')
    await asyncio.sleep(3)
    await bot.send_message(message.chat.id, f"у игрока выпало {player2.dice.value}")
    if player1.dice.value > player2.dice.value:
        await bot.send_message(message.chat.id, f"Результат: Победил Бот")
        return
    if player1.dice.value < player2.dice.value:
        await bot.send_message(message.chat.id, f"Результат: Победил {message.from_user.full_name}")
        return
    else:
        await bot.send_message(message.chat.id, f"Результат: Ничья")
    return


async def show_random_dish(message: types.Message):
    await sql_command_random(message)


async def parser_cars(message: types.Message):
    data = cars.parser()[:5]
    for item in data:
        await bot.send_message(message.chat.id,
                               f"{item['name']}\n\n"
                               f"Цена: {item['price']}\n"
                               f"{item['characteristics1']}\n"
                               f"{item['characteristics2']}\n"
                               f"{item['characteristics3']}\n"
                               f"Цвет: {item['color']}\n"
                               f"Кол-во просмотров: {item['count_view']}\n\n"
                               f"{item['foto']}\n\n"
                               f"{item['link']}\n\n")


def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(start_handler, commands=['start'])
    dp.register_message_handler(help_handler, commands=['help'])
    dp.register_message_handler(quiz_handler, commands=['quiz'])
    dp.register_message_handler(meme_handler, commands=['meme'])
    dp.register_message_handler(dice_handler, commands=['dice'])
    dp.register_message_handler(show_random_dish, commands=['random_dish'])
    dp.register_message_handler(parser_cars, commands=['cars'])
    dp.register_callback_query_handler(show_random_dish, lambda call: call.data == "Меню")