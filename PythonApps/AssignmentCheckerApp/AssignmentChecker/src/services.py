from repository import AssignmentRepository
from domain import Assignment

class AssignmentService:
    def __init__(self, repository):
        self.repository = repository

    def add_assignment(self, assignment):
        # Validate and add assignment
        if self.validate_assignment(assignment):
            self.repository.add_assignment(assignment)
        else:
            print("Error: Invalid assignment. Please check the input.")

    def get_all_assignments(self):
        # Return a list of all assignments
        return self.repository.read_assignments()

    def dishonesty_check(self):
        assignments = self.get_all_assignments()
        for i in range(len(assignments)):
            for j in range(i + 1, len(assignments)):
                common_words_percentage = self.calculate_common_words_percentage(assignments[i].solution, assignments[j].solution)
                if common_words_percentage >= 20:
                    print(f"{assignments[i].student_name} -> {assignments[j].student_name} ({common_words_percentage}% of {assignments[j].student_name}'s solution)")
                    #print(f"{assignments[j].student_name} -> {assignments[i].student_name} ({common_words_percentage}% of {assignments[i].student_name}'s solution)")
                    print()

    def calculate_common_words_percentage(self, solution1, solution2):
        words1 = set(solution1.split())
        words2 = set(solution2.split())
        common_words = words1.intersection(words2)
        return (len(common_words) / len(words1)) * 100 if len(words1) > 0 else 0

    def validate_assignment(self, assignment):
        # Validate assignment fields
        if not isinstance(assignment.assignment_id, int) or assignment.assignment_id < 0:
            return False
        if not isinstance(assignment.student_name, str) or len(assignment.student_name) < 3:
            return False
        if not isinstance(assignment.solution, str) or not assignment.solution:
            return False
        return True
