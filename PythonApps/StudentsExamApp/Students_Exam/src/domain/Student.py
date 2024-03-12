class Student:
    def __init__(self, student_id, name, attendance_count, grade):
        self.student_id = student_id
        self.name = name
        self.attendance_count = attendance_count
        self.grade = grade

    def __str__(self):
        return f"{self.student_id}, {self.name}, {self.attendance_count}, {self.grade}"
