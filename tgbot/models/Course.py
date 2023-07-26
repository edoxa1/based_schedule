class Course:
    def __init__(self, abbr, course_type, title,
                 credits_us, credits_eu,
                 start_date, end_date, weekdays, time,
                 enrolled, course_capacity,
                 faculty, room):
        self.abbr: str = abbr
        self.course_type: str = course_type
        self.title: str = title
        self.credits_us: str = credits_us
        self.credits_eu: str = credits_eu
        self.start_date: str = start_date
        self.end_date: str = end_date
        self.weekdays: str = weekdays
        self.time: str = time
        self.enrolled: str = enrolled
        self.course_capacity: str = course_capacity
        self.faculty: str = faculty
        self.room: str = room

    def get_info(self) -> str:
        text = f'{self.abbr} [{self.course_type}] - {self.title} \n{self.credits_eu} ECTS\n' \
            f'{self.start_date} - {self.end_date}\n' \
            f'{self.weekdays} - {self.time}\n' \
            f'{self.enrolled}/{self.course_capacity}\n' \
            f'{self.faculty}\n' \
            f'{self.room}\n'
        
        return text
