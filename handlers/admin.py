from random import sample
from aiogram import types, Dispatcher
from config import bot, ADMIN
from aiogram.dispatcher.filters import Text


async def game(message: types.Message):
    emoji = ('⚽', '🏀', '🎲', '🎯', '🎳', '🎰')
    if message.text.lower() == 'game':
        if message.from_user.id not in ADMIN:
            await message.answer("Вы не являетесь администратором!")
            return
        else:
            await bot.send_dice(message.chat.id, emoji=sample(emoji, 1))
            return


def register_handlers_admin(dp: Dispatcher):
    dp.register_message_handler(game, commands=['game'])
    dp.register_message_handler(game, Text(equals='game', ignore_case=True), state="*")
