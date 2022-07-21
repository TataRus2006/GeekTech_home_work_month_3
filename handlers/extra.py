from aiogram import types, Dispatcher
from config import bot


async def echo(message: types.Message):
    if message.text.startswith('!pin'):
        if not message.reply_to_message:
            await message.answer("Команда должна быть ответом на сообщение!")
            return
        else:
            await bot.pin_chat_message(message.chat.id, message.reply_to_message.message_id)
            return
    if message.text.startswith('!unpin'):
        await bot.unpin_chat_message(message.chat.id)
        return
    if message.text.isdigit():
        await bot.send_message(message.chat.id, int(message.text) ** 2)
    else:
        await bot.send_message(message.chat.id, message.text)


def register_handlers_extra(dp: Dispatcher):
    dp.register_message_handler(echo)
