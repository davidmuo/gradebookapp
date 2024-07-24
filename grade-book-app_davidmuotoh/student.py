class Student:
    def __init__(self, email, names, courses_registered=None, GPA=0.0):
        self.email = email
        self.names = names
        self.courses_registered = courses_registered if courses_registered else []
        self.GPA = GPA

    def calculate_GPA(self):
        if not self.courses_registered:
            self.GPA = 0.0
        else:
            total_credits = sum(course['course'].credits for course in self.courses_registered)
            total_points = sum(course['grade'] * course['course'].credits for course in self.courses_registered)
            self.GPA = total_points / total_credits if total_credits != 0 else 0.0

    def register_for_course(self, course, grade=0.0):
        self.courses_registered.append({'course': course, 'grade': grade})
        self.calculate_GPA()

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

    @classmethod
    def from_dict(cls, data):
        courses_registered = [
            {'course': Course.from_dict(course['course']), 'grade': course['grade']}
        ]
        return cls(data['email'], data['names'], courses_registered, data['GPA'])
