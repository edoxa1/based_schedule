from aiogram import Dispatcher
from aiogram.types import Message, CallbackQuery

from tgbot.keyboards.inline import generate_course_selection_keyboard


async def admin_start(message: Message):
    await message.reply("Hello, admin!")


async def update_schedule(message: Message):
    await message.reply("Updating..")
    if not message.get_args():
        return
    
    abbr = message.get_args().lower()
    res = message.bot['config'].table.get_course_types(abbr)
    if not res:
        return
    
    text = ""
    ctypes = []
    for course in res:
        text += f"\n{course.get_info_short()}\n"
        ctypes.append(course.course_type)
        
    await message.answer(text, reply_markup=generate_course_selection_keyboard(abbr, ctypes))
    

async def construct(call: CallbackQuery):
    await call.answer(f"Selected: {call.data}")
    await call.message.answer(f"Selected: {call.data}")


def register_admin(dp: Dispatcher):
    dp.register_message_handler(admin_start, commands=["start"], is_admin=True)
    dp.register_message_handler(update_schedule, commands=["update"], is_admin=True)
    
    # callbacks
    dp.register_callback_query_handler(construct, cdata_begins_with="course", is_admin=True)
