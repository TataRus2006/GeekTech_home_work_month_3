import asyncio
import aioschedule
from aiogram import types, Dispatcher
from config import bot


async def get_chat_id(message: types.Message):
    global chat_id
    chat_id = message.from_user.id
    await bot.send_message(chat_id=chat_id, text="Напоминание о тренировке включено!")


async def go_to_training():
    await bot.send_photo(chat_id=chat_id, photo=open("media/meme_sport.jpg", "rb"), caption="Пора на тренировку!")


async def scheduler():
    aioschedule.every().monday.at("16:00").do(go_to_training)
    aioschedule.every().wednesday.at("16:00").do(go_to_training)
    aioschedule.every().saturday.at("16:00").do(go_to_training)

    while True:
        await aioschedule.run_pending()
        await asyncio.sleep(2)


def register_handler_notification(dp: Dispatcher):
    dp.register_message_handler(get_chat_id, lambda word: 'тренировка' in word.text)
