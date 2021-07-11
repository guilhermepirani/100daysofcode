import tkinter as tk
from quiz_brain import QuizBrain
from data import get_questions


THEME_COLOR = "#375362"

class OptionsInterface():
    def __init__(self):
        self.window = tk.Tk()
        self.window.title('Quiz App')
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        self.v = tk.IntVar(value=9)
        self.d = tk.StringVar(value='easy')

        tk.Label(text='Choose a category and difficulty:', bg=THEME_COLOR, fg='white').pack()
 
        # Buttons
        categories = {
            "General Knowledge" : 9,
            "Books" : 10,
            "Films" : 11,
            "Video Games" : 15,
            "Anime & Manga" : 31,
            "Animals": 27,
            "Computers": 18,
            "History": 23,
            "Geography": 22,
            "Sports": 21
        }
        
        for (text, value) in categories.items():
            tk.Radiobutton(
                self.window,
                text = text,
                variable = self.v,
                value = value,
                bg = THEME_COLOR,
                fg='white',
                selectcolor='gray',
                activebackground=THEME_COLOR,
            ).pack(anchor='w', padx=20, pady=5)

        tk.Label(text='-------------', bg=THEME_COLOR, fg='white').pack()

        difficulties = {
            "Easy" : 'easy',
            "Medium" : 'medium',
            "Hard" : 'hard',
        }

        for (text, value) in difficulties.items():
            tk.Radiobutton(
                self.window,
                text = text,
                variable = self.d,
                value = value,
                bg = THEME_COLOR,
                fg='white',
                selectcolor='gray',
                activebackground=THEME_COLOR,
            ).pack(anchor='w', padx=20, pady=5)

        tk.Label(text='This window will refresh if not enough questions are found', bg=THEME_COLOR, fg='white').pack()

        self.start_button = tk.Button(text='Start Game', width=30, command=self.window.destroy).pack(pady=10)
       

        self.window.mainloop()


class QuizInterface():
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = tk.Tk()
        self.window.title('Quiz App')
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        # Score label
        self.score_label = tk.Label(text='Score: 0', bg=THEME_COLOR, fg='white', font=('Arial', 12))
        self.score_label.grid(row=0, column=1)

        # Card
        self.canvas = tk.Canvas(width=300, height=250, bg='white')
        self.question_text = self.canvas.create_text(
            150, 125, width=280,
            text='',
            font=('Arial', 16, 'italic'),
            fill=THEME_COLOR
        )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        # Buttons
        TRUE_IMG = tk.PhotoImage(file='C:/100daysofcode/day034/usequizapi/images/true.png')
        FALSE_IMG = tk.PhotoImage(file='C:/100daysofcode/day034/usequizapi/images/false.png')

        self.true_btn = tk.Button(image=TRUE_IMG, bg=THEME_COLOR, bd=0, highlightthickness=0, command=self.true_pressed)
        self.true_btn.grid(row=2, column=1)
        self.false_btn = tk.Button(image=FALSE_IMG, bg=THEME_COLOR, bd=0, highlightthickness=0, command=self.false_pressed)
        self.false_btn.grid(row=2, column=0)

        # Initialize quiz
        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg='white')
        self.true_btn.config(state='normal')
        self.false_btn.config(state='normal')
        if self.quiz.still_has_questions():
            self.score_label.config(text=f'Score: {self.quiz.score}')
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text='You\'ve reached the end of the quiz.')
            self.true_btn.config(state='disabled')
            self.false_btn.config(state='disabled')

    def true_pressed(self):
        self.give_feedback(self.quiz.check_answer('True'))

    def false_pressed(self):
        self.give_feedback(self.quiz.check_answer('False'))

    def give_feedback(self, scored):
        self.true_btn.config(state='disabled')
        self.false_btn.config(state='disabled')
        if scored:
            self.canvas.config(bg='#6bd154')
        else:
            self.canvas.config(bg='#eb4444')
        self.window.after(2000, self.get_next_question)