from typing import List
from tgbot.services.parser import PdfParser
from tgbot.models.Course import Course


class Table:
    def __init__(self, path: str) -> None:
        self.courses_list: List[Course] = PdfParser(path).get_courses_list()
        self.course_abbr_list: List[str] = [course.abbr.replace(' ', '').lower() for course in self.courses_list]
        self.unique_course_abbr_list: List[str] = sorted(list(set(self.course_abbr_list)))
        print(self.unique_course_abbr_list)

    def get_course_by_abbr(self, search_abbr: str) -> Course:
        search_abbr = search_abbr.lower()
        for index, abbr in enumerate(self.course_abbr_list):
            if abbr == search_abbr:
                return self.courses_list[index]
        
        return None
    
    def get_course_types(self, search_abbr: str) -> List[Course]:
        search_abbr = search_abbr.lower()
        arr: List[Course] = []
        for index, abbr in enumerate(self.course_abbr_list):
            if abbr == search_abbr:
                arr.append(self.courses_list[index])
        
        arr.sort(key=lambda course: sum([ord(ch) for ch in course.course_type]))
        return arr if arr.__len__() > 0 else None

    def get_course_by_ctype(self, search_abbr: str, search_ctype: str) -> Course:
        search_abbr = search_abbr.lower()
        for index, abbr in enumerate(self.course_abbr_list):
            if abbr == search_abbr:
                if self.courses_list[index].course_type == search_ctype:
                    return self.courses_list[index]
        
        return None
    
    def search_by_abbr(self, search_abbr: str) -> List[Course]:
        search_abbr = search_abbr.lower()
        courses: List[Course] = []
        for abbr in self.unique_course_abbr_list:
            if len(courses) > 4:
                break
             
            if search_abbr in abbr:
                courses.append(self.get_course_by_abbr(abbr))
                
        return courses if courses.__len__() > 0 else None
