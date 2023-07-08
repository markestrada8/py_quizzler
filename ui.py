from tkinter import *
from quiz_brain import QuizBrain

class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.THEME_COLOR = "#375362"
        self.GREEN = "#26AD70"
        self.RED = "#F25B5F"
        self.OFF_WHITE = "#fdffe3"

        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(background=self.THEME_COLOR, padx=20, pady=20)

        self.canvas = Canvas(width=400, height=300, bg="white")
        self.card_text = self.canvas.create_text(
            200,
            150,
            text="Text",
            width=280,
            font=("Arial", 20, "italic")
        )
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        self.score_label = Label(text="Score: 0", fg=self.OFF_WHITE, bg=self.THEME_COLOR, pady=20, padx=20)
        self.score_label.grid(column=1, row=0)

        self.correct_image = PhotoImage(file="images/true.png")
        self.correct_button = Button(image=self.correct_image, command=self.submit_true)
        self.correct_button.grid(column=0, row=2, pady=20)

        self.incorrect_image = PhotoImage(file="images/false.png")
        self.incorrect_button = Button(image=self.incorrect_image, command=self.submit_false)
        self.incorrect_button.grid(column=1, row=2, pady=20)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.set_white()
        if self.quiz.still_has_questions():
            question_text = self.quiz.next_question()
            self.canvas.itemconfig(self.card_text, text=question_text)
            self.score_label.config(text=f"Score: {self.quiz.score}")
        else:
            self.canvas.itemconfig(self.card_text, text="That's all, folks!!!")
            self.incorrect_button.config(state="disabled")
            self.correct_button.config(state="disabled")


    def submit_false(self):
        self.give_feedback(self.quiz.check_answer("False"))
        # self.set_white()
        # self.get_next_question()

    def submit_true(self):
        self.give_feedback(self.quiz.check_answer("True"))
        # self.set_white()
        # self.get_next_question()

    def set_red(self):
        self.canvas.config(bg=self.RED)

    def set_green(self):
        self.canvas.config(bg=self.GREEN)

    def set_white(self):
        self.canvas.config(bg=self.OFF_WHITE)

    def give_feedback(self, is_right):
        if is_right:
            self.set_green()
        else:
            self.set_red()

        self.window.after(1000, self.get_next_question)

