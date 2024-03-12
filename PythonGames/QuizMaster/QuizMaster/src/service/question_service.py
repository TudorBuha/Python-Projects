from src.domain.question import Question
from src.repository.question_repository import QuestionRepository
import random

class QuestionService:
    def __init__(self, question_repository):
        self.question_repository = question_repository

    def add_question(self, id, text, choices, answer, difficulty):
        question = Question(id, text, choices, answer, difficulty)
        self.question_repository.add_question(question)

    def generate_random_questions(self, num_questions=100):
        difficulties = ['easy', 'medium', 'hard']
        for i in range(1, num_questions + 1):
            text = f"Pseudo-random question {i}"
            choices = ['A', 'B', 'C']
            answer = random.choice(choices)
            difficulty = random.choice(difficulties)
            question = Question(str(i), text, choices, answer, difficulty)
            self.question_repository.add_question(question)

        # Updated to call save_questions without arguments
        self.question_repository.save_questions()

    def get_all_questions(self):
        return self.question_repository.get_questions()

    def get_questions_by_difficulty(self, difficulty):
        return self.question_repository.get_questions(difficulty)