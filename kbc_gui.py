import tkinter as tk
from tkinter import messagebox, ttk
from questions import questions
import pygame
import random

pygame.mixer.init()

# Load sounds
correct_sound = pygame.mixer.Sound("correct.wav")
wrong_sound = pygame.mixer.Sound("wrong.wav")
# Color theme for Dark Mode Quiz App
BG_COLOR = "#1E1E1E"
FRAME_COLOR = BG_COLOR  # Unified dark background
TEXT_COLOR = "#E0E0E0"
HEADER_TEXT_COLOR = "#FFFFFF"

PRIMARY_BTN_COLOR = "#3A86FF"
SECONDARY_BTN_COLOR = "#72EFDD"

CORRECT_COLOR = "#06D6A0"
WRONG_COLOR = "#FF6B6B"

BTN_HOVER_COLOR = "#4CC9F0"
HIGHLIGHT_COLOR = "#C77DFF"

SCOREBOARD_BG = "#2A2A72"

class KBCApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("KBC Game - Quiz")
        self.geometry("700x500")
        self.configure(bg=BG_COLOR)

        self.username = ""
        self.current_frame = None

        self.current_question_index = 0
        self.selected_questions = []
        self.score = 0

        # Progress bar styling
        style = ttk.Style()
        style.theme_use('default')
        style.configure("TProgressbar", thickness=6, troughcolor=BG_COLOR, background=PRIMARY_BTN_COLOR)

        self.show_login_page()

    def clear_frame(self):
        if self.current_frame:
            self.current_frame.destroy()

    def show_login_page(self):
        self.clear_frame()
        self.current_frame = tk.Frame(self, bg=FRAME_COLOR)
        self.current_frame.pack(pady=80, padx=40)

        tk.Label(self.current_frame, text="KBC Game", font=("Arial", 28, "bold"),
                 fg=TEXT_COLOR, bg=FRAME_COLOR).pack(pady=20)

        tk.Label(self.current_frame, text="Enter Your Name:", font=("Arial", 16),
                 fg=TEXT_COLOR, bg=FRAME_COLOR).pack(pady=10)
        name_entry = tk.Entry(self.current_frame, font=("Arial", 16))
        name_entry.pack()

        def proceed():
            name = name_entry.get().strip()
            if name:
                self.username = name
                self.show_category_page()
            else:
                messagebox.showerror("Error", "Please enter your name!")

        proceed_btn = tk.Button(self.current_frame, text="Proceed", font=("Arial", 16, "bold"),
                                bg=PRIMARY_BTN_COLOR, fg=TEXT_COLOR, activebackground=BTN_HOVER_COLOR,
                                command=proceed)
        proceed_btn.pack(pady=30)

    def show_category_page(self):
        self.clear_frame()
        self.current_frame = tk.Frame(self, bg=FRAME_COLOR)
        self.current_frame.pack(pady=40)

        tk.Label(self.current_frame, text=f"Welcome, {self.username}!", font=("Arial", 22, "bold"),
                 fg=TEXT_COLOR, bg=FRAME_COLOR).pack(pady=10)

        tk.Label(self.current_frame, text="Select a Category", font=("Arial", 18),
                 fg=TEXT_COLOR, bg=FRAME_COLOR).pack(pady=20)

        category_box = tk.Frame(self.current_frame, bg=FRAME_COLOR)
        category_box.pack()

        categories = list(questions.keys())

        for category in categories:
            btn = tk.Button(category_box, text=category, font=("Arial", 16, "bold"),
                            width=25, bg=PRIMARY_BTN_COLOR, fg=TEXT_COLOR, activebackground=BTN_HOVER_COLOR,
                            command=lambda c=category: self.start_quiz(c))
            btn.pack(pady=10)

    def start_quiz(self, category):
        self.selected_questions = questions[category]
        self.current_question_index = 0
        self.score = 0
        self.show_question()

    def show_question(self):
        self.clear_frame()
        self.current_frame = tk.Frame(self, bg=FRAME_COLOR)
        self.current_frame.pack(pady=30, padx=40)

        total_questions = len(self.selected_questions)
        question_number = self.current_question_index + 1
        current_q = self.selected_questions[self.current_question_index]

        # ✅ Question Counter Text
        tk.Label(self.current_frame, text=f"Question {question_number} / {total_questions}",
                 font=("Arial", 20, "bold"), fg=TEXT_COLOR, bg=FRAME_COLOR).pack(pady=(10, 5))

        # ✅ Progress Bar
        progress = ttk.Progressbar(self.current_frame, length=500, mode='determinate')
        progress_percentage = (question_number / total_questions) * 100
        progress['value'] = progress_percentage
        progress.pack(pady=(0, 20))

        # ✅ Question Text
        tk.Label(self.current_frame, text=current_q["question"], font=("Arial", 16),
                 fg=TEXT_COLOR, bg=FRAME_COLOR, wraplength=600).pack(pady=20)

        # ✅ Feedback Label
        self.feedback_label = tk.Label(self.current_frame, text="", font=("Arial", 16, "bold"), bg=FRAME_COLOR)
        self.feedback_label.pack(pady=10)

        # ✅ Options Frame
        options_frame = tk.Frame(self.current_frame, bg=FRAME_COLOR)
        options_frame.pack()

        options = current_q["options"].copy()
        random.shuffle(options)
        for option in options:
            btn = tk.Button(options_frame, text=option, font=("Arial", 14), width=40,
                            bg=PRIMARY_BTN_COLOR, fg=TEXT_COLOR, activebackground=BTN_HOVER_COLOR,
                            command=lambda opt=option: self.check_answer(opt))
            btn.pack(pady=5)

    def check_answer(self, selected_option):
        current_q = self.selected_questions[self.current_question_index]
        correct_answer = current_q["answer"]

        if selected_option == correct_answer:
            self.feedback_label.config(text="✅ Correct!", fg=CORRECT_COLOR)
            correct_sound.play()
            self.score += 1
            self.after(800, self.next_question)
        else:
            self.feedback_label.config(text=f"❌ Wrong! Answer", fg=WRONG_COLOR)
            wrong_sound.play()

            self.after(1200, self.next_question)

    def next_question(self):
        self.current_question_index += 1
        if self.current_question_index >= len(self.selected_questions):
            self.show_result()
        else:
            self.show_question()

    def show_result(self):
        self.clear_frame()
        self.current_frame = tk.Frame(self, bg=FRAME_COLOR)
        self.current_frame.pack(pady=80)

        total = len(self.selected_questions)

        tk.Label(self.current_frame, text="🎉 Quiz Completed!", font=("Arial", 24, "bold"),
                 fg=TEXT_COLOR, bg=FRAME_COLOR).pack(pady=20)

        tk.Label(self.current_frame, text=f"{self.username}, your score is {self.score} out of {total}.",
                 font=("Arial", 18), fg=TEXT_COLOR, bg=FRAME_COLOR).pack(pady=20)

        tk.Label(self.current_frame,
                 text=f"Correct: {self.score} ✅   Incorrect: {total - self.score} ❌",
                 font=("Arial", 16), fg=TEXT_COLOR, bg=FRAME_COLOR).pack(pady=10)

        restart_btn = tk.Button(self.current_frame, text="Play Again", font=("Arial", 16, "bold"),
                                bg=PRIMARY_BTN_COLOR, fg=TEXT_COLOR, activebackground=BTN_HOVER_COLOR,
                                command=self.show_category_page)
        restart_btn.pack(pady=30)

if __name__ == "__main__":
    app = KBCApp()
    app.mainloop()
