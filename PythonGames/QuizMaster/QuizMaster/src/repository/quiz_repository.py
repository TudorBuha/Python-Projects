from src.domain.quiz import Quiz
from src.repository.question_repository import QuestionRepository

class QuizRepository:
    def __init__(self, filename):
        self.filename = filename
        self.question_repository = QuestionRepository(filename)

    def load_quiz(self):
        questions = self.question_repository.load_questions()
        return Quiz(questions)

    def save_quiz(self, quiz):
        self.question_repository.save_questions(quiz.questions)
