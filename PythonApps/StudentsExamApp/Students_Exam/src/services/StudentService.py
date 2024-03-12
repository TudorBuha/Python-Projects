from src.repository.StudentRepository import *

class StudentService:

    @staticmethod
    def validate_student(repository, student_id, name, attendance_count, grade):
        if not StudentService.is_valid_name(name):
            raise ValueError("Invalid name format. Name must have at least 2 words with each word having at least 3 characters.")

        if not StudentService.is_valid_attendance_count(attendance_count):
            raise ValueError("Invalid attendance count. Attendance count must be a positive integer.")

        if not StudentService.is_valid_grade(grade):
            raise ValueError("Invalid grade. Grade must be an integer between 0 and 10.")

        if StudentService.is_duplicate_id(repository, student_id):
            raise ValueError("Duplicate student ID. Student ID must be unique.")

    @staticmethod
    def is_duplicate_id(repository, student_id):
        """
        Checks if a student ID already exists in the repository
        :param repository: the repository object
        :param student_id: the students ID
        :return:
        """
        for student in repository.get_all_students():
            if student.student_id == student_id:
                return True
        return False


    @staticmethod
    def is_valid_name(name):
        """
        Checks if a name is valid
        :param name: string list
        :return: true if the name is valid, false otherwise
        """
        words = name.split()
        ok = False
        for word in words:
            if len(word) >= 3:
                ok = True
        if len(words) >= 2 and ok == True:
            return True
        else:
            return False
    @staticmethod
    def is_valid_attendance_count(attendance_count):
        """
        Checks if an attendance count is valid
        :param attendance_count: number
        :return: true if the attendance count is valid, false otherwise
        """
        ok = False
        if isinstance(attendance_count, int):  # verifica daca attendance_count este de tip int
            ok = True
        if attendance_count >= 0 and ok == True:
            return True
        else:
            return False

    @staticmethod
    def is_valid_grade(grade):
        """
        Checks if a grade is valid
        :param grade: number
        :return: true if the grade is valid, false otherwise
        """
        ok = False
        if isinstance(grade, int): # verifica daca grade este de tip int
            ok = True
        if grade >= 0 and grade <= 10 and ok == True:
            return True
        else:
            return False


    def add_student(self, repository, student_id, name, attendance_count, grade):
        """
        Adds a new student to the repository if it is valid and does not already exist
        :param repository: the repository object
        :param student_id: the student ID
        :param name: the student name
        :param attendance_count: the student attendance count
        :param grade: the student grade
        :return: the student is added to the repository
        """
        try:
            # Validate input
            self.validate_student(repository, student_id, name, attendance_count, grade)

            # Create a new student object
            new_student = Student(student_id, name, attendance_count, grade)

            # Add the new student to the repository
            repository.add_student(new_student)
        except ValueError as e:
            #print(f"Error: {e}")
            raise ValueError(str(e))



    def get_students_sorted(self, repository):
        students = repository.get_all_students()

        # nu sorteaza bine dupa nume alfabetic daca au acelasi note
        #sorted_students = sorted(students, key=lambda student: (student.grade, student.name), reverse=True)
        sorted_students = sorted(students, key=lambda student: student.name)
        sorted_students = sorted(students, key=lambda student: student.grade, reverse=True)

        return sorted_students
        # for student in sorted_students:
        #     print(student)

    def give_bonuses(self, repository, p, b):
        students = repository.get_all_students()

        for student in students:
            if student.attendance_count >= p:
                student.grade += b
                if student.grade > 10:
                    student.grade = 10

        repository.save_students()

    def get_students_by_name(self, repository, search_string):
        students = repository.get_all_students()

        matching_students = []
        for student in students:
            if search_string.lower() in student.name.lower():
                matching_students.append(student)

        return matching_students

        # for student in matching_students:
        #     print(student)
