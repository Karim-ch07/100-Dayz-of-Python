from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"
FONT_TPL = ("Arial", 16, "italic")


class QuizUI:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        # Window

        self.window = Tk()
        self.window.title("Quiz Game!")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        # Label

        self.label_score = Label(text="Score: 0", bg=THEME_COLOR, fg="white")
        self.label_score.grid(column=1, row=0)

        # Canvas

        self.canvas = Canvas(width=300, height=250, bg="white", highlightthickness=0)
        self.text_question = self.canvas.create_text(
            150,
            125,
            width=260,
            text="Hey Hey",
            fill=THEME_COLOR,
            font=FONT_TPL
        )
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        # Button

        img_right = PhotoImage(file="./images/true.png")
        self.button_right = Button(image=img_right, width=100, height=100, highlightthickness=0, bg=THEME_COLOR)
        self.button_right.grid(column=1, row=2)

        img_wrong = PhotoImage(file="./images/false.png")
        self.button_wrong = Button(image=img_wrong, width=100, height=100, highlightthickness=0, bg=THEME_COLOR)
        self.button_wrong.grid(column=0, row=2)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        question_text = self.quiz.next_question()
        self.canvas.itemconfig(self.text_question, text=question_text)