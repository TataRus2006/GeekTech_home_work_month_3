from aiogram import types, Dispatcher
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
from config import bot, ADMIN
from keyboards import client_kb
from database import bot_db

class FSMAdmin(StatesGroup):
    dish_photo = State()                      # фотография блюда
    dish_name = State()                       # название блюда
    dish_description = State()                # описание блюда
    dish_weight = State()                     # вес блюда
    dish_calorie = State()                    # калорийность блюда
    dish_price = State()                      # цена блюда


async def fsm_start(message: types.Message):
    if message.from_user.id in ADMIN:
        await FSMAdmin.dish_photo.set()
        await message.answer(f"Приветствую Вас {message.from_user.full_name}, "
                             f"загрузите фотографию блюда", reply_markup=client_kb.cancel_marcup)
    else:
        await message.reply("Вы не являетесь администратором!")


async def load_dish_photo(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["photo"] = message.photo[0].file_id
    await FSMAdmin.next()
    await message.answer("Введите название блюда")


async def load_dish_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["name"] = message.text
    await FSMAdmin.next()
    await message.answer("Введите описание блюда")


async def load_dish_description(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["description"] = message.text
    await FSMAdmin.next()
    await message.answer("Введите вес блюда в граммах")


async def load_dish_weight(message: types.Message, state: FSMContext):
    try:
        async with state.proxy() as data:
            data["weight"] = int(message.text)
        await FSMAdmin.next()
        await message.answer("Введите калорийность блюда в килокалории")
    except:
        await message.answer("Вводите только цифры!")


async def load_dish_calorie(message: types.Message, state: FSMContext):
    try:
        async with state.proxy() as data:
            data["calorie"] = int(message.text)
        await FSMAdmin.next()
        await message.answer("Введите цену блюда в в кыргызских сомах")
    except:
        await message.answer("Вводите только цифры!")


async def load_dish_price(message: types.Message, state: FSMContext):
    try:
        async with state.proxy() as data:
            data["price"] = int(message.text)
            await bot.send_photo(message.chat.id, data['photo'],
                                 caption=f"Название блюда: {data['name']}\n"
                                         f"Описание блюда: {data['description']}\n"
                                         f"Вес блюда: {data['weight']} грамм\n"
                                         f"Калорийность блюда: {data['calorie']} ккал\n"
                                         f"Цена блюда: {data['price']} сом\n")
        await bot_db.sql_command_insert(state)
        await state.finish()
        await message.answer(f"Вы успешно добавили блюдо: \"{data['name']}\"", reply_markup=client_kb.dishMenu)
    except:
        await message.answer("Вводите только цифры!")

async def cancel_add_dish(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        return
    else:
        await message.answer("Добавление блюда отменено!", reply_markup=client_kb.dishMenu)
        await state.finish()


async def show_menu(message: types.Message):
    menu = await bot_db.sql_command_all()
    for dish in menu:
        await bot.send_photo(message.chat.id, dish[0],
                             caption=f"Название блюда: {dish[1]}\n"
                                     f"Описание блюда: {dish[2]}\n"
                                     f"Вес блюда: {dish[3]} грамм\n"
                                     f"Калорийность блюда: {dish[4]} ккал\n"
                                     f"Цена блюда: {dish[5]} сом\n")


async def delete_dish(message: types.Message):
    if message.from_user.id in ADMIN and message.chat.type == "private":
        dishes = await bot_db.sql_command_all()
        for dish in dishes:
            await bot.send_photo(message.from_user.id, dish[0],
                                 caption=f"Название блюда: {dish[1]}\n"
                                         f"Описание блюда: {dish[2]}\n"
                                         f"Вес блюда: {dish[3]} грамм\n"
                                         f"Калорийность блюда: {dish[4]} ккал\n"
                                         f"Цена блюда: {dish[5]} сом\n",
                                 reply_markup=InlineKeyboardMarkup().add(InlineKeyboardButton(f"delete: {dish[1]}",
                                 callback_data=f"delete {dish[1]}")))
    else:
        await message.reply("Вы не являетесь администратором!")


async def complete_delete(call: types.CallbackQuery):
    await bot_db.sql_command_delete(call.data.replace('delete ', ''))
    await call.answer(text="Блюдо удалено", show_alert=True)
    await bot.delete_message(call.message.chat.id, call.message.message_id)


def register_handlers_fsm_menu(dp: Dispatcher):
    dp.register_message_handler(cancel_add_dish, state="*", commands='cancel')
    dp.register_message_handler(cancel_add_dish, Text(equals='cancel', ignore_case=True), state="*")
    dp.register_message_handler(fsm_start, commands=['add_dish'])
    dp.register_message_handler(load_dish_photo, state=FSMAdmin.dish_photo, content_types=["photo"])
    dp.register_message_handler(load_dish_name, state=FSMAdmin.dish_name)
    dp.register_message_handler(load_dish_description, state=FSMAdmin.dish_description)
    dp.register_message_handler(load_dish_weight, state=FSMAdmin.dish_weight)
    dp.register_message_handler(load_dish_calorie, state=FSMAdmin.dish_calorie)
    dp.register_message_handler(load_dish_price, state=FSMAdmin.dish_price)
    dp.register_message_handler(show_menu, commands=["show_menu"])
    dp.register_message_handler(delete_dish, commands=["del_dish"])
    dp.register_callback_query_handler(complete_delete,
                                       lambda call: call.data and call.data.startswith('delete '))
