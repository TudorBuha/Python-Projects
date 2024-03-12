from src.service.quiz_service import QuizService
from src.service.question_service import QuestionService
from src.repository.question_repository import QuestionRepository
from src.domain.quiz import Quiz
from src.domain.question import Question



class QuizUI:
    def __init__(self):
        question_repository = QuestionRepository("questions.txt")
        self.question_service = QuestionService(question_repository)
        self.quiz_service = QuizService(question_repository)

    def start(self):
        print("Welcome to the Quiz Program!")
        while True:
            print("\nChoose an option:")
            print("1. Create a new quiz")
            print("2. Take a quiz")
            print("3. Start a quiz from a file")
            print("4. Exit")
            choice = input("> ")

            if choice == '1':
                self.create_quiz_ui()
            elif choice == '2':
                self.take_quiz_ui()
            elif choice == '3':
                filename = input("Enter the filename of the quiz to start: ")
                self.start_quiz_from_file(filename)
            elif choice == '4':
                print("Exiting the program.")
                break
            else:
                print("Invalid option. Please try again.")

    def create_quiz_ui(self):
        print("Creating a new quiz:")
        difficulty = input("Enter the difficulty level (easy, medium, hard): ")
        num_questions = int(input("Enter the number of questions for the quiz: "))
        filename = input("Enter the filename for the new quiz: ")

        try:
            self.quiz_service.create_and_save_quiz(difficulty, num_questions, filename)
            print(f"Quiz created and saved in {filename}")
        except ValueError as e:
            print(e)

    def take_quiz_ui(self):
        num_questions = int(input("Enter the number of questions for the quiz: "))
        difficulty = input("Enter the difficulty level (easy, medium, hard): ")
        try:
            quiz = self.quiz_service.create_quiz(num_questions, difficulty)
            while True:
                question = self.quiz_service.get_next_question(quiz)
                if question is None:
                    break
                print(question.text)
                for i, choice in enumerate(question.choices, 1):
                    print(f"{i}. {choice}")
                answer = input("Your answer (1-3): ")
                self.quiz_service.answer_question(quiz, question.choices[int(answer) - 1])
            print(f"Quiz finished! Your final score is {quiz.get_score()}.")
        except ValueError as e:
            print(e)

    def start_quiz_from_file(self, filename):
        try:
            with open(filename, 'r') as file:
                content = file.readlines()

            questions = self.parse_questions_from_file(content)
            quiz = Quiz(questions)
            self.run_quiz(quiz)
        except FileNotFoundError:
            print(f"File not found: {filename}")
        except Exception as e:
            print(f"An error occurred: {e}")

    def parse_questions_from_file(self, content):
        questions = []
        question_text = ""
        choices = []
        answer = ""
        for line in content:
            if line.startswith("Choices:"):
                choices = line.split(':')[1].strip().split(', ')
            elif line.startswith("Answer:"):
                answer = line.split(':')[1].strip()
                # Create a question object
                question = Question("", question_text, choices, answer, "")  # ID and difficulty are not used here
                questions.append(question)
                question_text = ""
                choices = []
            else:
                question_text += line.strip() + " "

        return questions

    def run_quiz(self, quiz):
        correct_answers = 0
        total_questions = len(quiz.questions)

        for question in quiz.questions:
            print(question.text)
            for i, choice in enumerate(question.choices, 1):
                print(f"{i}. {choice}")
            user_answer = input("Your answer: ")

            if user_answer.lower() == question.answer.lower():
                print("Correct!")
                correct_answers += 1
            else:
                print("Incorrect. The correct answer was " + question.answer)
            print()

        score = correct_answers / total_questions * 100
        print(f"Quiz complete! Your score is {score:.2f}% ({correct_answers} out of {total_questions} correct).")

# Main execution
if __name__ == '__main__':
    ui = QuizUI()
    ui.start()