from src.domain.Student import Student

class StudentRepository:
    def __init__(self, file_path):
        self.file_path = file_path
        self.students = self.load_students()

    def load_students(self):
        students_list = []

        with open(self.file_path, 'r') as file:
            for line in file:
                student_data = line.strip().split(', ')
                student_id = int(student_data[0])
                name = student_data[1]
                attendance_count = int(student_data[2])
                grade = int(student_data[3])
                student = Student(student_id, name, attendance_count, grade)
                students_list.append(student)

        return students_list

    def save_students(self):
        with open(self.file_path, 'w') as file:
            for student in self.students:
                file.write(str(student) + '\n')

    def add_student(self, student):
        """
        Adds a student to the repository
        :param student: Student object
        :return: Adds the student to the repository
        """
        self.students.append(student)
        self.save_students()

    def get_all_students(self):
        return self.students

