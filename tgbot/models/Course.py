from typing import List, Dict


class Course:
    def __init__(self, abbr, course_type, title,
                 credits_us, credits_eu,
                 start_date, end_date, weekdays, time,
                 enrolled, course_capacity,
                 faculty, room, room_capacity):
        self.abbr = abbr
        self.course_type = course_type
        self.title = title
        self.credits_us = credits_us
        self.credits_eu = credits_eu
        self.start_date = start_date
        self.end_date = end_date
        self.weekdays = weekdays
        self.time = time
        self.enrolled = enrolled
        self.course_capacity = course_capacity
        self.faculty = faculty
        self.room = room
        self.room_capacity = room_capacity



