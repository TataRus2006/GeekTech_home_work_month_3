import random
import sqlite3
from config import bot


def sql_create():
    global db, cursor
    db = sqlite3.connect("bot.sqlite3")
    cursor = db.cursor()

    if db:
        print("База данных подключена!")

    db.execute("CREATE TABLE IF NOT EXISTS menu "
               "(photo TEXT, name TEXT PRIMARY KEY, description TEXT, "
               "weight INTEGER, calorie INTEGER, price INTEGER)")
    db.commit()

async def sql_command_insert(state):
    async with state.proxy() as data:
        cursor.execute("INSERT INTO menu VALUES (?, ?, ?, ?, ?, ?)", tuple(data.values()))
        db.commit()

async def sql_command_random(message):
    result = cursor.execute("SELECT * FROM menu").fetchall()
    random_user = random.choice(result)
    await bot.send_photo(message.chat.id, random_user[0],
                         caption=f"Название блюда: {random_user[1]}\n"
                                 f"Описание блюда: {random_user[2]}\n"
                                 f"Вес блюда: {random_user[3]} грамм\n"
                                 f"Калорийность блюда: {random_user[4]} ккал\n"
                                 f"Цена блюда: {random_user[5]} сом\n")
async def sql_command_all():
    return cursor.execute("SELECT * FROM menu").fetchall()

async def sql_command_delete(name):
    cursor.execute("DELETE FROM menu WHERE name == ?", (name, ))
    db.commit()
