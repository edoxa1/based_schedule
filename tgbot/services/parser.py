from typing import List, Dict
from tabula import read_pdf

from tgbot.models.Course import Course
from tgbot.models.Enums import Column

coursed_options = {'header': None,
                   'names': ['Course Abbr', 'S/T', 'Course Title',
                             'Cr(U\rS)', 'Cr(E\rCTS)',
                             'Start Date', 'End Date', 'Days', 'Time',
                             'Enr', 'Cap', 'Faculty', 'Room']}


class PdfParser:
    def __init__(self, path: str):
        self.path = path
        self.pdf_json = self.load_schedule()

    def load_schedule(self) -> List[Dict[str, any]]:
        # noinspection PyTypeChecker
        courses_json: List[Dict[str, any]] = read_pdf(self.path, pandas_options=coursed_options, pages='all',
                                                      output_format='json', lattice=True, stream=False)

        return courses_json

    def get_courses_list(self) -> List[Course]:
        courses: List[Course] = []
        for page in self.pdf_json:
            for row in page['data']:
                variables = (self.__get_abbr(row), self.__get_ctype(row), self.__get_title(row),
                             self.__get_credits_us(row), self.__get_credits_eu(row), self.__get_start_date(row),
                             self.__get_end_date(row), self.__get_weekdays(row), self.__get_time(row),
                             self.__get_enrolled(row), self.__get_course_capacity(row),
                             self.__get_faculty(row), self.__get_room(row))  # WHAT THE FUCK

                (abbr, ctype, title, cus, ceu, start_date, end_date, days, times, enr, cap, faculty, room) = variables

                if not abbr:
                    last_course = courses.pop()
                    last_course.weekdays.append(days)
                    last_course.time.append(times)
                    last_course.faculty = last_course.faculty + " " + faculty
                    last_course.room = last_course.room + " " + room
                    courses.append(last_course)
                    continue

                temp = Course(abbr, ctype, title, cus, ceu, start_date, end_date, days, times, enr, cap, faculty, room)

                courses.append(temp)

        courses.pop(0)
        return courses

    def __get_abbr(self, row: List[Dict[str, any]]) -> str:
        return self.get_column(row, Column.ABBR)

    def __get_ctype(self, row: List[Dict[str, any]]) -> str:
        return self.get_column(row, Column.CTYPE)

    def __get_title(self, row: List[Dict[str, any]]) -> str:
        return self.get_column(row, Column.TITLE)

    def __get_credits_us(self, row: List[Dict[str, any]]) -> str:
        return self.get_column(row, Column.CRED_US)

    def __get_credits_eu(self, row: List[Dict[str, any]]) -> str:
        return self.get_column(row, Column.CRED_EU)

    def __get_start_date(self, row: List[Dict[str, any]]) -> str:
        return self.get_column(row, Column.START)

    def __get_end_date(self, row: List[Dict[str, any]]) -> str:
        return self.get_column(row, Column.END)

    def __get_weekdays(self, row: List[Dict[str, any]]) -> str:
        return self.get_column(row, Column.DAYS)

    def __get_time(self, row: List[Dict[str, any]]) -> str:
        return self.get_column(row, Column.TIME)

    def __get_enrolled(self, row: List[Dict[str, any]]) -> str:
        return self.get_column(row, Column.ENR)

    def __get_course_capacity(self, row: List[Dict[str, any]]) -> str:
        return self.get_column(row, Column.CAP)

    def __get_faculty(self, row: List[Dict[str, any]]) -> str:
        return self.get_column(row, Column.FACULTY)

    def __get_room(self, row: List[Dict[str, any]]) -> str:
        return self.get_column(row, Column.ROOM)

    @staticmethod
    def get_column(row: List[Dict[str, any]], column: Column) -> str:
        cid = column.value
        temp = ''
        try:
            temp = row[cid]['text'].replace('\r', ' ')
        except Exception as e:
            print(e)
            # print(cid, row)
            temp = "-"

        return temp

# registrar PCC
