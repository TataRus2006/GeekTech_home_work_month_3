from aiogram.utils import executor
from config import dp
import logging
import asyncio

from handlers import client, callback, extra, admin, fsm_AdminMenu, notification, fsmqrcode, inline
from database.bot_db import sql_create


async def on_startup(_):
    asyncio.create_task(notification.scheduler())
    sql_create()


client.register_handlers_client(dp)
callback.register_handlers_callback(dp)
admin.register_handlers_admin(dp)
fsm_AdminMenu.register_handlers_fsm_menu(dp)
fsmqrcode.register_handler_fsmqrcode(dp)
inline.register_handlers_inline(dp)
notification.register_handler_notification(dp)

extra.register_handlers_extra(dp)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
