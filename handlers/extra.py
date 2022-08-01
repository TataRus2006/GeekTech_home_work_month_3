from aiogram import types, Dispatcher
from config import bot
from keyboards import client_kb
import random


async def echo(message: types.Message):
    if message.text.startswith('!pin'):
        if not message.reply_to_message:
            await message.answer("Команда должна быть ответом на сообщение!")
            return
        else:
            await bot.pin_chat_message(message.chat.id, message.reply_to_message.message_id)
            return
    elif message.text.startswith('!unpin'):
        await bot.unpin_chat_message(message.chat.id)
        await message.answer(f'Закрепленно сообщение откреплено')
        return
    elif message.text.isdigit():
        await bot.send_message(message.chat.id, int(message.text) ** 2)
    elif message.text == "🔸️ Рандомное число":
        await bot.send_message(message.from_user.id, 'Ваше число: ' + str(random.randint(1, 100)))
    elif message.text == "⬅️Главное меню":
        await bot.send_message(message.from_user.id, '⬅️Главное меню', reply_markup=client_kb.mainMenu)
    elif message.text == "➡️Другое":
        await bot.send_message(message.from_user.id, '➡️Другое', reply_markup=client_kb.otherMenu)
    elif message.text == "🤡 Развлечение":
        await bot.send_message(message.from_user.id, '🤡 Развлечение', reply_markup=client_kb.funMenu)
    elif message.text == "🧆 Меню":
        await bot.send_message(message.from_user.id, '🧆 Меню', reply_markup=client_kb.dishMenu)
    else:
        await bot.send_message(message.chat.id, message.text)


def register_handlers_extra(dp: Dispatcher):
    dp.register_message_handler(echo)
