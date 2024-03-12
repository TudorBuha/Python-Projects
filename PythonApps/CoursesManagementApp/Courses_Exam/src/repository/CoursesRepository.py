from src.domain.Courses import *

class CourseRepository:
    def __init__(self, file_path):
        self.file_path = file_path
        self.courses = self.load_courses()

    def load_courses(self):
        courses = []

        with open(self.file_path, 'r') as file:
            for line in file:
                course_data = line.strip().split(', ')
                course = Course(course_data)
                courses.append(course)

        return courses

    def save_courses(self):
        with open(self.file_path, 'w') as file:
            for course in self.courses:
                file.write(str(course) + '\n')

    def add_course(self, course):
        self.courses.append(course)
        self.save_courses()

    def get_all_courses(self):
        return self.courses