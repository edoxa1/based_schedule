from aiogram import Dispatcher
from aiogram.types import Message

from tgbot.services.parser import PdfParser


async def admin_start(message: Message):
    await message.reply("Hello, admin!")


async def update_schedule(message: Message):
    await message.reply("Updating..")
    if not message.get_args():
        return
    
    abbr = message.get_args()
    res = message.bot['config'].table.search_by_abbr(abbr)
    text = '-----\n'.join(course.get_info() for course in res)
    await message.answer(text)
    

def register_admin(dp: Dispatcher):
    dp.register_message_handler(admin_start, commands=["start"], state="*", is_admin=True)
    dp.register_message_handler(update_schedule, commands=["update"], is_admin=True)
