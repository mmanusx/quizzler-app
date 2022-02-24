from tkinter import *
from quiz_brain import QuizBrain


THEME_COLOR = "#375362"

class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        # Score Text / Label
        self.score_text = Label(text="Score:0",fg="white", bg=THEME_COLOR)
        self.score_text.grid(row=0, column=1)

        # Canvas
        self.canvas = Canvas(width=300, height=250)
        self.question_text = self.canvas.create_text(150, 125,
                                                     text="Question", # first two argüment is position arguments
                                                     fill=THEME_COLOR,
                                                     width=280, # to wrap text for if too long text line
                                                     font=("Arial", 20, "italic"))
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        # Buttons
        true_image = PhotoImage(file="images/true.png") #burada self yazmamıza gerek yok classda başka bir yerde kullanmayacağız
        self.true_button = Button(image=true_image, highlightthickness=0, command=self.push_true)
        self.true_button.grid(row=2, column=0)

        false_image = PhotoImage(file="images/false.png")
        self.false_button = Button(image=false_image, highlightthickness=0, command=self.push_false)
        self.false_button.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")  # renk değişimdinden sonra bg u resetledim
        if self.quiz.still_has_questions():
            self.score_text.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the quiz.")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def push_true(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def push_false(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, is_right):
        if is_right:
            color = "green"
            self.canvas.config(bg=color)
        else:
            color = "red"
            self.canvas.config(bg=color)
        self.window.after(1000, self.get_next_question) # tkinter da sleep metodunu kullanamıyoruz
