# Day 17
# Updated 2023, Jarid Prince

# Imports OOP modules
from days.day_017.files.helpers import *
from days.day_017.files.question_model import Question
from days.day_017.files.data import question_data
from days.day_017.files.quiz_brain import QuizBrain


# Main logic
def day_017():
    title("QUIZ")
    question_bank = []

    # Creates a question object per item in question_data and appends it to the bank
    for i in question_data:
        question_text = i["question"]
        question_answer = i["correct_answer"]
        question = Question(question_text, question_answer)
        question_bank.append(question)

    # Shuffles the bank
    random.shuffle(question_bank)

    # Uses bank with QuizBrain and begins questioning
    quiz = QuizBrain(question_bank)
    quiz.next_question()
