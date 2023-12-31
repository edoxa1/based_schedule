from typing import List


class Course:
    def __init__(self, abbr: str, course_type: str, title: str,
                 credits_us: str, credits_eu: str,
                 start_date: str, end_date: str, weekdays: str, times: str,
                 enrolled: int, course_capacity: int,
                 faculty: str, room: str):
        self.abbr: str = abbr if abbr else 'N/A'
        self.course_type: str = course_type if course_type else 'N/A'
        self.title: str = title if title else 'N/A'
        self.credits_us: str = credits_us if credits_us else 'N/A'
        self.credits_eu: str = credits_eu if credits_eu else 'N/A'
        self.start_date: str = start_date if start_date else 'N/A'
        self.end_date: str = end_date if end_date else 'N/A'
        self.weekdays: List[str] = [day for day in weekdays.split(" ")]
        self.time: List[str] = [times]
        self.enrolled: str = enrolled if enrolled else 'N/A'
        self.course_capacity: str = course_capacity if course_capacity else 'N/A'
        self.faculty: str = faculty if faculty else 'N/A'
        try:
            self.room: str = room.split('-')[0].strip() if room else 'N/A'
        except ValueError:
            self.room = room if room else 'N/A'

    def get_info(self) -> str:
        text = f'{self.abbr} [{self.course_type}] - {self.title} \n{self.credits_eu} ECTS\n' \
            f'{self.start_date} - {self.end_date}\n' \
            f'{self.weekdays} - {self.time}\n' \
            f'{self.enrolled}/{self.course_capacity}\n' \
            f'{self.faculty}\n' \
            f'{self.room}\n\n'
        
        return text

    def get_info_short(self) -> str:
        text = f'{self.abbr} [{self.course_type}]\n' \
            f'{self.weekdays}: {self.time}\n' \
            f'{self.faculty} | {self.room}\n\n'  # f'{self.enrolled}/{self.course_capacity}\n' \
            
        return text

    def get_course_overall_info(self) -> str:
        text = f'{self.abbr} - {self.title} | ' \
            f'{self.credits_eu} ECTS\n\n'
        
        return text

    def __eq__(self, other):
        if not isinstance(other, Course):
            return False

        return self.abbr == other.abbr and self.course_type == other.course_type
