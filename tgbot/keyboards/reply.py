from typing import List
from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton


def generate_courses_select_keyboard(abbrs: List[str]):
    kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    for abbr in abbrs:
        kb.insert(KeyboardButton(text=abbr))
        
    return kb


def generate_course_types_keyboard(ctypes: List[str]):
    kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    for ctype in ctypes:
        kb.insert(KeyboardButton(text=ctype))
        
    return kb
