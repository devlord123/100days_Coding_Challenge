from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"



class interface:

    def __init__(self, quiz_brain:QuizBrain):
        self.quiz = quiz_brain
        self.windows = Tk()
        self.windows.config(padx=50, pady=50, bg=THEME_COLOR)
        self.windows.title("Quizzler")

        self.score_lab = Label(text="Score: 0", fg="white", bg=THEME_COLOR)
        self.score_lab.grid(column=1, row=0)

        self.canvas = Canvas(width=300, height=200, bg="white")
        self.question = self.canvas.create_text(150, 100, text="Hello some text",
                                                fill=THEME_COLOR,
                                                font=("Arial", 16, "normal"),
                                                width=280
                                                )

        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        self.false_img = PhotoImage(file="images/false.png")
        self.false = Button(image=self.false_img, highlightthickness=0, command=self.wrong)
        self.false.grid(column=0, row=2)

        self.right_img = PhotoImage(file="images/true.png")
        self.right = Button(image=self.right_img, highlightthickness=0, command=self.correct)
        self.right.grid(column=1, row=2)
        self.get_next_question()

        self.windows.mainloop()


    def get_next_question(self):
        if self.quiz.still_has_questions():
            self.canvas.config(bg='white')
            self.score_lab.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question, text=q_text)
        else:
            self.canvas.itemconfig(self.question, text="You have reached the end of the quiz.")
            self.canvas.config(bg="white")

    def wrong(self):
        isright = self.quiz.check_answer("False")
        self.feedback(isright)

    def correct(self):
        self.feedback(self.quiz.check_answer("True"))


    def feedback(self, isright):
        if isright:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.windows.after(1000, self.get_next_question)





