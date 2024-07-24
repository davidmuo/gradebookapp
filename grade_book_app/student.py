# student.py

from course import Course

class Student:
    def __init__(self, email, names):
        self.email = email
        self.names = names
        self.courses_registered = []
        self.GPA = 0.0

    def calculate_GPA(self):
        if not self.courses_registered:
            self.GPA = 0.0
            return
        total_points = sum(course['grade'] * course['course'].credits for course in self.courses_registered)
        total_credits = sum(course['course'].credits for course in self.courses_registered)
        self.GPA = total_points / total_credits if total_credits > 0 else 0.0

    def register_for_course(self, course, grade=0.0):
        self.courses_registered.append({'course': course, 'grade': grade})
        self.calculate_GPA()

    @classmethod
    def from_dict(cls, data):
        student = cls(data['email'], data['names'])
        student.courses_registered = [
            {'course': Course.from_dict(course['course']), 'grade': course['grade']}
            for course in data['courses_registered']
        ]
        student.GPA = data['GPA']
        return student

    def to_dict(self):
        return {
            'email': self.email,
            'names': self.names,
            'courses_registered': [
                {'course': course['course'].to_dict(), 'grade': course['grade']}
                for course in self.courses_registered
            ],
            'GPA': self.GPA
        }
