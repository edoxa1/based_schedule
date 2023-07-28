from typing import List
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


# def generate_course_selection_keyboard(abbr: str, types: List[str]) -> InlineKeyboardMarkup:
#     kb = InlineKeyboardMarkup(row_width=4)
#     types.sort(key=by_ascii_sum)
    
#     for index in range(len(types)):
#         kb.insert(
#             InlineKeyboardButton(text=f"{types[index]}", 
#                                  callback_data=f"course:{abbr}_{types[index]}")
#         )
    
#     return kb


def generate_course_selection_keyboard(abbr: str, page: str, size: str):
    kb = InlineKeyboardMarkup(row_width=3)
    kb.add(InlineKeyboardButton(text="<-", callback_data=f"constructor:left:{abbr}:{page}"),
           InlineKeyboardButton(text=f"{page}/{size}"),
           InlineKeyboardButton(text="->", callback_data=f"constructor:right:{abbr}:{page}"))
    
    return kb


def generate_constructor_menu_keyboard() -> InlineKeyboardMarkup:
    kb = InlineKeyboardMarkup(row_width=2)
    kb.add(
        InlineKeyboardButton(text="Cart", callback_data="constructor:menu"),
        InlineKeyboardButton(text="Import", callback_data="constructor:import"),
        InlineKeyboardButton(text="Back", callback_data="constructor:back"))
    
    return kb


def by_ascii_sum(word):
    return sum([ord(c) for c in word])  # ord(c) returns ascii value
