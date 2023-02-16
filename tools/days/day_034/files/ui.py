from days.day_034.files.quiz_brain import QuizBrain
from days.day_034.files.helpers import *


class QuizInterface:
    # Set up
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_int = 0
        self.score = Label(text=f"Score: {self.score_int}", bg=THEME_COLOR, fg="white")
        self.score.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(
            150,
            125,
            text="goes here",
            width=280,
            font=("Arial", 21, "italic"),
            fill=THEME_COLOR,
        )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        true_img = PhotoImage(file="./tools/days/day_034/files/images/true.png")
        false_img = PhotoImage(file="./tools/days/day_034/files/images/false.png")
        self.true_btn = Button(
            image=true_img,
            bg="green",
            fg="white",
            highlightthickness=0,
            command=self.true_pressed,
        )
        self.false_btn = Button(
            image=false_img,
            bg="red",
            fg="white",
            highlightthickness=0,
            command=self.false_pressed,
        )
        self.true_btn.grid(row=2, column=0)
        self.false_btn.grid(row=2, column=1)

        # Init
        self.get_next_question()
        self.window.mainloop()

    # Pull next question in
    def get_next_question(self):
        self.canvas.config(bg="white")
        self.true_btn.config(state="active")
        self.false_btn.config(state="active")
        self.score["text"] = f"Score: {self.score_int}"
        if self.quiz.still_has_questions() == True:
            qt = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=qt)
        else:
            self.canvas.itemconfig(self.question_text, text="No more questions.")
            self.true_btn.config(state="disabled")
            self.false_btn.config(state="disabled")

    # True Pressed Handler
    def true_pressed(self):
        is_correct = self.quiz.check_answer("True")
        if is_correct == True:
            self.score_int += 1
        self.visual_feedback(is_correct)

    # False Pressed Handler
    def false_pressed(self):
        is_correct = self.quiz.check_answer("False")
        if is_correct == True:
            self.score_int += 1
        self.visual_feedback(is_correct)

    # Visual Feedback depending on answer
    def visual_feedback(self, is_correct):
        self.true_btn.config(state="disabled")
        self.false_btn.config(state="disabled")
        if is_correct == True:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        # proceed to next question after 1s
        self.window.after(1000, self.get_next_question)
