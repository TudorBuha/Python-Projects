from src.domain.question import Question

class QuestionRepository:
    def __init__(self, filename):
        self.filename = filename
        self.questions = self.load_questions()  # Load questions immediately

    def load_questions(self):
        questions = []
        try:
            with open(self.filename, 'r') as file:
                for line in file:
                    parts = line.strip().split(';')
                    if len(parts) == 7:
                        id, text, choice_a, choice_b, choice_c, answer, difficulty = parts
                        question = Question(id, text, [choice_a, choice_b, choice_c], answer, difficulty)
                        questions.append(question)
        except FileNotFoundError:
            pass  # If the file does not exist, return an empty list
        return questions

    def add_question(self, question):
        if isinstance(question, Question):
            self.questions.append(question)

    def get_questions(self, difficulty=None):
        if difficulty:
            return [question for question in self.questions if question.difficulty == difficulty]
        return self.questions

    def save_questions(self):
        with open(self.filename, 'w') as file:
            for question in self.questions:
                line = f"{question.id};{question.text};{question.choices[0]};{question.choices[1]};{question.choices[2]};{question.answer};{question.difficulty}\n"
                file.write(line)