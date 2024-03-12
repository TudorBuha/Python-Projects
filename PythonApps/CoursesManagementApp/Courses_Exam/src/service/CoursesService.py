from src.domain.Courses import Course
class CourseService:
    @staticmethod
    def validate_course(title, instructor, enrolled_students):
        if not CourseService.is_valid_title(title):
            raise ValueError("Invalid title. Title must be at least 5 characters long.")

        if not CourseService.is_valid_instructor(instructor):
            raise ValueError("Invalid instructor format. Instructor's name must have at least 2 words with each word having at least 3 characters.")

        if not CourseService.is_valid_enrolled_students(enrolled_students):
            raise ValueError("Invalid number of enrolled students. Must be a non-negative integer.")

    @staticmethod
    def is_valid_title(title):
        return len(title) >= 5

    @staticmethod
    def is_valid_instructor(instructor):
        words = instructor.split()
        return len(words) >= 2 and all(len(word) >= 3 for word in words)

    @staticmethod
    def is_valid_enrolled_students(enrolled_students):
        return isinstance(enrolled_students, int) and enrolled_students >= 0

    def validate_course_id(self, repository, course_id):
        if self.is_duplicate_id(repository, course_id):
            raise ValueError("Duplicate course ID. Course ID must be unique.")

    def is_duplicate_id(self, repository, course_id):
        # Check if the course ID already exists in the repository
        return any(course.course_id == course_id for course in repository.get_all_courses())

    def add_course(self, repository, course_id, title, instructor, enrolled_students):
        try:
            # Validate input
            self.validate_course_id(repository, course_id)
            self.validate_course(title, instructor, enrolled_students)

            # Create a new course object
            new_course = Course(course_id, title, instructor, enrolled_students)

            # Add the new course to the repository
            repository.add_course(new_course)
        except ValueError as e:
            print(f"Error: {e}")

    def display_courses_sorted(self, repository):
        # Retrieve all courses from the repository
        courses = repository.get_all_courses()

        # Implement sorting logic
        sorted_courses = sorted(courses, key=lambda course: (course.enrolled_students, course.title.lower()), reverse=True)

        # Display sorted courses
        for course in sorted_courses:
            print(course)
