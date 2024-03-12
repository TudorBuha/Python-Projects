from src.repository import AssignmentRepository
from src.services import AssignmentService
from src.domain import Assignment

class AssignmentUI:
    def __init__(self, service):
        self.service = service

    def start(self):
        while True:
            print("\n1. Add Assignment")
            print("2. Display All Assignments")
            print("3. Dishonesty Check")
            print("4. Exit")

            choice = input("Enter your choice: ")

            if choice == '1':
                self.add_assignment()
            elif choice == '2':
                self.display_all_assignments()
            elif choice == '3':
                self.dishonesty_check()
            elif choice == '4':
                print("Exiting the program.")
                break
            else:
                print("Invalid choice. Please try again.")

    def add_assignment(self):
        try:
            assignment_id = int(input("Enter assignment id: "))
            student_name = input("Enter student name: ")
            solution = input("Enter solution: ")

            assignment = Assignment(assignment_id, student_name, solution)
            self.service.add_assignment(assignment)

            print("Assignment added successfully.")
        except ValueError:
            print("Error: Invalid input for assignment id. Please enter a valid integer.")

    def display_all_assignments(self):
        assignments = self.service.get_all_assignments()
        if assignments:
            print("\nAll Assignments:")
            for assignment in assignments:
                print(f"{assignment.assignment_id}, {assignment.student_name}, {assignment.solution}")
        else:
            print("No assignments available.")

    def dishonesty_check(self):
        print("\nDishonesty Check:")
        self.service.dishonesty_check()



if __name__ == "__main__":
    repository = AssignmentRepository("assignments.txt")
    service = AssignmentService(repository)
    ui = AssignmentUI(service)
    ui.start()