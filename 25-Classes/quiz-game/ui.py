from tkinter import *
from quiz_brain import QuizBrain

# Constants:
THEME_COLOR = "#375362"
BG_LIGHT = "#F9FEFF"
BG_RIGHT = "#E7FFCA"
BG_WRONG = "#FFD1CA"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):  # IMPORTANT: "quiz_brain: QuizBrazil" is setting data type "QuizBrain"
        self.quiz = quiz_brain
        # window:
        self.window = Tk()
        self.window.title("Quizzler by @aldolammel")
        self.window.minsize(width=0, height=0)
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        # canvas:
        self.canvas = Canvas(width=300, height=250)
        self.canvas.config(highlightthickness=0, bg=BG_LIGHT)
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)
        # labels:
        self.lb_score = Label(
            text="Score: 0",
            font=("Arial", 12, "normal"),
            fg="#FFFFFF",
            bg=THEME_COLOR
        )
        self.lb_score.grid(column=1, row=0)
        self.txt_question = self.canvas.create_text(
            150, 125,  # to centralize, set the half values of canvas size ;)
            width=280,  # force the text to wrap.
            text="",
            font=("Arial", 20, "italic"),
            fill=THEME_COLOR
        )
        # images:
        img_true = PhotoImage(file="images/true.png")  # doesn't need "self." 'cause it won't be used somewhere else.
        img_false = PhotoImage(file="images/false.png")  # doesn't need "self." 'cause it won't be used somewhere else.
        # buttons:
        self.bt_true = Button(image=img_true, highlightthickness=0, command=self.true_pressed)
        self.bt_true.grid(column=0, row=2)
        self.bt_false = Button(image=img_false, highlightthickness=0, command=self.false_pressed)
        self.bt_false.grid(column=1, row=2)
        # load the first question:
        self.get_next_question()
        # screen update:
        self.window.mainloop()  # keep the Tkinter window on screen

    def get_next_question(self):
        # Reset the bg color:
        self.canvas.config(bg=BG_LIGHT)
        # Update the scoreboard:
        self.lb_score.config(text=f"Score: {self.quiz.score}")
        # Check the number of questions available:
        if self.quiz.still_has_questions():
            # Load the next question:
            q_text = self.quiz.next_question()
            # Show the next question:
            self.canvas.itemconfig(self.txt_question, text=q_text)
        else:
            self.canvas.itemconfig(self.txt_question, text="Done!")
            self.bt_true.config(state="disabled")
            self.bt_false.config(state="disabled")

    def true_pressed(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def false_pressed(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, is_right: bool):
        if is_right:
            self.canvas.config(bg=BG_RIGHT)
        else:
            self.canvas.config(bg=BG_WRONG)
        self.window.after(1500, self.get_next_question)  # SLEEP substitute for TKinter. Here, 1.5 seconds of delay.
