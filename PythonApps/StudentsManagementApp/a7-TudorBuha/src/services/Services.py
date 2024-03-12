from src.repository.Repository import *
from src.domain.Student import *

class Services:
    def __init__(self, repo: Repository):
        self.__repo = repo

    def add(self, student_id, student_name, student_group):
        """
        Adds a student with the given ID, name, and group to the repository.
        :param id: The ID of the student
        :param name: The name of the student
        :param group: The group to which the student belongs
        :return:the Student object with it's properties
        """
        self.__repo.add_student(Student(student_id, student_name, student_group))

    def get_all(self):
        return self.__repo.get_all_students()

    def filter(self, gr):
        self.__repo.filter(gr)

    def undo(self):
        self.__repo.undo()