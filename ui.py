from tkinter import *
from quiz_brain import QuizBrain


THEME_COLOR = "#375362"

class QuizInterface:
    def __init__(self,quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("quizzler")
        self.window.config(bg=THEME_COLOR,padx=20,pady=20)

        self.canvas = Canvas(width=300,height=250)
        self.canvas.grid(column=1,row=2,columnspan=2,padx=10,pady=10)
        self.question_text = self.canvas.create_text(150,125,text="some question text",fill = THEME_COLOR,
                                                     font=("Arial",20,"italic"),width=280)

        self.right_img = PhotoImage(file="./images/true.png")
        self.right = Button(image=self.right_img,highlightthickness=0,command=self.true_pressed)
        self.right.grid(column=1,row=3,padx=10,pady=10)

        self.wrong_img = PhotoImage(file="./images/false.png")
        self.wrong = Button(image=self.wrong_img, command=self.false_pressed,highlightthickness=0)
        self.wrong.grid(column=2, row=3, padx=10, pady=10)

        self.score = Label(text=f"Score: 0",bg=THEME_COLOR,fg='white',font=("Arial",15,"italic"))
        self.score.grid(column=2,row=1,pady=10,padx=10)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg='white')
        if self.quiz.still_has_questions():
            self.score.config(text=f"Score : {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text = q_text)
        else:
            self.canvas.itemconfig(self.question_text,text="You have reached the end of quiz.\ncongrats!!!")
            self.right.config(state="disabled")
            self.wrong.config(state="disabled")



    def true_pressed(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)
    def false_pressed(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)
    def give_feedback(self,is_right):
        if is_right:
            self.canvas.config(bg='green')
        else:
            self.canvas.config(bg='red')
        self.window.after(1000,self.get_next_question)
