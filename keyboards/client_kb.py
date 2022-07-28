from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

start_button = KeyboardButton("/start")
meme_button = KeyboardButton("/meme")
help_button = KeyboardButton("/help")
quiz_button = KeyboardButton("/quiz")
game_button = KeyboardButton("game")
dice_button = KeyboardButton("/dice")
menu_button = KeyboardButton("/menu")
pin_button = KeyboardButton("!pin")
unpin_button = KeyboardButton("!unpin")
random_dish = KeyboardButton("/random_dish")
show_menu = KeyboardButton("/show_menu")
delete_dish = KeyboardButton("/del_dish")
training_button = KeyboardButton("тренировка")
cars_button = KeyboardButton("/cars")

start_marcup = ReplyKeyboardMarkup(resize_keyboard=True)

start_marcup.row(start_button, help_button, meme_button, game_button)
start_marcup.row(quiz_button, dice_button, pin_button, unpin_button)
start_marcup.row(menu_button, random_dish, show_menu, delete_dish)
start_marcup.row(training_button, cars_button)

cancel_button = KeyboardButton("CANCEL")
cancel_marcup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(cancel_button)
