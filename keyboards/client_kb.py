from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


btnMain = KeyboardButton("⬅️Главное меню")

#-------------Main Menu-------------
btnStart = KeyboardButton("/start")
help_button = KeyboardButton("/help")
btnFun = KeyboardButton("🤡 Развлечение")
btnMenu = KeyboardButton("🧆 Меню")
btnOther = KeyboardButton("➡️Другое")
mainMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(btnStart, help_button, btnFun, btnMenu, btnOther)


#-------------Other Menu-------------
btnTraining = KeyboardButton("тренировка")
btnCars = KeyboardButton("/cars")
btnPin = KeyboardButton("!pin")
btnUnpin = KeyboardButton("!unpin")
otherMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(btnTraining, btnCars, btnPin, btnUnpin, btnMain)


#-------------Dish Menu-------------
btnShow_menu = KeyboardButton("/show_menu")
btnRandom_dish = KeyboardButton("/random_dish")
btnAdd_dish = KeyboardButton("/add_dish")
btnDelete_dish = KeyboardButton("/del_dish")
dishMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(btnShow_menu, btnRandom_dish, btnAdd_dish, btnDelete_dish,
                                                         btnMain)

#-------------Fun Menu-------------
btnRandom = KeyboardButton("🔸️ Рандомное число")
btnMeme = KeyboardButton("/meme")
btnGame = KeyboardButton("game")
btnDice = KeyboardButton("/dice")
btnQuiz = KeyboardButton("/quiz")
funMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(btnRandom, btnMeme, btnGame, btnDice, btnQuiz, btnMain)




# start_marcup = ReplyKeyboardMarkup(resize_keyboard=True)
#
#
# start_marcup.row(start_button, help_button, meme_button, game_button)
# start_marcup.row(quiz_button, dice_button, pin_button, unpin_button)
# start_marcup.row(menu_button, random_dish, show_menu, delete_dish)
# start_marcup.row(training_button, cars_button)


cancel_button = KeyboardButton("CANCEL")
cancel_marcup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(cancel_button)
