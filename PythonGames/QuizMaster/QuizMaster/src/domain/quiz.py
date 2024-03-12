from src.domain.question import Question

class Quiz:
    def __init__(self, questions=[]):
        self.questions = questions
        self.current_question_index = -1
        self.score = 0

    def add_question(self, question):
        if isinstance(question, Question):
            self.questions.append(question)

    def next_question(self):
        self.current_question_index += 1
        if self.current_question_index < len(self.questions):
            return self.questions[self.current_question_index]
        else:
            return None

    def answer_current_question(self, user_answer):
        current_question = self.questions[self.current_question_index]
        if current_question.check_answer(user_answer):
            self.score += current_question.get_points()
            return True
        return False

    def is_complete(self):
        return self.current_question_index == len(self.questions) - 1

    def get_score(self):
        return self.score
