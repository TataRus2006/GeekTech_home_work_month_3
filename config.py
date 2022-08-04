from aiogram import Bot, Dispatcher
from decouple import config
from aiogram.contrib.fsm_storage.memory import MemoryStorage

STORAGE = MemoryStorage()

TOKEN = config('TOKEN')
bot = Bot(TOKEN)
dp = Dispatcher(bot=bot, storage=STORAGE)
ADMIN = [863372886, 1746047370, 5367214519]     # -> Rustam, Nuria, Esen
URL = "https://rustam-bot.herokuapp.com/"
PORT = config('PORT')
