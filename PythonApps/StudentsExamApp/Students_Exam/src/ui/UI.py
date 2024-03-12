class StudentUI:
    def __init__(self, repository, service):
        self.repository = repository
        self.service = service

    def display_menu(self):
        print("1. Add a new student")
        print("2. Display all students in decreasing order of their grade")
        print("3. Give bonuses")
        print("4. Display all students whose name includes a given string")
        print("0. Exit")

    def run(self):
        while True:
            self.display_menu()
            choice = input("Enter your choice: ")

            if choice == "1":
                self.add_new_student()

            elif choice == "2":
                self.display_students_sorted()

            elif choice == "3":
                self.give_bonuses()

            elif choice == "4":
                self.display_students_by_name()

            elif choice == "0":
                break

            else:
                print("Invalid choice. Please enter a valid option.")

    def add_new_student(self):
        """
        Reads a student from the console and adds it to the repository
        :return:
        """
        student_id = int(input("Enter student ID: "))
        name = input("Enter student name: ")
        attendance_count = int(input("Enter attendance count: "))
        grade = int(input("Enter grade: "))
        #validate inputs
        try:
            self.service.add_student(self.repository, student_id, name, attendance_count, grade)
        except ValueError as e:
            print(f"Error: {e}")



    def display_students_sorted(self):
        sorted_list = self.service.get_students_sorted(self.repository)
        for student in sorted_list:
            print(student)

    def give_bonuses(self):
        p = int(input("Enter attendance count threshold: "))
        b = int(input("Enter bonus value: "))
        self.service.give_bonuses(self.repository, p, b)

    def display_students_by_name(self):
        search_string = input("Enter the search string: ")
        student_list = self.service.get_students_by_name(self.repository, search_string)
        for student in student_list:
            print(student)
