from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"
WHITE_COLOR = "#FFFFFF"

class Quiz_Interface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        self.canvas = Canvas(height=250, width=300, bg=WHITE_COLOR, highlightthickness=0)
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        # BUTTONS
        image_true = PhotoImage(file="./images/true.png")
        self.button_true = Button(image=image_true, highlightthickness=0, command=self.true_button)
        self.button_true.grid(column=0, row=2)

        image_false = PhotoImage(file="./images/false.png")
        self.button_false = Button(image=image_false, highlightthickness=0, command=self.false_button)
        self.button_false.grid(column=1, row=2)

        # TEXT
        self.score_text = Label(text="Score:0", font=("Arial", 12, "normal"), fg="white", bg=THEME_COLOR)
        self.score_text.grid(column=1, row=0)

        self.question_text = self.canvas.create_text(
            150,
            125,
            width=280,
            text="Score:0",
            font=("Arial", 20, "italic"),
            fill=THEME_COLOR
        )

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_text.config(text=f"Score:{self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the quiz.")
            self.button_true.config(state="disabled")
            self.button_false.config(state="disabled")

    def true_button(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def false_button(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)
    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")

        self.window.after(1000, self.get_next_question)
