from typing import List
from tgbot.services.parser import PdfParser
from tgbot.models.Course import Course


class Table:
    def __init__(self, path: str) -> None:
        self.courses_list: List[Course] = PdfParser(path).get_courses_list()
        self.course_abbr_list: List[str] = [course.abbr.replace(' ', '') for course in self.courses_list]
        print(self.course_abbr_list.__len__())

    def search_by_abbr(self, search: str) -> List[Course]:
        arr: List[Course] = []
        for index, abbr in enumerate(self.course_abbr_list):
            if abbr == search:
                arr.append(self.courses_list[index])
            
        return arr

