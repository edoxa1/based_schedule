from aiogram import Dispatcher
from aiogram.types import Message

from tgbot.handlers.constructor import register_handlers


async def user_start(message: Message):
    await message.reply("Hello, user!")


def register_user(dp: Dispatcher):
    register_handlers(dp)
    dp.register_message_handler(user_start, commands=["start"], state="*")
