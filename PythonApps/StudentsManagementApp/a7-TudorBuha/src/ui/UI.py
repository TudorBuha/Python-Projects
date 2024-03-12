from src.services.Services import *
from jproperties import Properties

class UI:
    def __init__(self, service: Services):
        self.service = service
    def menu(self):
        print("Menu")
        print("1 - Add a student")
        print("2 - Display the list of students")
        print("3 - Filter the list so that students in a given group are deleted from the list")
        print("4 - Undo")
        print("0 - Exit")

    def start(self):

        add_student = 1
        display_list = 2
        filter_list = 3
        undo = 4
        exit = 0
        while True:
            try:
                self.menu()
                users_choice = int(input(">>"))
                if users_choice == add_student:
                    print("Introduce the ID of the student")
                    students_id = int(input())
                    print("Introduce the name of the student")
                    students_name = input()
                    print("Introduce the group")
                    students_group = int(input())
                    self.service.add(students_id, students_name, students_group)
                elif users_choice == display_list:
                    for student in self.service.get_all():
                        print(student)
                elif users_choice == filter_list:
                    print("Introduce the group that will be removed")
                    students_group_to_be_removed = int(input())
                    self.service.filter(students_group_to_be_removed)
                elif users_choice == undo:
                    self.service.undo()
                elif users_choice == exit:
                    print("Bye!")
                    break
                else:
                    print("Invalid option!")
            except Exception as ex:
                print(ex)


if __name__ == "__main__":
    repository = Repository()
    config = Properties()

    config_file = open("settings.properties", "rb")
    config.load(config_file)

    repository_type = config.get("repo_type").data

    if repository_type == "memory":
        repository = MemoryRepository()
    elif repository_type == "txt":
        file_name = config.get("text_file_name").data
        repository = TextFileRepository(file_name)
    elif repository_type == "bin":
        file_name = config.get("binary_name").data
        repository = BinaryRepository(file_name)
    elif repository_type == "json":
        file_name = config.get("json_name").data
        repository = JsonRepository(file_name)

    service = Services(repository)
    ui = UI(service)
    ui.start()