from src.services.StudentService import *
from src.ui.UI import StudentUI

if __name__ == "__main__":
    file_path = "students.txt"
    repository = StudentRepository(file_path)
    service = StudentService()

    ui = StudentUI(repository, service)
    ui.run()
