from dataclasses import dataclass
from typing import Literal

@dataclass
class Student:
    first_name: str
    last_name: str
    email: str
    gender: Literal['Male', 'Female', 'Other']
    mobile_number: str
    date_of_birth: str
    subjects: str
    hobbies: Literal['Sports', 'Reading', 'Music']
    picture: str
    address: str
    state: str
    city: str

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    @property
    def state_and_city(self):
        return f"{self.state} {self.city}"


def create_student():
    return Student(
        first_name='Alex',
        last_name='Alexov',
        email='alex.alexov@mail.ru',
        gender='Male',
        mobile_number='1234567890',
        date_of_birth='26 November,1990',
        subjects='History',
        hobbies='Reading',
        picture='foto.jpg',
        address='address',
        state='NCR',
        city='Delhi'
    )