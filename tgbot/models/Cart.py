from datetime import datetime
from typing import List

from tgbot.models.Course import Course


class Cart:
    def __init__(self, user_id: int, created: datetime, last_updated: datetime):
        self.user_id: int = user_id
        self.created = created
        self.last_updated = last_updated
        self.courses_list: List[Course] = []

    def add(self, course: Course) -> bool:
        if not self.__check_for_unique(course):
            return False

        self.courses_list.append(course)
        self.__update_datetime()
        return True

    def remove(self, course: Course) -> bool:
        try:
            self.courses_list.remove(course)
            self.__update_datetime()
            return True
        except ValueError:
            return False

    def clear_cart(self):
        self.courses_list.clear()
        self.__update_datetime()
        return True

    def __update_datetime(self):
        self.last_updated = datetime.now()

    def __check_for_unique(self, course: Course) -> bool:
        for temp_course in self.courses_list:
            if course == temp_course:
                return False

        return True
