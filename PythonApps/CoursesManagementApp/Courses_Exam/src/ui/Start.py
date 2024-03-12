from src.service.CoursesService import CourseService
from src.repository.CoursesRepository import CourseRepository
from src.ui.UI import CourseUI

if __name__ == "__main__":
    file_path = "mathematica.txt"
    repository = CourseRepository(file_path)
    service = CourseService()

    ui = CourseUI(repository, service)
    ui.run()
