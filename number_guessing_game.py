import tkinter as tk
import random

class NumberGuessingGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Number Guessing Game")

        self.total_guesses = 0
        self.max_guesses = 0
        self.secret_number = 0

        self.setup_ui()

    def setup_ui(self):
        # Title label
        tk.Label(self.root, text="Number Guessing Game", font=("Helvetica", 20, "bold")).pack(pady=10)

        # Frame for input fields
        input_frame = tk.Frame(self.root)
        input_frame.pack(pady=10)

        # Input fields and labels
        tk.Label(input_frame, text="Total Guesses:").grid(row=0, column=0, padx=5, pady=5)
        self.guess_entry = tk.Entry(input_frame)
        self.guess_entry.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(input_frame, text="Enter the lower range:").grid(row=1, column=0, padx=5, pady=5)
        self.lower_entry = tk.Entry(input_frame)
        self.lower_entry.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(input_frame, text="Enter the upper range:").grid(row=2, column=0, padx=5, pady=5)
        self.upper_entry = tk.Entry(input_frame)
        self.upper_entry.grid(row=2, column=1, padx=5, pady=5)

        # Start button
        self.submit_button = tk.Button(self.root, text="Start Game", command=self.start_game)
        self.submit_button.pack(pady=10)

        # Result display label
        self.result_label = tk.Label(self.root, text="", font=("Helvetica", 15))
        self.result_label.pack()

        # Guess entry field
        self.guess_label_prompt = tk.Label(self.root, text="Enter your guess:")
        self.guess_label_prompt.pack()
        self.guess_entry_game = tk.Entry(self.root, state=tk.DISABLED)
        self.guess_entry_game.pack()

    def start_game(self):
        try:
            self.max_guesses = int(self.guess_entry.get())
            low = int(self.lower_entry.get())
            high = int(self.upper_entry.get())
            self.secret_number = random.randint(low, high)

            self.total_guesses = 0
            self.result_label.config(text=f"Game started! Make a guess between {low} and {high}")

            # Enable guess entry field and set focus
            self.guess_entry_game.config(state=tk.NORMAL)
            self.guess_entry_game.delete(0, tk.END)
            self.guess_entry_game.focus()

            # Change button command to guess check
            self.submit_button.config(text="Submit Guess", command=self.check_guess)

        except ValueError:
            self.result_label.config(text="Invalid input. Please enter integers.")

    def check_guess(self):
        try:
            guess = int(self.guess_entry_game.get())
            self.total_guesses += 1

            if guess < self.secret_number:
                self.result_label.config(text="The number guessed is low")
            elif guess > self.secret_number:
                self.result_label.config(text="The number guessed is high")
            else:
                self.result_label.config(text=f"The number guessed is right! Total guesses taken: {self.total_guesses}")
                self.submit_button.config(state=tk.DISABLED)
                self.guess_entry_game.config(state=tk.DISABLED)

        except ValueError:
            self.result_label.config(text="Invalid input. Please enter an integer.")

def main():
    root = tk.Tk()
    app = NumberGuessingGame(root)
    root.mainloop()

if __name__ == "__main__":
    main()
