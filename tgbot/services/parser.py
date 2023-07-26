from typing import List, Dict
from tabula import read_pdf

from tgbot.models.Course import Course
from tgbot.models.Enums import Columns

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
                                                      output_format='json')

        return courses_json

    def normalise_pdf_file(self) -> List[Course]:
        courses: List[Course] = []
        for page in self.pdf_json:
            for row in page['data']:
                temp = Course(self.get_abbr(row), self.get_ctype(row), self.get_title(row))
                courses.append()

        return courses

    def get_abbr(self, row: List[Dict[str, any]]) -> str:
        return self.get_column(row, Columns.ABBR)

    def get_ctype(self, row: List[Dict[str, any]]) -> str:
        return self.get_column(row, Columns.CTYPE)

    def get_title(self, row: List[Dict[str, any]]) -> str:
        return self.get_column(row, Columns.TITLE)

    def get_credits_us(self, row: List[Dict[str, any]]) -> str:
        return self.get_column(row, Columns.CRED_US)

    def get_credits_eu(self, row: List[Dict[str, any]]) -> str:
        return self.get_column(row, Columns.CRED_EU)

    def get_start_date(self, row: List[Dict[str, any]]) -> str:
        return self.get_column(row, Columns.START)

    def get_end_date(self, row: List[Dict[str, any]]) -> str:
        return self.get_column(row, Columns.END)

    def get_weekdays(self, row: List[Dict[str, any]]) -> str:
        return self.get_column(row, Columns.DAYS)

    def get_time(self, row: List[Dict[str, any]]) -> str:
        return self.get_column(row, Columns.TIME)

    def get_enrolled(self, row: List[Dict[str, any]]) -> str:
        return self.get_column(row, Columns.ENR)

    def get_course_capacity(self, row: List[Dict[str, any]]) -> str:
        return self.get_column(row, Columns.CAP)

    def get_faculty(self, row: List[Dict[str, any]]) -> str:
        return self.get_column(row, Columns.FACULTY)

    def get_room(self, row: List[Dict[str, any]]) -> str:
        return self.get_column(row, Columns.ROOM)

    @staticmethod
    def get_column(row: List[Dict[str, any]], column: Columns) -> str:
        cid = column.value
        return row[cid]['text'].replace('\r', ' ')

