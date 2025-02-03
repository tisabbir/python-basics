import tkinter as tk
from tkinter import messagebox
import random

# List of words to choose from
WORDS = ["apple", "bread", "crane", "drive", "eagle", "flame", "glove", "house", "input", "joker"]

class WordleApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Wordle Clone")
        self.word = self.get_random_word()
        self.attempts = 6
        self.current_attempt = 0

        # UI Setup
        self.frame = tk.Frame(self.root, bg="#f5f5f5")
        self.frame.pack(pady=20)

        self.title_label = tk.Label(self.frame, text="Wordle Clone", font=("Helvetica", 24, "bold"), bg="#f5f5f5", fg="#333")
        self.title_label.grid(row=0, column=0, columnspan=5, pady=10)

        self.entries = []
        for i in range(self.attempts):
            entry_row = []
            for j in range(5):
                entry = tk.Entry(self.frame, font=("Helvetica", 18), width=2, justify="center")
                entry.grid(row=i+1, column=j, padx=5, pady=5)
                entry_row.append(entry)
            self.entries.append(entry_row)

        self.submit_button = tk.Button(self.frame, text="Submit", command=self.check_guess, font=("Helvetica", 14), bg="#4caf50", fg="white")
        self.submit_button.grid(row=self.attempts+1, column=0, columnspan=5, pady=10)

    def get_random_word(self):
        return random.choice(WORDS).upper()

    def display_feedback(self, guess):
        feedback = []
        for i in range(len(guess)):
            if guess[i] == self.word[i]:
                feedback.append(f"[{guess[i]}]")  # Correct letter in the correct position
                self.entries[self.current_attempt][i].config(bg="#4caf50", fg="white")  # Green
            elif guess[i] in self.word:
                feedback.append(f"({guess[i]})")  # Correct letter in the wrong position
                self.entries[self.current_attempt][i].config(bg="#ffeb3b", fg="black")  # Yellow
            else:
                feedback.append(guess[i])  # Incorrect letter
                self.entries[self.current_attempt][i].config(bg="#f44336", fg="white")  # Red
        return " ".join(feedback)

    def check_guess(self):
        guess = "".join([entry.get().upper() for entry in self.entries[self.current_attempt]])
        if len(guess) != 5 or not guess.isalpha():
            messagebox.showwarning("Invalid Input", "Please enter a valid 5-letter word.")
            return

        feedback = self.display_feedback(guess)
        print(f"Feedback: {feedback}")
        if guess == self.word:
            messagebox.showinfo("Congratulations!", "You guessed the word correctly!")
            self.root.destroy()
        elif self.current_attempt < self.attempts - 1:
            self.current_attempt += 1
        else:
            messagebox.showinfo("Game Over", f"Sorry, you're out of attempts. The word was {self.word}.")
            self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = WordleApp(root)
    root.mainloop()
