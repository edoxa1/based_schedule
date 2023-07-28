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
                variables = (self._get_abbr(row), self._get_ctype(row), self._get_title(row),
                             self._get_credits_us(row), self._get_credits_eu(row), self._get_start_date(row),
                             self._get_end_date(row), self._get_weekdays(row), self._get_time(row),
                             self._get_enrolled(row), self._get_course_capacity(row),
                             self._get_faculty(row), self._get_room(row))  # WHAT THE FUCK

                (abbr, ctype, title, cus, ceu, start_date, end_date, days, times, enr, cap, faculty, room) = variables

                if not abbr:
                    last_course = courses.pop()
                    last_course.weekdays = last_course.weekdays + "_" + days
                    last_course.time = last_course.time + "_" + times
                    last_course.faculty = last_course.faculty + " " + faculty
                    last_course.room = last_course.room + " " + room
                    courses.append(last_course)
                    continue

                temp = Course(abbr, ctype, title, cus, ceu, start_date, end_date, days, times, enr, cap, faculty, room)

                courses.append(temp)

        courses.pop(0)
        return courses

    def _get_abbr(self, row: List[Dict[str, any]]) -> str:
        return self.get_column(row, Column.ABBR)

    def _get_ctype(self, row: List[Dict[str, any]]) -> str:
        return self.get_column(row, Column.CTYPE)

    def _get_title(self, row: List[Dict[str, any]]) -> str:
        return self.get_column(row, Column.TITLE)

    def _get_credits_us(self, row: List[Dict[str, any]]) -> str:
        return self.get_column(row, Column.CRED_US)

    def _get_credits_eu(self, row: List[Dict[str, any]]) -> str:
        return self.get_column(row, Column.CRED_EU)

    def _get_start_date(self, row: List[Dict[str, any]]) -> str:
        return self.get_column(row, Column.START)

    def _get_end_date(self, row: List[Dict[str, any]]) -> str:
        return self.get_column(row, Column.END)

    def _get_weekdays(self, row: List[Dict[str, any]]) -> str:
        return self.get_column(row, Column.DAYS)

    def _get_time(self, row: List[Dict[str, any]]) -> str:
        return self.get_column(row, Column.TIME)

    def _get_enrolled(self, row: List[Dict[str, any]]) -> str:
        return self.get_column(row, Column.ENR)

    def _get_course_capacity(self, row: List[Dict[str, any]]) -> str:
        return self.get_column(row, Column.CAP)

    def _get_faculty(self, row: List[Dict[str, any]]) -> str:
        return self.get_column(row, Column.FACULTY)

    def _get_room(self, row: List[Dict[str, any]]) -> str:
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
