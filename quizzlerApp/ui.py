import tkinter as tk
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = tk.Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        # Centering Window on the Screen and creating window size.
        window_width = 550
        window_height = 800
        screen_width = self.window.winfo_screenwidth()
        screen_height = self.window.winfo_screenheight()

        center_x = int(screen_width / 2 - window_width / 2)
        center_y = int(screen_height / 2 - window_height / 2)

        self.window.geometry(f"{window_width}x{window_height}+{center_x}+{center_y}")

        self.canvas = tk.Canvas(width=500, height=500, bg="white")
        self.question_text = self.canvas.create_text(250, 200, width=240, text="Question", font=("Ariel", 20, "italic"))
        self.canvas.grid(column=0, row=1, columnspan=2)

        self.true_image = tk.PhotoImage(file=".\images\\true.png")
        self.true_button = tk.Button(image=self.true_image, highlightthickness=0, command=self.true_pressed)
        self.true_button.grid(column=0, row=2, pady=20)

        self.false_image = tk.PhotoImage(file=".\images\\false.png")
        self.false_button = tk.Button(image=self.false_image, highlightthickness=0, command=self.false_pressed)
        self.false_button.grid(column=1, row=2)

        self.score_board = tk.Label(text="Score: 0", font=("Ariel", 25), highlightthickness=0, bg=THEME_COLOR,
                                    fg="white")
        self.score_board.grid(column=1, row=0, pady=20)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_board.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the quiz")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def true_pressed(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def false_pressed(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)
