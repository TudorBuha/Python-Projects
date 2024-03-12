from src.repository.CoursesRepository import CourseRepository

class CourseUI:
    def __init__(self, repository, service):
        self.repository = repository
        self.service = service

    def display_menu(self):
        print("1. Add a new course")
        print("2. Display all courses")
        print("3. Update instructor")
        print("4. Display courses by instructor's partial string")
        print("0. Exit")

    def run(self):
        while True:
            self.display_menu()
            choice = input("Enter your choice: ")

            if choice == "1":
                self.add_new_course()

            elif choice == "2":
                self.display_courses_sorted()

            elif choice == "3":
                self.update_instructor()

            elif choice == "4":
                self.display_courses_by_instructor()

            elif choice == "0":
                break

            else:
                print("Invalid choice. Please enter a valid option.")

    def add_new_course(self):
        course_id = int(input("Enter course ID: "))

        # Call the service to validate the course ID
        self.service.validate_course_id(self.repository, course_id)

        title = input("Enter course title: ")
        instructor = input("Enter instructor's name: ")
        enrolled_students = int(input("Enter number of enrolled students: "))

        # Call the service to add a new course
        self.service.add_course(self.repository, course_id, title, instructor, enrolled_students)

    def display_courses_sorted(self):
        # Call the service to display courses sorted
        self.service.display_courses_sorted(self.repository)

    def update_instructor(self):
        course_id = int(input("Enter course ID for updating instructor: "))
        new_instructor = input("Enter new instructor's name: ")

        # TODO: Call the service to update the instructor for the specified course

    def display_courses_by_instructor(self):
        instructor_name = input("Enter instructor's name: ")

        # TODO: Call the service to display courses taught by the specified instructor