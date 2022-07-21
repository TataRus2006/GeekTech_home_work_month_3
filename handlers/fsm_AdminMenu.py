from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
from config import bot, ADMIN
from keyboards import client_kb


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
    await message.answer("Введите вес блюда")


async def load_dish_weight(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["weight"] = message.text
    await FSMAdmin.next()
    await message.answer("Введите калорийность блюда")


async def load_dish_calorie(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["calorie"] = message.text
    await FSMAdmin.next()
    await message.answer("Введите цену блюда")


async def load_dish_price(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["price"] = message.text
        await bot.send_photo(message.chat.id, data['photo'],
                             caption=f"Название блюда: {data['name']}\n"
                                     f"Описание блюда: {data['description']}\n"
                                     f"Вес блюда: {data['weight']}\n"
                                     f"Калорийность блюда: {data['calorie']}\n"
                                     f"Цена блюда: {data['price']}\n")
    await state.finish()
    await message.answer(f"Вы успешно добавили блюдо: \"{data['name']}\"")


async def cancel_add_dish(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        return
    else:
        await state.finish()
        await message.answer("Добавление блюда отменено!")


def register_handlers_fsm_menu(dp: Dispatcher):
    dp.register_message_handler(cancel_add_dish, state="*", commands='cancel')
    dp.register_message_handler(cancel_add_dish, Text(equals='cancel', ignore_case=True), state="*")
    dp.register_message_handler(fsm_start, commands=['menu'])
    dp.register_message_handler(load_dish_photo, state=FSMAdmin.dish_photo, content_types=["photo"])
    dp.register_message_handler(load_dish_name, state=FSMAdmin.dish_name)
    dp.register_message_handler(load_dish_description, state=FSMAdmin.dish_description)
    dp.register_message_handler(load_dish_weight, state=FSMAdmin.dish_weight)
    dp.register_message_handler(load_dish_calorie, state=FSMAdmin.dish_calorie)
    dp.register_message_handler(load_dish_price, state=FSMAdmin.dish_price)
