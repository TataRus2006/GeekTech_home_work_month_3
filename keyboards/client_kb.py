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
btnQRcode = KeyboardButton("/qr")
btnCars = KeyboardButton("/cars")
btnPin = KeyboardButton("!pin")
btnUnpin = KeyboardButton("!unpin")
otherMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(btnTraining, btnQRcode, btnCars, btnPin, btnUnpin, btnMain)


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


cancel_button = KeyboardButton("CANCEL")
cancel_marcup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(cancel_button)


cancel_qr_button = KeyboardButton("CANCEL QR")
cancel_qr_marcup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(cancel_qr_button)
