from typing import Union, List

from aiogram.types import CallbackQuery
from aiogram.dispatcher.filters import BoundFilter


class CallbackDataFilter(BoundFilter):
    key = 'callback_data'

    def __init__(self, callback_data: Union[str, List[str]]):
        self.callback_data = callback_data

    async def check(self, obj: CallbackQuery):
        if not self.callback_data:
            return False

        if isinstance(self.callback_data, list):
            return obj.data in self.callback_data

        print(obj.data == self.callback_data)
        return obj.data == self.callback_data


class CallbackDataBeginsWithFilter(BoundFilter):
    key = 'cdata_begins_with'
    
    def __init__(self, cdata_begins_with: str):
        self.cdata_begins_with = cdata_begins_with
        
    async def check(self, obj: CallbackQuery):
        if not self.cdata_begins_with:
            return False
        
        return obj.data[:len(self.cdata_begins_with)] == self.cdata_begins_with
