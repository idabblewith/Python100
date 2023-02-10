from days.day_017.files.helpers import *


class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.score = 0
        self.question_list = question_list

    def next_question(self):
        current_q = self.question_list[self.question_number]
        q_text = current_q.text
        q_answer = current_q.answer
        user_answer = (
            nli(f"Question {self.question_number+1}: {q_text} True or False?\n")
        ).capitalize()
        self.check_answer(user_answer, q_answer)

    def check_answer(self, user_answer, q_answer):
        cls()
        if user_answer == "T" or user_answer == "Y":
            user_answer = "True"
        elif user_answer == "F" or user_answer == "N":
            user_answer = "False"
        if user_answer == q_answer:
            self.score += 1
            nls(f"\nCorrect!\nThe answer was: {q_answer}")
        else:
            nls(f"\nIncorrect!\nThe answer was: {q_answer}")
        if self.question_number == len(self.question_list) - 1:
            nls(f"Your final score is: {self.score}/{self.question_number +1}")
        else:
            nls(f"Your current score is: {self.score}/{self.question_number +1}")

        self.question_number += 1
        while self.question_number < len(self.question_list):
            self.next_question()
