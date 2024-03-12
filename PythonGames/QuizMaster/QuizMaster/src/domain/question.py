class Question:
    def __init__(self, id, text, choices, answer, difficulty):
        self.id = id
        self.text = text
        self.choices = choices
        self.answer = answer
        self.difficulty = difficulty

    def check_answer(self, user_answer):
        return self.answer == user_answer

    def get_points(self):
        difficulty_points = {'easy': 1, 'medium': 2, 'hard': 3}
        return difficulty_points.get(self.difficulty, 0)
