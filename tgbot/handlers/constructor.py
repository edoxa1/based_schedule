from typing import List

from aiogram import Dispatcher
from aiogram.types import Message, CallbackQuery
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup

from tgbot.keyboards import inline, reply
from tgbot.models.Course import Course
from tgbot.services.table import Table


class CourseSelectionForm(StatesGroup):
    user_course_abbr: str = State()
    selected_course_abbr: str = State()
    selected_course_type: Course = State()


async def start_constructor(message: Message):
    kb = inline.generate_constructor_menu_keyboard()
    await message.answer(text='Enter course abbreviation or import them', reply_markup=kb)
    await CourseSelectionForm.user_course_abbr.set()
    

async def get_user_abbr(message: Message, state: FSMContext):
    table: Table = message.bot['config'].table
    abbr = message.text
    courses: List[Course] = table.search_by_abbr(abbr)
   
    if not courses:
        await message.answer(f"No results for <i>{abbr}</i>")
        return

    abbrs = [course.abbr for course in courses]
    kb = reply.generate_courses_select_keyboard(abbrs)
    text = ''
    for course in courses:
        text += course.get_course_overall_info()
        
    async with state.proxy() as data:
        data['user_course_abbr'] = message.text
        data['result_abbrs'] = abbrs
        
    await message.answer(text=text, reply_markup=kb)
    await CourseSelectionForm.next()


async def course_abbr_selection(message: Message, state: FSMContext):
    table: Table = message.bot['config'].table
    abbr = message.text.lower().replace(' ', '')
    
    courses: List[Course] = table.get_course_types(abbr)
    if not courses:
        await message.answer("Not found")
        return
    
    text = ""
    ctypes = []
    for course in courses:
        text += f"{course.get_info_short()}"
        ctypes.append(course.course_type)
    
    kb = reply.generate_course_types_keyboard(ctypes)
    
    async with state.proxy() as data:
        data['selected_course_abbr'] = abbr
        
    await message.answer(text, reply_markup=kb)
    await CourseSelectionForm.next()


async def course_type_selection(message: Message, state: FSMContext):
    table: Table = message.bot['config'].table
    ctype = message.text
    kb = inline.generate_constructor_menu_keyboard()
    
    async with state.proxy() as data:
        print(data['selected_course_abbr'], ctype)
        course: Course = table.get_course_by_ctype(data['selected_course_abbr'], ctype)
        data['course'] = course
        
    await message.answer(f"Course {course.abbr} added to cart!", reply_markup=kb)   
    await state.finish()


async def cancel_form(message: Message, state: FSMContext):
    current_state = await state.get_state()
    if not current_state:
        return
    
    await message.answer("Returning back")
    await state.finish()


def register_handlers(dp: Dispatcher):
    dp.register_message_handler(start_constructor, commands=["construct"])
    dp.register_message_handler(get_user_abbr, state=CourseSelectionForm.user_course_abbr)
    dp.register_message_handler(course_abbr_selection, state=CourseSelectionForm.selected_course_abbr)
    dp.register_message_handler(course_type_selection, state=CourseSelectionForm.selected_course_type)
    dp.register_message_handler(cancel_form, commands=["/cancel"], state="*")