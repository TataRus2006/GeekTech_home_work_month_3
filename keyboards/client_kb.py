from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


cancel_button = KeyboardButton("CANCEL")
cancel_marcup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(cancel_button)


start_button = KeyboardButton("/start")
meme_button = KeyboardButton("/meme")
help_button = KeyboardButton("/help")
quiz_button = KeyboardButton("/quiz")
game_button = KeyboardButton("game")
dice_button = KeyboardButton("/dice")
menu_button = KeyboardButton("/menu")
pin_button = KeyboardButton("!pin")
unpin_button = KeyboardButton("!unpin")
location_button = KeyboardButton("location", request_location=True)
contact_button = KeyboardButton("contact", request_contact=True)

start_marcup = ReplyKeyboardMarkup(resize_keyboard=True)

start_marcup.row(start_button, meme_button, help_button, menu_button)
start_marcup.row(quiz_button, game_button, dice_button)
start_marcup.row(pin_button, unpin_button)
start_marcup.row(location_button, contact_button)
