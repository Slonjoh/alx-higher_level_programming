#!/usr/bin/python3
"""
A class Student that defines a student by: (based on 9-student.py)
"""


class Student:
    """
    A class representing a student.
    """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Returns a dictionary representation of the student.
        """
        student_dict = {}
        if attrs is None:
            for key, value in self.__dict__.items():
                student_dict[key] = value
        else:
            for attr in attrs:
                if hasattr(self, attr):
                    student_dict[attr] = getattr(self, attr)
        return student_dict
