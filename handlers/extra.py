from aiogram import types, Dispatcher
from config import bot


async def echo(message: types.Message):
    if message.text.startswith('!pin'):
        if not message.reply_to_message:
            await message.answer("Команда должна быть ответом на сообщение!")
            return
        else:
            await bot.pin_chat_message(message.chat.id, message.message_id)
            return
    if message.text.startswith('!unpin'):
        await bot.unpin_chat_message(message.chat.id)
        return
    if message.text.lower() == 'dice':
        await bot.send_message(message.chat.id, "Кости для бота")
        player1 = await bot.send_dice(message.chat.id, emoji='🎲')
        await bot.send_message(message.chat.id, "Кости для игрока")
        player2 = await bot.send_dice(message.chat.id, emoji='🎲')
        if player1.dice.value > player2.dice.value:
            await bot.send_message(message.chat.id, f"У бота выпало {player1.dice.value}, "
                                                    f"у игрока выпало {player2.dice.value}\n"
                                                    f"Победил Бот")
        if player1.dice.value < player2.dice.value:
            await bot.send_message(message.chat.id, f"У бота выпало {player1.dice.value}, "
                                                    f"у игрока выпало {player2.dice.value}\n"
                                                    f"Победил игрок")
        else:
            await bot.send_message(message.chat.id, f"У бота выпало {player1.dice.value}, "
                                                    f"у игрока выпало {player2.dice.value}\n"
                                                    f"Ничья")
        return
    if message.text.isdigit():
        await bot.send_message(message.chat.id, int(message.text) ** 2)
    else:
        await bot.send_message(message.chat.id, message.text)


def register_handlers_extra(dp: Dispatcher):
    dp.register_message_handler(echo)
