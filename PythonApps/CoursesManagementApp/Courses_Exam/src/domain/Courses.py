class Course:
    def __init__(self, course_id, title, instructor, enrolled_students):
        self.course_id = course_id
        self.title = title
        self.instructor = instructor
        self.enrolled_students = enrolled_students

    def __str__(self):
        return f"Course ID:{self.course_id}, Title:{self.title}, Instructor:{self.instructor}, Nr of students:{self.enrolled_students}"
