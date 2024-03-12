import copy
import pickle
from src.domain.Student import *
import jsonpickle
import json
from random import randint

class Repository:
    def __init__(self):
        self.list = []
        self.history = []

    def generate(self):
        """
        Generates ten students and puts them in the list
        :return:
        """
        for new_id in range(10):
            student_id = new_id
            names_list = ["Cosmin", "Eliza", "Teo", "Mihai", "Andrei", "Otilia", "Daria", "Ioana", "Bianca", "Miruna",
                     "Ilinca", "Andreea"]
            student_name = names_list[randint(0, 11)]
            student_group = randint(910, 917)
            self.list.append(Student(student_id, student_name, student_group))

    def add_student(self, student: Student):
        """
        Adds a student to the list of students and maintains a history of the student list.
        :param student: A Student object representing the student to be added.
        :type student: Student
        """
        self.history.append(copy.deepcopy(self.list))
        self.list.append(student)

    def get_all_students(self):
        return self.list

    def filter(self, group_to_be_removed):
        self.history.append(copy.deepcopy(self.list))

        found = True
        while found == True:
            found = False
            for student in self.list:
                if student.group == group_to_be_removed:
                    self.list.remove(student)
                    found = True


    def undo(self):
        self.list = self.history[-1]
        self.history.pop()


class BinaryRepository(Repository):
    def __init__(self, file_name: str):
        super().__init__()
        self.__file_name = file_name
        self.load()

    def load(self):
        file = open(self.__file_name, "rb")
        self._list = pickle.load(file)
        file.close()

    def save(self):
        file = open(self.__file_name, "wb")
        pickle.dump(self._list, file)
        file.close()

    def filter(self, group: int):
        super().filter(group)
        self.save()

    def add_student(self, student: Student):
        super().add_student(student)
        self.save()

    def undo(self):
        super().undo()
        self.save()


class TextFileRepository(Repository):
    def __init__(self, file_name: str):
        super().__init__()
        self.file_name = file_name
        self.load()

    def load(self):
        student_id = 0
        student_name = 1
        student_group = 2

        file = open(self.file_name, "r")
        values_from_file = file.readlines()
        for value in values_from_file:
            student = value.split("|")
            students_id = int(student[student_id])
            students_name = student[student_name]
            students_group = int(student[student_group])
            self.list.append(Student(students_id, students_name, students_group))

    def save(self):
        value_list = []
        for student in self.list:
            value_list.append(str(student.id) + "|" + student.name + "|" + str(student.group) + '\n')

        file = open(self.file_name, "w")
        file.writelines(value_list)
        file.flush()
        file.close()

    def filter(self, group: int):
        super().filter(group)
        self.save()

    def add_student(self, student: Student):
        super().add_student(student)
        self.save()

    def undo(self):
        super().undo()
        self.save()


class JsonRepository(Repository):
    def __init__(self, file_name: str):
        super().__init__()
        self.__file_name = file_name
        self.load()

    def load(self):
        file = open(self.__file_name, "r")
        self._list = jsonpickle.decode(json.load(file))
        file.close()

    def save(self):
        file = open(self.__file_name, "w")
        json.dump(jsonpickle.encode(self._list), file)
        file.close()

    def filter(self, group: int):
        super().filter(group)
        self.save()

    def add_student(self, student: Student):
        super().add_student(student)
        self.save()

    def undo(self):
        super().undo()
        self.save()


class MemoryRepository(Repository):
    def __init__(self):
        super().__init__()
        self.generate()