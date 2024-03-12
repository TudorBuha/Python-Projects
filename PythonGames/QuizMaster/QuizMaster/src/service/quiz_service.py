from src.domain.quiz import Quiz
from src.repository.quiz_repository import QuizRepository
import random

class QuizService:
    def __init__(self, question_repository):
        self.question_repository = question_repository

    def create_and_save_quiz(self, difficulty, num_questions, filename):
        all_questions = self.question_repository.get_questions(difficulty)
        if len(all_questions) < num_questions:
            raise ValueError("Not enough questions for the quiz")

        selected_questions = random.sample(all_questions, num_questions)
        quiz = Quiz(selected_questions)

        with open(filename, 'w') as file:
            for question in quiz.questions:
                line = f"{question.text}\nChoices: {', '.join(question.choices)}\nAnswer: {question.answer}\n\n"
                file.write(line)

    def create_quiz(self, number_of_questions, difficulty):
        questions = self.question_repository.get_questions(difficulty)
        if len(questions) < number_of_questions:
            raise ValueError("Not enough questions for the quiz")
        quiz = Quiz(questions[:number_of_questions])
        return quiz

    def answer_question(self, quiz, user_answer):
        if quiz.answer_current_question(user_answer):
            print("Correct!")
        else:
            print("Wrong answer.")
        if quiz.is_complete():
            print(f"Quiz complete! Your score is {quiz.get_score()}.")

    def get_next_question(self, quiz):
        return quiz.next_question()