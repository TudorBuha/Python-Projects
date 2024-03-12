from src.domain import Assignment

class AssignmentRepository:
    def __init__(self, file_path):
        self.file_path = file_path

    def read_assignments(self):
        assignments = []
        with open(self.file_path, 'r') as file:
            for line in file:
                parts = line.strip().split(', ')
                assignment_id, student_name, solution = map(str.strip, parts)
                assignments.append(Assignment(int(assignment_id), student_name, solution))

        return assignments

    def add_assignment(self, assignment):
        assignments = self.read_assignments()
        assignments.append(assignment)
        with open(self.file_path, 'w') as file:
            for assignment in assignments:
                file.write(f"{assignment.assignment_id}, {assignment.student_name}, {assignment.solution}\n")

