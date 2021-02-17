from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_bank: QuizBrain):
        self.quiz = quiz_bank
        self.window = Tk()
        self.window.title("Quiz Master")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        # label
        self.score_label = Label(text=f"Score: 0", font=("Arial", 20, "italic"), bg=THEME_COLOR, fg="white")
        self.score_label.grid(row=0, column=1, padx=20, pady=20)

        # Canvas
        self.canvas = Canvas(width=300, height=250, highlightthickness=0, bg="white")
        self.canvas_text = self.canvas.create_text(
            150,
            125,
            width=280,
            font=("Arial", 20, "italic"),
            text="word")
        self.canvas.grid(row=1, column=0, columnspan=2, padx=20, pady=20)

        # Button
        true_img = PhotoImage(file="images/true.png")
        self.true_button = Button(image=true_img, highlightthickness=0, command=self.true_pressed)
        self.true_button.grid(row=2, column=0, padx=20, pady=20)

        false_img = PhotoImage(file="images/false.png")
        self.false_button = Button(image=false_img, highlightthickness=0, command=self.false_pressed)
        self.false_button.grid(row=2, column=1, padx=20, pady=20)
        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.canvas_text, text=q_text)
        else:
            self.canvas.itemconfig(
                self.canvas_text,
                text=f"You have reached the end of the quiz.\nYour total score is: {self.quiz.score}/10"
            )
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")
        self.score_label.config(text=f"Score: {self.quiz.score}")

    def true_pressed(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)

    def false_pressed(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)





