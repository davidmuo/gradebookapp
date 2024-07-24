import json
from student import Student
from course import Course

class GradeBook:
    def __init__(self):
        self.student_list = []
        self.course_list = []
        self.load_data()

    def add_student(self, email, names):
        student = Student(email, names)
        self.student_list.append(student)
        self.save_data()

    def add_course(self, name, trimester, credits):
        course = Course(name, trimester, credits)
        self.course_list.append(course)
        self.save_data()

    def register_student_for_course(self, student_email, course_name, grade=0.0):
        student = next((s for s in self.student_list if s.email == student_email), None)
        course = next((c for c in self.course_list if c.name == course_name), None)
        if student and course:
            student.register_for_course(course, grade)
            self.save_data()

    def calculate_ranking(self):
        return sorted(self.student_list, key=lambda s: s.GPA, reverse=True)

    def search_by_grade(self, min_grade, max_grade):
        return [s for s in self.student_list if min_grade <= s.GPA <= max_grade]

    def generate_transcript(self, student_email):
        student = next((s for s in self.student_list if s.email == student_email), None)
        if student:
            transcript = {
                'email': student.email,
                'names': student.names,
                'courses': [(c['course'].name, c['grade']) for c in student.courses_registered],
                'GPA': student.GPA
            }
            return transcript
        return None

    def save_data(self):
        data = {
            'students': [student.to_dict() for student in self.student_list],
            'courses': [course.to_dict() for course in self.course_list]
        }
        with open('data.json', 'w') as f:
            json.dump(data, f, indent=4)

    def load_data(self):
        try:
            with open('data.json', 'r') as f:
                data = json.load(f)
                self.student_list = [Student.from_dict(s) for s in data['students']]
                self.course_list = [Course.from_dict(c) for c in data['courses']]
        except FileNotFoundError:
            self.student_list = []
            self.course_list = []
